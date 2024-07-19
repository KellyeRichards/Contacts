import json

# Path to the JSON file
file_path = '/Users/kellye/Desktop/PythonProjects/JSON/contacts.json'

# New contact to add
new_contact = {
    "name": "Alice Johnson",
    "phone": "+1-800-555-6789",
    "email": "alice.johnson@example.com"
}

# Read existing data
with open(file_path, 'r') as file:
    contacts = json.load(file)

# Add new contact
contacts.append(new_contact)

# Write updated data back to JSON file
with open(file_path, 'w') as file:
    json.dump(contacts, file, indent=4)

print("New contact added successfully.")
