import sqlite3

con = sqlite3.connect("networking_tracker.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    organization TEXT,
    category TEXT,
    date_contacted TEXT,
    follow_up_status TEXT,
    notes TEXT
)
""")

con.commit()

def add_contact():
    name = input("Enter contact name: ")
    organization = input("Enter organization: ")
    category = input("Enter category: ")
    date_contacted = input("Enter date contacted (YYYY-MM-DD): ")
    follow_up_status = input("Enter follow-up status: ")
    notes = input("Enter notes: ")

    cur.execute("""
    INSERT INTO contacts (name, organization, category, date_contacted, follow_up_status, notes)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, organization, category, date_contacted, follow_up_status, notes))

    con.commit()
    print("Contact added successfully!")

def show_all_contacts():
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    print("\nAll Contacts:")
    for row in rows:
        print(row)

def filter_by_category():
    category = input("Enter a category to search for: ")

    cur.execute("SELECT * FROM contacts WHERE category = ?", (category,))
    rows = cur.fetchall()

    print("\nMatching Contacts:")
    if len(rows) == 0:
        print("No matching contacts found.")
    else:
        for row in rows:
            print(row)

def update_contact():
    contact_id = input("Enter the ID of the contact to update: ")

    cur.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    row = cur.fetchone()

    if row is None:
        print("No contact found with that ID.")
        return

    print("\nCurrent Contact:")
    print(row)

    name = input("Enter new name: ")
    organization = input("Enter new organization: ")
    category = input("Enter new category: ")
    date_contacted = input("Enter new date contacted (YYYY-MM-DD): ")
    follow_up_status = input("Enter new follow-up status: ")
    notes = input("Enter new notes: ")

    cur.execute("""
        UPDATE contacts
        SET name = ?, organization = ?, category = ?, date_contacted = ?, follow_up_status = ?, notes = ?
        WHERE id = ?
    """, (name, organization, category, date_contacted, follow_up_status, notes, contact_id))

    con.commit()
    print("Contact updated successfully!")

def delete_contact():
    contact_id = input("Enter the ID of the contact to delete: ")

    cur.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    row = cur.fetchone()

    if row is None:
        print("No contact found with that ID.")
        return

    print("\nContact to Delete:")
    print(row)

    confirm = input("Are you sure you want to delete this contact? (yes/no): ")

    if confirm.lower() == "yes":
        cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        con.commit()
        print("Contact deleted successfully!")
    else:
        print("Delete canceled.")


def main():
    while True:
        print("\n--- Startup Networking Tracker ---")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search contacts by category")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

main()
con.close()

