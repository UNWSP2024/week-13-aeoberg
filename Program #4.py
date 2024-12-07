import sqlite3


def connect_db():
    return sqlite3.connect('phonebook.db')


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_entry(name, phone_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Entries (name, phone_number)
        VALUES (?, ?)
    ''', (name, phone_number))
    conn.commit()
    conn.close()


def get_phone_number(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT phone_number FROM Entries WHERE name = ?
    ''', (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None


def update_phone_number(name, new_phone_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Entries
        SET phone_number = ?
        WHERE name = ?
    ''', (new_phone_number, name))
    conn.commit()
    conn.close()


def delete_entry(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Entries WHERE name = ?
    ''', (name,))
    conn.commit()
    conn.close()


# Function to display the main menu
def show_menu():
    print("1. Add entry")
    print("2. Look up phone number")
    print("3. Update phone number")
    print("4. Delete entry")
    print("5. Exit")


def main():
    create_table()

    while True:
        show_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_entry(name, phone_number)
            print(f"Entry for {name} added successfully.")

        elif choice == '2':
            name = input("Enter name to look up: ")
            phone_number = get_phone_number(name)
            if phone_number:
                print(f"{name}'s phone number is {phone_number}.")
            else:
                print(f"No phone number found for {name}.")

        elif choice == '3':
            name = input("Enter name to update: ")
            new_phone_number = input("Enter new phone number: ")
            update_phone_number(name, new_phone_number)
            print(f"Phone number for {name} updated successfully.")

        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_entry(name)
            print(f"Entry for {name} deleted successfully.")

        elif choice == '5':
            print("Exiting the phonebook application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


# Run the program
if __name__ == '__main__':
    main()

