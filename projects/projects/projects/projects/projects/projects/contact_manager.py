"""
Contact Manager
---------------
A simple program to manage contacts using a JSON file.
Created by islandgreedster 🚀
"""

import json
import os

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, email, phone):
        contact = {"name": name, "email": email, "phone": phone}
        self.contacts.append(contact)
        self.save_contacts()

    def show_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact['name']} | {contact['email']} | {contact['phone']}")


# Demo usage
if __name__ == "__main__":
    manager = ContactManager()

    # Add some demo contacts
    manager.add_contact("Alice", "alice@example.com", "123-456-7890")
    manager.add_contact("Bob", "bob@example.com", "987-654-3210")

    print("\n📇 Contact List:")
    manager.show_contacts()


