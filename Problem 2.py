# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:58:13 2023

@author: harv3
"""
def command_menu():
    print("COMMAND MENU")
    print("list - Display All Contacts")
    print("view - View A Contact")
    print("add - Add A Contact")
    print("del - Delete A Contact")
    print("exit - Exit The Program")
    
def display_contacts(contacts):
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}:{contact[0]}")


def view_contact(contacts):
    choice = int(input("Number: "))
    if 1 <= choice <= len(contacts):
        contact = contacts[choice -1]
        print(f"Name: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}\n")
    else:
        print("This is not a valid selection.")
     
      

def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contacts.append([name, email, phone])
    print(f"{name} was added.\n")
    
def del_contact(contacts):
    contact_del = int(input("Number:  "))
    if contact_del <1 or contact_del > len(contacts):
        print("Invalid Selection \n")
    else:
        contact = contacts.pop(contact_del-1)
        print("{} was deleted.\n".format(contact[0]))
    

# Starting data for two contacts
contacts = [
    ["Guido Van Rossum", "guido@guido.com", "7099992107"],
    ["Eric Idle", "eric@ericidle.com", "442079460958"]]

def main():
    command_menu()
    while True:
        choice = input("\nCommand: ")
    
        if choice == 'list':
            display_contacts(contacts)
        elif choice == 'view':
            view_contact(contacts)
        elif choice == 'del':
            del_contact(contacts)
        elif choice == 'add':
            add_contact(contacts)
        elif choice == 'exit':
            print("Bye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()