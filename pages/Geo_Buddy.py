import streamlit as st
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from geopy.extra.rate_limiter import RateLimiter
from io import BytesIO
import pandas as pd 

# Set up the page
st.set_page_config(page_title="Geopy Address Converter", layout="centered")

st.title("📍 Address Geocoder")

st.markdown("""
Upload a CSV with an `address` column and get latitude and longitude added.
""")

# Session state to track file and data
if "df" not in st.session_state:
    st.session_state.df = None
if "geocoded" not in st.session_state:
    st.session_state.geocoded = False

# Step 1: Upload & Verify CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        if "address" not in df.columns:
            st.error("❌ Your file must have an 'address' column.")
        else:
            df["str_add"] = df["address"] + ", Raleigh, NC"
            st.session_state.df = df
            st.session_state.geocoded = False
            st.success(f"✅ File uploaded with {len(df)} rows.")
            st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error reading file: {e}")

# Step 2: Get Coordinates
if st.session_state.df is not None:
    name = st.text_input("Enter a name for the output file (no extension)", "mydata")

    if st.button("Get Coordinates"):
        df = st.session_state.df.copy()
        # Calling the Nominatim tool
        geolocator = Nominatim(user_agent="streamlit-geocoder")

        def get_lat(address):
            try:
                getLoc = geolocator.geocode(address, timeout=10)

                if getLoc:
                    return getLoc.latitude, getLoc.longitude
                else:
                    st.warning(f"Address not found: {address}")
                    return None, None
            except (GeocoderTimedOut, GeocoderServiceError) as e:
                st.warning(f"Error geocoding {address}: {e}")
                return None, None
            except Exception as e:
                st.warning(f"Unexpected error for {address}: {e}")
                return None, None

        with st.spinner("Geocoding in progress...."):
            df[["latitude", "longitude"]] = df["str_add"].apply(lambda x: pd.Series(get_lat(x)))

        st.success("✅ Geocoding complete.")
        st.session_state.geocoded = True
        st.session_state.df = df  # Save updated version
        st.dataframe(df)

        # Show count of failed addresses
        failed = df["latitude"].isna().sum()
        if failed:
            st.warning(f"{failed} addresses could not be geocoded")

# Step 3: Download
if st.session_state.geocoded:
    csv_bytes = st.session_state.df.to_csv(index=False).encode("utf-8")
    filename = f"{name}_coords.csv"

    st.download_button(
        label="Download Geocoded CSV",
        data=csv_bytes,
        file_name=filename,
        mime="text/csv"
    )

            
