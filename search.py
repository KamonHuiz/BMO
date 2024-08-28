import os
import json
import cv2
import matplotlib.pyplot as plt
global folder_path
'''def search_text_in_json(search_term):
    image_paths = []
    folder_path = "D:\VSCODE\AIC_Model\json_query"
    # Walk through all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                json_path = os.path.join(root, file)
                
                # Load JSON file
                with open(json_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    
                    # Search for the text in the JSON data
                    for entry in data:
                        if search_term.lower() in entry["text"].lower():
                            image_paths.append(entry["image_path"])
    length = len(image_paths)
    while (length >= 10):
        length = length - 5
    # Print the found image paths
    if image_paths:
        print("Found image paths:", length)
    else:
        print(f"No entries found containing the term '{search_term}'.")
    
    


    return image_paths[0:round(length)]
'''


def search_text_in_json(search_term):
    image_paths = []
    folder_path = r"D:/VSCODE/AIC_Model/json_query"  # Use raw string to handle backslashes
    # Walk through all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                json_path = os.path.join(root, file)
                
                # Load JSON file
                try:
                    with open(json_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file {json_path}: {e}")
                    continue  # Skip this file if it can't be parsed
                
                # Check if the data is a list (adjust if needed based on your actual structure)
                if isinstance(data, list):
                    for entry in data:
                        # Ensure entry is a dictionary and has the required keys
                        if isinstance(entry, dict) and "text" in entry and "image_path" in entry:
                            # Search for the text in the JSON data
                            if search_term.lower() in entry["text"].lower():
                                image_paths.append(entry["image_path"])
    length = len(image_paths)
    while (length >= 200):
        length = length - 5
    # Print the found image paths
    if image_paths:
        print("Found image paths:", length)
        print(search_term)

    else:
        print(f"No entries found containing the term '{search_term}'.")
    for i in image_paths[0:round(length)]:
        print(i)  
    return image_paths[0:round(length)]
