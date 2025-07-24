import streamlit as st

st.set_page_config(
    page_title="Welcome to MapBuddy",
    page_icon="👋",
)

st.write("# Welcome to MapBuddy! 👋")

st.sidebar.success("Select your buddy above")

st.markdown(
    """
    MapBuddy was created to make creating geo datasets for ArcGIS easy.

    **👈 Select your buddy from the sidebar** to get started.
    
    ### Choose Your Buddy
    Different buddies for different needs.

    #### 📍 Geo Buddy: Address Geocoder
    *Uses geopy Library*

    *Only works with Raleigh, NC addresses currently*

    ##### :material/checklist: Use Case
    You have: `csv` with `address` column.
    and you need: `csv` with cooresponding `latitude` and `longitude` columns

    Give it a `csv` file with an `address` column and use geopy to add `latitude` and `longitude`.

    Then export the results as a `csv` that can be added as a layer in an ArcGIS map.

    ---

    #### 📌 Overpass Buddy: Place Finder
    *Uses OpenStreetMap Overpass API*

    ##### :material/checklist: Use Case
    You have: `city` and what you want to `filter` by (Restaurants, Libraries, etc.)
    and you need: `csv` with geocoded locations matching your criteria, 
    
    Enter a `city` name, and choose from defined `filters` like `Libraries`, `Restaurants`, or `Hotels`,
    or browse OpenStreetMap map features for `custom filtering` options.

    Then export the results as a `csv` that can be added as a layer in an ArcGIS map.

    """
)