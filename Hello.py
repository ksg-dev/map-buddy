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
    """)

st.markdown(
    """
    #### 📍 Geo Buddy: Address Geocoder
    *Uses geopy Library*

    *Only works with Raleigh, NC addresses currently*

    ##### :material/checklist: Use Case
    :green-badge[:material/task_alt: You have] `csv` with `address` column.\n
    :orange-badge[:material/pending: You need] `csv` with cooresponding `latitude` and `longitude` columns

    ##### :material/info: About
    Give it a `csv` file with an `address` column and use geopy to add `latitude` and `longitude`.

    Then export the results as a `csv` that can be added as a layer in an ArcGIS map.
"""
)

st.divider()

    
st.markdown(
    """
    #### 📌 Overpass Buddy: Place Finder
    *Uses OpenStreetMap Overpass API*

    ##### :material/checklist: Use Case
    :green-badge[:material/task_alt: You have] `city` and what you want to `filter` by (`Restaurants`, `Libraries`, etc.)\n
    :orange-badge[:material/pending: You need] `csv` with geocoded locations matching your criteria, 
    
    ##### :material/info: About
    Enter a `city` name, and choose from defined `filters` like `Libraries`, `Restaurants`, or `Hotels`,
    or browse OpenStreetMap map features for `custom filtering` options.

    Then export the results as a `csv` that can be added as a layer in an ArcGIS map."""
)

    