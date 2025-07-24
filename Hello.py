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

    #### Overpass Buddy
    *Uses OpenStreetMap Overpass API*

    Use this buddy when you want to find certain types of locations in a city. 
    
    Enter a **city name**, and **choose from defined filters like Libraries, Restaurants, or Hotels,** 
    or browse OpenStreetMap map features for custom filtering options.

    Then export the results as a csv that can be added as a layer in an ArcGIS map.

    #### Geo Buddy
    *Uses geopy Library*

    *Only works with Raleigh, NC addresses currently*

    ##### :material/checklist: Use Case
    You have: `csv` with `address` column.
    and you need: `csv` with cooresponding `latitude` and `longitude` columns

    Use this buddy when you have a **list of places and their addresses, but you need latitude and longitude.**
    Give it a **csv file with an address column** and use geopy to add latitude and longitude.

    Then export the results as a csv that can be added as a layer in an ArcGIS map."""
)