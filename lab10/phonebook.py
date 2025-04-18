import psycopg2
import csv

def get_conn(): #соединение с базой данных
    return psycopg2.connect(
        dbname="mydb",    
        user="postgres",     
        password="7355608", 
        host="localhost",
        port="5432"
    )

# создать
def create_table():
    conn = get_conn()
    cur = conn.cursor() # Создать cursor object чтобы взаимодействовать с db
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# С csv
def insert_from_csv(filename):
    conn = get_conn()
    cur = conn.cursor()
    with open(filename, 'r') as f: 
        reader = csv.DictReader(f) #читает содержимое файла как словарь
        for row in reader:
            cur.execute(
                "INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;",
                (row['first_name'], row['phone'])
            )
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV.")

# С консоля
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;",
        (name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from console.")

# Обновлять
def update_user():
    phone = input("Enter phone of the user to update: ")
    new_name = input("Enter new name: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE PhoneBook SET first_name = %s WHERE phone = %s",
        (new_name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("User updated.")

# Искать по имени или номеру
def search_by_name():
    conn = get_conn()
    name = input("Enter name to search: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s", (f"%{name}%",))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def search_by_phone():
    conn = get_conn()
    phone = input("Enter phone to search: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# Удалить с помошью имени или номеру
def delete_user():
    choice = input("Delete by (1) name or (2) phone? ")
    conn = get_conn()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    else:
        print("Invalid choice")
        return

    conn.commit()
    cur.close()
    conn.close()
    print("User deleted.")

def view_all_users():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall() 
    if rows:
        print("\nAll Contacts:")
        for i in rows:
            print(i)
    else:
        print("PhoneBook is empty.")
    cur.close()
    conn.close()






def main():
    create_table()
    while True:
        print("PhoneBook Menu")
        print("1. Insert from CSV")
        print("2. Insert from Console")
        print("3. Update User")
        print("4. Search by Name")
        print("5. Search by Phone")
        print("6. Delete User")
        print("7. View All Users")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("C:/pylabs/lab10/text.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            search_by_phone()
        elif choice == "6":
            delete_user()
        elif choice == "7":
            view_all_users()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__": # запускаем основную программу
    main()
