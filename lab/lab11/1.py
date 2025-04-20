import psycopg2

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "12345",
    "host": "localhost",
    "port": "5432"
}

def call_search_pattern(pattern):
    with psycopg2.connect(**DB_PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
            results = cur.fetchall()
            print("\n Search results:")
            for row in results:
                print(row)

def call_insert_or_update_user(name, phone):
    with psycopg2.connect(**DB_PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
            conn.commit()
            print(f" User '{name}' inserted/updated.")

def call_insert_many_users(names, phones):
    with psycopg2.connect(**DB_PARAMS) as conn:
        with conn.cursor() as cur:
            cur.callproc("insert_many_users", (names, phones))
            invalid = cur.fetchone()
            print("\n Invalid entries:")
            for item in invalid[0]:
                print(" -", item)

def call_paginated_users(limit, offset):
    with psycopg2.connect(**DB_PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_users_paginated(%s, %s)", (limit, offset))
            results = cur.fetchall()
            print(f"\n Page (limit={limit}, offset={offset}):")
            for row in results:
                print(row)

def call_delete_user(identifier):
    with psycopg2.connect(**DB_PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_user(%s)", (identifier,))
            conn.commit()
            print(f"User with name or phone '{identifier}' deleted.")

def menu():
    while True:
        print("\n PHONEBOOK MENU")
        print("1. Search by pattern")
        print("2. Insert or update one user")
        print("3. Insert multiple users")
        print("4. View paginated users")
        print("5. Delete by name or phone")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == '1':
            pattern = input("Enter search pattern: ")
            call_search_pattern(pattern)
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            call_insert_or_update_user(name, phone)
        elif choice == '3':
            count = int(input("How many users? "))
            names = []
            phones = []
            for _ in range(count):
                name = input("Name: ")
                phone = input("Phone: ")
                names.append(name)
                phones.append(phone)
            call_insert_many_users(names, phones)
        elif choice == '4':
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            call_paginated_users(limit, offset)
        elif choice == '5':
            identifier = input("Enter username or phone to delete: ")
            call_delete_user(identifier)
        elif choice == '6':
            print("Exiting")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
