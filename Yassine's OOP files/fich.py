import json

data = {
    "nom": "Jean",
    "age": 25,
    "ville": "Paris"
}

# Writing initial data to JSON file
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

# Reading and printing the initial content
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("Contenu du fichier initial:")
    print(loaded_data)

# Modifying the data
loaded_data["langage"] = "Python"

# Writing modified data back to the JSON file
with open("data.json", "w") as json_file:
    json.dump(loaded_data, json_file, indent=2)

# Reading and printing the modified content
with open("data.json", "r") as json_file:
    modified_data = json.load(json_file)
    print("\nContenu du fichier après modification:")
    print(modified_data)
