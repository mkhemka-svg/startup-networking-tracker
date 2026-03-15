# Startup Networking Tracker

# What this app tracks & why I chose it
This app tracks my professional and startup-related networking contacts. I chose this topic because it is personally useful for keeping track of who I met, what organization they are from, when I contacted them and whether I need to follow up with them.

# My database schema
This app uses one SQLite table called `contacts`.

The columns and their respective data types are as follows:
1. id: INTEGER (Primary key, auto-incrementing unique id)
2. name: TEXT (Name of the contact)
3. organisation: TEXT (Company, startup, or institution)
4. category: TEXT (Type of contact)
5. date_contacted: TEXT (Date the contact was reached out to)
6. follow_up_status: TEXT (Follow-up status)
7. notes: TEXT (Additional notes about the interaction)

# How to run the app
1. Make sure Python 3 is installed.
2. Open Terminal and go to the project folder "startup-networking-tracker.
3. Run:
python3 networking_tracker.py

# Brief description of each CRUD operation and how a user performs it

1. CREATE: Choose option 1 from the menu to add a new contact. The app asks for the contact's name, organization, category, date contacted, follow-up status and notes.
2. READ: Choose option 2 to view all contacts currently stored in the database. Choose option 3 to search for contacts by category; the user enters a category and the app shows matching records.
3. UPDATE: Choose option 4 to update a contact. The user enters the contact's id, reviews the current record and then types the new entries.
4. Choose option 5 to delete a contact. The user enters the contact's id, reviews the record and confirms deletion.

