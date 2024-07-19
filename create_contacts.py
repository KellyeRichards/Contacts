# create_contacts.py
import json

# Sample contact data
contacts = [
    {
        "name": "John Doe",
        "phone": "+1-800-555-5555",
        "email": "john.doe@example.com"
    },
    {
        "name": "Jane Smith",
        "phone": "+1-800-555-1234",
        "email": "jane.smith@example.com"
    }
]

# Write data to JSON file
with open('contacts.json', 'w') as file:
    json.dump(contacts, file, indent=4)

print("Data written to contacts.json")
