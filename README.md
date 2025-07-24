# 🗺️ MapBuddy


**MapBuddy** is a lightweight, interactive web app built with [Streamlit](https://streamlit.io/) that helps you quickly visualize and map location data using OpenStreetMap's Overpass API and address geocoding tools.

Whether you're searching for public points of interest (like grocery stores or restaurants) or enriching your own CSV files with geolocation data, MapBuddy has you covered — no GIS expertise required.

<br>

## 🚀 Features

### 🔍 Overpass Query Tool
- Search any `city` for selected types of places (e.g. `supermarkets`, `libraries`, `cafes`, `coworking spaces`, etc.)
- Based on live data from OpenStreetMap
- Visualize results on a map
- Export results to `CSV`

### 📍 Address Geocoder
- Upload a `CSV` file with an `address` column
- Automatically geocode each address (adding `latitude`/`longitude`) using Nominatim (OpenStreetMap)
- Logs failed addresses and supports custom output naming
- Download the enriched file as a `CSV`


<br>

## 🧑‍💻 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/ksg-dev/map-buddy.git
cd map-buddy
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run Hello.py
```


<br>

## 🌐 Live Demo

You can try it instantly on [Streamlit Cloud](https://map-buddy-geotools.streamlit.app) or by clicking the badge below:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://map-buddy-geotools.streamlit.app)

<br>

## 📁 Project Structure

```
map-buddy/
├── Hello.py                # Home page
├── pages/
│   └── Geo_Buddy.py        # Address Geocoder
│   └── Overpass_Buddy.py   # City Place Finder (Streamlit multipage)
├── requirements.txt        # Required Python libraries
└── README.md               # This file
```

<br>

## 🧩 Built With

* [Streamlit](https://streamlit.io/) – UI and deployment
* [OpenStreetMap + Overpass API](https://overpass-turbo.eu/) – Public location data
* [Geopy (Nominatim)](https://geopy.readthedocs.io/) – Address geocoding
* [Pandas](https://pandas.pydata.org/) – Data manipulation

<br>

## 🛡️ Notes

* The Overpass API and Nominatim geocoding services have rate limits. MapBuddy is designed for small-to-medium sized datasets.
* Always verify and clean address data before geocoding for best results.

<br>

## 🧠 Ideas for Future Enhancements

* 🌍 Expand Geocoding to handle different city/st
* ✅ Save/load previous queries
* ✅ Custom city bounding box input
* 🌍 Add bounding box-based search (instead of city name)
* 🔄 Batch processing with queueing
* 🗂️ Shapefile or GeoJSON export
* 🔐 Optional login for saving user maps

<br>

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

<br>

## 🤝 Contributing

Contributions, ideas, and suggestions are welcome! Feel free to open an issue or pull request.

<br>

## 👋 Author

Built with 💙 by \ksg-dev
GitHub: [@ksg-dev](https://github.com/ksg-dev)

---
