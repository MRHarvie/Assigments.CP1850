# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:15:12 2023

@author: harv3
"""

import csv
import os

    
def command_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact ")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program\n")
    

def read_contacts():
    
 
    file_path = 'contacts.csv'
    contacts = []

    # Check if the file exists using os.path.isfile()
    
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            contacts = [row for row in reader]

    return contacts


def write_contacts(contacts):
  
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
        
        # Writes each contact in a row instead of on one line.
        

def add_contact(contacts):
 
    name = input("Name: ")
    email = input("Email: ")
    phone_number = input("Phone: ")
    new_contact = [name, email, phone_number]
    contacts.append(new_contact)
    write_contacts(contacts)
    print(f"{name} was added.")
    
def delete_contact(contacts):
    list_contact(contacts)
    if contacts:
        number = int(input("Number: "))
        if 1 <= number <= len(contacts):
            deleted_contact = contacts.pop(number - 1)
            write_contacts(contacts)
            print(f"{deleted_contact[0]} was deleted.")
        else:
            print("Invalid Selection.")
    else:
        print("No contacts to delete.")
        

def list_contact(contacts):
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]}")

def view_contact(contacts):
    contact_number = int(input("Number: "))
    if 1 <= contact_number <= len(contacts):
        contact = contacts[contact_number - 1]
        print(f"Name: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
    else:
        print("Invalid selection. Please try again.")



def main():
    print("Contact Manager\n")
    contacts = read_contacts()
    command_menu()
    while True:
        command = input("\nCommand: ").lower()
        if command == 'list':
            list_contact(contacts)
        elif command == 'view':
            view_contact(contacts)
        elif command == 'add':
            add_contact(contacts)
        elif command == 'del':
            delete_contact(contacts)
        elif command == 'exit':
            print("\nBye!")
            break
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == '__main__':
    main()
    
    