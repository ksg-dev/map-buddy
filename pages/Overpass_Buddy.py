import streamlit as st
import requests
import pandas as pd 

# Set up the page
st.set_page_config(page_title="📌 Overpass Place Finder", layout="centered")

st.title("📌 Overpass Buddy: Place Finder")
st.markdown("Search for places in a city using OpenStreetMap Overpass API, and export to csv for use in ArcGIS maps.")

# Inputs
city = st.text_input("Enter a city (e.g. Raleigh)", "Raleigh")

default_filters = "shop=supermarket, amenity=restaurant, amenity=cafe"
# Predefined Overpass filter options
filter_options = {
    "Supermarket": "shop=supermarket",
    "Grocery Store": "shop=grocery",
    "Restaurant": "amenity=restaurant",
    "Cafe": "amenity=cafe",
    "Bar": "amenity=bar",
    "Library": "amenity=library",
    "Pharmacy": "amenity=pharmacy",
    "Park": "leisure=park",
    "Co-working Space": "office=co_working",
    "Hotel": "tourism=hotel"
}

selected_labels = st.multiselect(
    "Choose place types to search for:",
    options=list(filter_options.keys()),
    default=["Supermarket", "Restaurant", "Cafe"]
)

filters = [filter_options[label] for label in selected_labels]

custom_filter = st.text_input("Or enter a custom Overpass tag (e.g. amenity=theatre, see: OpenStreetMaps features for available options below)")
# Link to OpenStreetMap Tags Wiki
tags_url = "https://wiki.openstreetmap.org/wiki/Map_features#Amenity"
st.link_button("Explore OpenStreetMap Filters", tags_url, help="View all available filters on OpenStreetMap Wiki", icon=":material/interests:")

if custom_filter and "=" in custom_filter:
    filters.append(custom_filter.strip())

if st.button("Run Query"):
    if not city:
        st.warning("Plese enter a city")
    else:
        with st.spinner("Querying Overpass API..."):
            
            # Build Overpass Query
            filter_str = "\n".join([
                f'  node["{tag.split("=")[0]}"="{tag.split("=")[1]}"](area.a);'
                for tag in filters
            ])
            query = f"""
            [out:json];
            area["name"="{city}"]["admin_level"="8"]->.a;
            (
            {filter_str}
            );
            out center;
            """

            # Call Overpass API
            try:
                url = "https://overpass-api.de/api/interpreter"
                response = requests.get(url, params={"data": query})
                response.raise_for_status()
                data = response.json()

                # Parse results
                places = []
                for element in data.get("elements", []):
                    tags = element.get("tags", {})
                    name = tags.get("name", "Unnamed")
                    lat = element.get("lat")
                    lon = element.get("lon")
                    for tag in filters:
                        k, v = tag.split('=')
                        if tags.get(k) == v:
                            places.append({
                                "Name": name,
                                "Category": v,
                                "Latitude": lat,
                                "Longitude": lon
                            })
                            break
                
                # Show results
                if places:
                    df = pd.DataFrame(places)
                    st.success(f"Found {len(places)} places")
                    st.dataframe(df)

                    # Optional: Show on a map if coords present
                    if "Latitude" in df.columns and "Longitude" in df.columns:
                        st.subheader("📍 Map of Results")
                        st.map(df.rename(columns={'Latitude': 'lat', "Longitude": 'lon'}))

                    # Download button
                    csv = df.to_csv(index=False).encode("utf-8")
                    st.download_button("Download CSV", data=csv, file_name="places.csv", mime="text/csv")
                else:
                    st.info("No places found for the given criteria")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
