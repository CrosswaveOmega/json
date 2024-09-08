import json
import os
from typing import *

"""
Utilities for updating the JSON files

"""


def search_json_by_name(
    file_path: str, value: Any, field: str = "name"
) -> List[Tuple[str, Any]]:
    """
    Search for entries in the JSON file with a specified value at a given field.

    Args:
    - file_path (str): Path to the JSON file.
    - value (Any): The value to search for.
    - field (str, optional): The field to search in. Defaults to 'name'.

    Returns:
    - List[Tuple[str,Any]]: A list of tuple pairs containing the key and the matching entry.
    """
    matching_entries = []

    # Load JSON file
    with open(file_path, "r") as f:
        data = json.load(f)

    # Iterate through each entry in the JSON data
    for key, entry in data.items():
        # Check if 'name' field exists and matches the search string (case insensitive)
        if field in entry:
            current = str(entry[field])
            if current.lower() == value.lower():
                matching_entries.append((key, entry))

    return matching_entries


def update_json_file(
    file_path: str, key: str, updates: Dict[str, Dict[str, Any]], over: bool = False
):
    """
    Update fields in the JSON file for a specified key.

    Args:
    - file_path (str): Path to the JSON file.
    - key (str): The key for which the updates should be applied.
    - updates (Dict[str, Dict[str, Any]]): A dictionary where keys are the fields to be updated
      and values are the new values to set.
    - over (bool): if a new entry should be made at key if not present already.
    Returns:
    - None
    """
    # Load JSON file
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    # Check if the key exists in the JSON data
    if key in data:
        # Update fields for the specified key
        for field, value in updates.items():
            data[key][field] = value
    else:
        if over:
            data[key] = updates
        else:
            print(f"Key '{key}' not found in the JSON file.")

    # Write updated JSON back to the file
    with open(file_path, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4)


def load_and_merge_json_files(directory_path: str):
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
            with open(file_path, "r", encoding="utf8") as f:
                try:
                    json_data = json.load(f)
                    # Remove file extension from filename
                    file_key = os.path.splitext(filename)[0]
                    planets_data[file_key] = json_data
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON from {filename}: {e}")

    return planets_data


"""
file_path = 'hd2json/planets/planets.json'  # Replace with your JSON file path
tosearch=["X-45", "GACRUX", "BARABOS", "ASPEROTH PRIME", "SEASSE", "PHERKAD SECUNDUS", "NABATEA SECUNDUS", "CAPH", "FORNSKOGUR II", "IVIS", "BORE ROCK", "CLASA", "KRAKABOS" ]
for search_string in tosearch:
    results = search_json_by_name(file_path, search_string)
    print(results)

file_path = 'hd2json/planets/planets.json'  # Replace with your JSON file path

to_search=["Nublaria I",
"Solghast",
"Atrama",
"Tarsh",
"Ratch",
"Bashyr",
"Iro",
"Socorro III",
"Gar Haren",
"Khandark",
"Klaka 5",
"Merga IV",
"Setia",
"Skitter"]

#tosearch=["X-45", "GACRUX", "BARABOS", "ASPEROTH PRIME", "SEASSE", "PHERKAD SECUNDUS", "NABATEA SECUNDUS", "CAPH", "FORNSKOGUR II", "IVIS", "BORE ROCK", "CLASA", "KRAKABOS" ]
for search_string in to_search:
    results = search_json_by_name(file_path, search_string)

    # Print results
    if results:
        print(f"Found {len(results)} matching entries for name '{search_string}':")
        for key, entry in results:

            updates = {
                'biome': 'haunted_swamp',
                'environmentals': ['thick_fog']
            }

            update_json_file(file_path, key, updates)
            print(f"Key: {key}")
            print(json.dumps(entry, indent=4))
            print("-" * 20)
    else:
        print(f"No entries found for name '{search_string}'.")
"""


def search_and_replace_in_json(
    file_path: str, search_string: str, key: str, updates: Dict[str, Any]
) -> None:
    """Get Entries in json that have value search string at field key,
    modifying the entry based on the updates dictionary.



    """
    results: List[Dict[str, Any]] = search_json_by_name(file_path, search_string, key)

    # Print results
    if results:
        print(f"Found {len(results)} matching entries for name '{search_string}':")
        for key, entry in results:
            update_json_file(file_path, key, updates)
            print(f"Key: {key}")
            print(json.dumps(entry, indent=4))
            print("-" * 20)
    else:
        print(f"No entries found for name '{search_string}'.")


# search_and_replace_in_json(
#     "hd2json/planets/planets.json",
#     "toxic",
#     "biome",
#     {"environmentals": ["acid_storms"]},
# )
def add_planet_effect(idval: int, name: str = "none", desc: str = "none"):
    """add a new planet effect."""
    update_json_file(
        "hd2json/effects/planetEffects.json",
        idval,
        {"galacticEffectId": idval, "name": name, "desc": desc},
        over=True,
    )


"""
add_planet_effect(1177, "black hole", "This planet is a black hole.")

add_planet_effect(
    1186, "light gloom", "This planet is lightly obscured by a gloom cloud."
)

add_planet_effect(1187, "gloom", "A gloom cloud enveloped this world.")

add_planet_effect(
    1188, "heavy gloom", "A thick gloom cloud obscures this world from view."
)

add_planet_effect(1190, "unreachable", "Our sensors can no longer monitor this planet.")
"""

biome_changes={
    'mesa':'sandy_base',
    'toxic':'sandy_acid',
    'moon':'sandy_moon',
    'canyon':'sandy_mineral',
    'desert':'sandy_spiky',
    'jungle':'primordial_base',
    'wasteland':'primordial_dead',
    'ethereal':'primordial_purple',
    'rainforest':'primordial_blue',
    'supercolony':'primordial_bug',
    'winter':'arctic_glacier_base',
    'icemoss':'arctic_glacier_coldrocky',
    'highlands':'moor_baseplanet',
    'tundra':'moor_tundra',
    'desolate':'moor_arid',
    'crimsonmoor':'moor_red',
    'swamp':'swamp_base',
    'haunted_swamp':'swamp_haunted'

}
""" 
with open('hd2json/planets/biomes.json', "r") as f:
    data = json.load(f)
for old, new in biome_changes.items():
    search_and_replace_in_json(
        "hd2json/planets/planets.json",
        old,
        "biome",
        {"biome": new},
    )
    if old in data:
        last=data.pop(old)
        last['old_slug']=old
        data[new]=last

    old = f"{old}"
    new = f"{new}"
    image_folder = "assets/allimages"

    old_image_path = os.path.join(image_folder, f"{old}.png")
    new_image_path = os.path.join(image_folder, f"{new}.png")

    if os.path.exists(old_image_path):
        os.rename(old_image_path, new_image_path)
    else:
        print(f"Image {old}.png not found in {image_folder}.")
    
with open('hd2json/planets/biomes.json', "w", encoding="utf8") as f:
    json.dump(data, f, indent=4) """
vjson = load_and_merge_json_files("./hd2json/planets/")
json.dump(vjson, open("allplanet.json", "w"), indent=4)
