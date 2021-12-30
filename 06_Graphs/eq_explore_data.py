import json

# Explore the structure data
filename = 'data/1.0_week.geojson'
with open(filename, encoding="utf8") as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)