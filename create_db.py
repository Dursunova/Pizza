import mysql.connector

connection = mysql.connector.connect(
    host="localhost", 
    user="root",       
    password="777"  
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS PizzaRestoran")
cursor.execute("USE PizzaRestoran")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    category VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    datee DATE,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Order_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    menu_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (menu_id) REFERENCES Menu(id)
)
""")


menu_items = [
    ('Classic Cheese Pizza', 7.99, 'Pizza'),
    ('Spicy Pepperoni Pizza', 9.99, 'Pizza'),
    ('Fresh Lemonade', 2.49, 'Drink'),
    ('Iced Tea', 1.99, 'Drink'),
    ('BBQ Chicken Pizza', 11.49, 'Pizza'),
    ('Mediterranean Veggie Pizza', 8.99, 'Pizza'),
    ('Herb Garlic Bread', 2.99, 'Side'),
    ('Mozzarella Sticks', 5.49, 'Side'),
    ('Tiramisu', 6.49, 'Dessert'),
    ('Vanilla Sundae', 3.99, 'Dessert'),
    ('Mineral Water', 1.29, 'Drink'),
    ('Sweet Potato Fries', 4.29, 'Side'),
    ('Honey BBQ Wings', 8.49, 'Side'),
    ('Tropical Hawaiian Pizza', 10.99, 'Pizza'),
    ('Grilled Chicken Sandwich', 7.49, 'Burger')
]

cursor.executemany("INSERT INTO Menu (name, cost, category) VALUES (%s, %s, %s)", menu_items)

customers = [
    ('Alice Smith', '555-123-4567', 'alice@example.com'),
    ('John Doe', '555-765-4321', 'john@example.com'),
    ('Emily Johnson', '555-987-6543', 'emily@example.com'),
    ('Michael Brown', '555-456-7890', 'michael@example.com'),
    ('Sophia Davis', '555-234-5678', 'sophia@example.com'),
    ('Daniel Wilson', '555-765-4321', 'daniel@example.com'),
    ('Olivia Martinez', '555-112-2334', 'olivia@example.com'),
    ('James Taylor', '555-998-8776', 'james@example.com'),
    ('Emma Anderson', '555-665-5443', 'emma@example.com'),
    ('Benjamin Moore', '555-443-3221', 'benjamin@example.com')
]


cursor.executemany("INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s)", customers)


orders = [
    (101, '2024-12-01', 21.45),
    (102, '2024-12-02', 14.99),
    (103, '2024-12-03', 27.89),
    (104, '2024-12-04', 11.49),
    (105, '2024-12-05', 17.79),
    (106, '2024-12-06', 22.39),
    (107, '2024-12-07', 32.50),
    (108, '2024-12-08', 19.75),
    (109, '2024-12-09', 10.49),
    (110, '2024-12-10', 15.99)
]


cursor.executemany("INSERT INTO orders (customer_id, datee, total_price) VALUES (%s, %s, %s)", orders)


order_details = [
    (1, 1, 2),
    (1, 3, 1),
    (2, 2, 1),
    (2, 5, 1),
    (3, 4, 2),
    (3, 6, 1),
    (4, 7, 3),
    (5, 8, 2),
    (6, 9, 1),
    (7, 10, 2),
    (8, 11, 5),
    (9, 12, 3),
    (10, 13, 4)
]

cursor.executemany("INSERT INTO order_details (order_id, menu_id, quantity) VALUES (%s, %s, %s)", order_details)

connection.commit()

print("Bütün məlumatlar uğurla əlavə edildi!")