import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="777",
    database="PizzaRestoran"
)
cursor = connection.cursor()

def show_menu():
    cursor.execute("SELECT * FROM Menu")
    results = cursor.fetchall()
    print("\n--- Menu ---")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Cost: {row[2]} AZN, Category: {row[3]}")

def show_customers():
    cursor.execute("SELECT * FROM Customers")
    results = cursor.fetchall()
    print("\n--- Customers ---")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")

def show_orders():
    cursor.execute("""
        SELECT Orders.id, Customers.name, Orders.datee, Orders.total_price
        FROM Orders
        JOIN Customers ON Orders.customer_id = Customers.id
    """)
    results = cursor.fetchall()
    print("\n--- Orders ---")
    for row in results:
        print(f"ID: {row[0]}, Orders: {row[1]}, Datee: {row[2]}, Total_price: {row[3]} AZN")

def show_order_details(order_id):
    cursor.execute("""
        SELECT Order_details.id, Menu.name, Order_details.quantity
        FROM Order_details
        JOIN Menu ON Order_details.menu_id = Menu.id
        WHERE Order_details.order_id = %s
    """, (order_id,))
    results = cursor.fetchall()
    print(f"\n--- Order Details (Order ID: {order_id}) ---")
    if results:
        for row in results:
            print(f"ID: {row[0]}, Dish: {row[1]}, Quantity: {row[2]}")
    else:
        print("Bu sifariş üçün detallar tapılmadı.")

def add_customer(name, phone, email):
    cursor.execute("INSERT INTO Customers (ad, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    connection.commit()
    print(f"\nMüştəri əlavə edildi: {name}")

def add_order(customer_id, datee, total_price):
    cursor.execute("INSERT INTO Orders (customer_id, datee, total_price) VALUES (%s, %s, %s)", (customer_id, datee, total_price))
    connection.commit()
    print(f"\nYeni sifariş əlavə edildi: Customer ID {customer_id}, Date {datee}, Total price {total_price} AZN")


def show_category_items(category):
    cursor.execute("SELECT * FROM Menu WHERE Category = %s", (category))
    results = cursor.fetchall()
    print(f"\n--- {category} Category ---")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Cost: {row[2]} AZN")
def main():
    while True:
        print("\n--- Pizza Restoran Sorğuları ---")
        print("1. Menyunu göstər")
        print("2. Müştəriləri göstər")
        print("3. Sifarişləri göstər")
        print("4. Sifariş detalları göstər")
        print("5. Yeni müştəri əlavə et")
        print("6. Yeni sifariş əlavə et")
        print("7. Kateqoriyaya görə menyunu göstər")
        print("0. Çıxış")

        choice = input("\nSeçiminizi daxil edin: ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            show_customers()
        elif choice == "3":
            show_orders()
        elif choice == "4":
            order_id = int(input("Sifariş ID-ni daxil edin: "))
            show_order_details(order_id)
        elif choice == "5":
            name = input("Müştərinin adını daxil edin: ")
            phone = input("Telefon nömrəsini daxil edin: ")
            email = input("Email ünvanını daxil edin: ")
            add_customer(name, phone, email)
        elif choice == "6":
            customer_id = int(input("Müştəri ID-ni daxil edin: "))
            datee = input("Sifariş tarixi (YYYY-MM-DD): ")
            total_price = float(input("Ümumi qiymət: "))
            add_order(customer_id, datee, total_price)
        elif choice == "7":
            category = input("Kateqoriyanı daxil edin (məsələn, 'Pizza', 'İçki', 'Yan yemək'): ")
            show_category_items(category)
        elif choice == "0":
            print("Çıxılır...")
            break
        else:
            print("Yanlış seçim. Yenidən cəhd edin.")

if __name__ == "__main__":
    main()
cursor.close()
connection.close()