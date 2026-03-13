import json
import csv

with open("data.json") as f:
    data = json.load(f)

with open("output.csv", "w", newline="") as f:

    writer = csv.DictWriter(f, fieldnames=data[0].keys())

    writer.writeheader()
    writer.writerows(data)

print("Converted JSON to CSV")
