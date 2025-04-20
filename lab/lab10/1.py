import psycopg2
import csv

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "12345",
    "host": "localhost",
    "port": "5432"
}

def connect():
    return psycopg2.connect(**DB_PARAMS)

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, 'r', encoding='utf-8', errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row['first_name'], row['phone']))
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV.")

def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from console.")

def update_name(old_name, new_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    conn.commit()
    cur.close()
    conn.close()
    print("Name updated.")

def update_phone(name, new_phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()
    print("Phone number updated.")

def query_by_name(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", ('%' + name + '%',))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()

def query_by_phone(phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", ('%' + phone + '%',))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()

def delete_by_name(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Entry deleted by name.")

def delete_by_phone(phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    cur.close()
    conn.close()
    print("Entry deleted by phone.")

def menu():
    create_table()
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update name")
        print("4. Update phone")
        print("5. Query by name")
        print("6. Query by phone")
        print("7. Delete by name")
        print("8. Delete by phone")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            fname = input("Enter CSV file path: ")
            insert_from_csv(fname)
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            old = input("Old name: ")
            new = input("New name: ")
            update_name(old, new)
        elif choice == '4':
            name = input("Name to update phone for: ")
            phone = input("New phone number: ")
            update_phone(name, phone)
        elif choice == '5':
            name = input("Enter name to search: ")
            query_by_name(name)
        elif choice == '6':
            phone = input("Enter phone to search: ")
            query_by_phone(phone)
        elif choice == '7':
            name = input("Enter name to delete: ")
            delete_by_name(name)
        elif choice == '8':
            phone = input("Enter phone to delete: ")
            delete_by_phone(phone)
        elif choice == '9':
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
