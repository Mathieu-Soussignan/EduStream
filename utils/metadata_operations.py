import json
import os
from datetime import datetime

METADATA_PATH = "data/metadata.json"

def load_metadata():
    if not os.path.exists(METADATA_PATH):
        return {}
    with open(METADATA_PATH, "r") as file:
        return json.load(file)

def save_metadata(metadata):
    with open(METADATA_PATH, "w") as file:
        json.dump(metadata, file, indent=4)

def update_metadata(title, category):
    metadata = load_metadata()
    filename = title.replace(" ", "_").lower() + ".md"
    metadata[filename] = {
        "title": title,
        "category": category,
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_metadata(metadata)