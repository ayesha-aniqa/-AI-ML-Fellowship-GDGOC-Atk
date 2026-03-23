#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json

class ContactManager:
    def __init__(self, file="contacts.json"):
        self.file = file
        try:
            with open(file, 'r') as f: self.contacts = json.load(f)
        except: self.contacts = []
            
#saving contacts
    def save(self):
        with open(self.file, 'w') as f: json.dump(self.contacts, f, indent=2)

#reading the contacts
    def view(self):
        if not self.contacts: print("No contacts available.")
        for i, c in enumerate(self.contacts, 1): 
            print(f"{i}. {c['name']} | {c['phone']}")

#updatin the contacts
    def update(self, i):
        if 0 <= i < len(self.contacts):
            name, phone = input("New name: "), input("New phone: ")
            if name: self.contacts[i]['name'] = name
            if phone: self.contacts[i]['phone'] = phone
            self.save()
        else: print("Invalid index.")

def main():
    cm = ContactManager()
    while True:
        choice = input("\n1. Add 2. View 3. Update 4. Exit: ")
        if choice == "1":
            cm.contacts.append({"name": input("Name: "), "phone": input("Phone: ")})
            cm.save()
        elif choice == "2":
            cm.view()
        elif choice == "3":
            cm.view()
            try: cm.update(int(input("Number to update: ")) - 1)
            except: print("Invalid input.")
        elif choice == "4": break

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




