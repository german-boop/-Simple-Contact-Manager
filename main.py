# The following is an English version of the code, formatted in accordance with PEP 8 and PEP 257 standards. It includes clearly organized modules and function docstrings, along with comprehensive inline comments for better understanding.

"""
Simple Contact Manager

This module provides a simple script to add contacts to a text file
called 'contacts.txt'. Each contact consists of a name and a phone number
and is stored on a new line in the file.

Usage:
    Run this script directly to add a new contact.
"""


def add_contact(filename="contacts.txt"):
    """
    Prompt the user to enter a contact name and phone number,
    then save it to 'contacts.txt'.

    This function opens 'contacts.txt' in append mode, writes
    the contact in the format 'name - phone', and prints a
    confirmation message.

    Args:
        filename (str): Name of the file to save contacts to.
    """
    # 🎯 Prompt for contact info
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    # Validate input
    if not name or not phone:
        print("❌ Name or phone cannot be empty!")
        return

    # 📝 Save contact to file with error handling
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{name} - {phone}\n")
    except IOError as e:
        print(f"❌ Failed to save contact: {e}")
        return

    print("\n✅ Contact saved successfully!\n")


# 🚀 Run the manager
if __name__ == "__main__":
    add_contact()


