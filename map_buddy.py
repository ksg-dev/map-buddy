import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import pandas as pd 

def build_overpass_query(city, filters):
    filter_str = "\n".join([
        f'  node["{tag.split("=")[0]}"="{tag.split("=")[1]}"](area.a);'
        for tag in filters
    ])
    return f"""
    [out:json];
    area["name"="{city}"]["admin_level"="8"]->.a;
    (
    {filter_str}
    );
    out center;
    """

def fetch_places(city, filters):
    url = "https://overpass-api.de/api/interpreter"
    query = build_overpass_query(city, filters)
    response = requests.get(url, params={'data': query})
    response.raise_for_status()
    data = response.json()

    results = []
    for element in data.get("elements", []):
        tags = element.get("tags", {})
        lat = element.get("lat")
        lon = element.get("lon")
        name = tags.get("name", "Unnamed")
        for tag in filters:
            k, v = tag.split('=')
            if tags.get(k) == v:
                results.append({
                    "Name": name,
                    "Category": v,
                    "Latitude": lat,
                    "Longitude": lon
                })
                break
    return results

def run_query():
    city = city_entry.get().strip()
    raw_filters = filter_entry.get().strip()
    filters = [f.strip() for f in raw_filters.split(",") if "=" in f]

    if not city or not filters:
        messagebox.showwarning("Missing Input", "Please enter a city and at least one valid filter (e.g., shop=supermarket).")
        return
    
    try:
        places = fetch_places(city, filters)
        if not places:
            messagebox.showinfo("No Results", "No matches found for the given city and filters")
            return
    
        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csvv")],
            title="Save Results As"
        )

        if save_path:
            df = pd.DataFrame(places)
            df.to_csv(save_path, index=False)
            messagebox.showinfo("Success", f"Exported {len(df)} rows to:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


# GUI Layout
root = tk.Tk()
root.title("Overpass Place Finder")
root.geometry("460x260")
root.resizable(False, False)

tk.Label(root, text="City (e.g. Raleigh):").pack(pady=(15, 0))
city_entry = tk.Entry(root, width=50)
city_entry.pack()

tk.Label(root, text="Filters (comma-separated, e.g. shop=supermarket, amenity=restaurant):").pack(pady=(15, 0))
filter_entry = tk.Entry(root, width=50)
filter_entry.pack()

run_button = tk.Button(root, text="Run Query and Export CSV", command=run_query, bg="#007acc", fg="white")
run_button.pack(pady=25)

tk.Label(root, text="Powered by OpenStreetMap Overpass API", fg="gray").pack(side="bottom", pady=5)

root.mainloop()