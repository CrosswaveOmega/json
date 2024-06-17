import json
import os

'''
Utilities for updating the JSON files

'''

def search_json_by_name(file_path, name,field='name'):
    matching_entries = []

    # Load JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Iterate through each entry in the JSON data
    for key, entry in data.items():
        # Check if 'name' field exists and matches the search string (case insensitive)
        if field in entry and entry[field].lower() == name.lower():
            matching_entries.append((key, entry))

    return matching_entries

def update_json_file(file_path, key, updates):
    # Load JSON file
    with open(file_path, 'r',encoding='utf8') as f:
        data = json.load(f)

    # Check if the key exists in the JSON data
    if key in data:
        # Update fields for the specified key
        for field, value in updates.items():
            data[key][field] = value
    else:
        print(f"Key '{key}' not found in the JSON file.")

    # Write updated JSON back to the file
    with open(file_path, 'w',encoding='utf8') as f:
        json.dump(data, f, indent=4)



def load_planets_from_directory(directory_path):
    """
    Load all JSON files from the specified directory into a single dictionary.

    Args:
    - directory_path (str): Path to the directory containing JSON files.

    Returns:
    - dict: A dictionary where keys are file names (without extension) and values are loaded JSON data.
    """
    planets_data = {}

    # Validate directory path
    if not os.path.isdir(directory_path):
        raise ValueError(f"Directory '{directory_path}' does not exist.")

    # Load JSON files
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r',encoding='utf8') as f:
                try:
                    json_data = json.load(f)
                    # Remove file extension from filename
                    file_key = os.path.splitext(filename)[0]
                    planets_data[file_key] = json_data
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON from {filename}: {e}")

    return planets_data

'''
file_path = 'hd2json/planets/planets.json'  # Replace with your JSON file path
tosearch=["X-45", "GACRUX", "BARABOS", "ASPEROTH PRIME", "SEASSE", "PHERKAD SECUNDUS", "NABATEA SECUNDUS", "CAPH", "FORNSKOGUR II", "IVIS", "BORE ROCK", "CLASA", "KRAKABOS" ]
for search_string in tosearch:
    results = search_json_by_name(file_path, search_string)

    # Print results
    if results:
        print(f"Found {len(results)} matching entries for name '{search_string}':")
        for key, entry in results:
            
            updates = {
                'biome': 'rainyjungle',
                'environmentals': ['rainstorms']
            }

            update_json_file(file_path, key, updates)
            print(f"Key: {key}")
            print(json.dumps(entry, indent=4))
            print("-" * 20)
    else:
        print(f"No entries found for name '{search_string}'.")
'''