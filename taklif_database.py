import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
mycursor = mydb.cursor()

# Create the SHOP database
sql = "CREATE DATABASE IF NOT EXISTS SHOP"
mycursor.execute(sql)

# Connect to the SHOP database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="SHOP"
)
mycursor = mydb.cursor()

# Create the Category table
sql = """
        CREATE TABLE IF NOT EXISTS Category(
            c_id INT AUTO_INCREMENT,
            c_name VARCHAR(250),
            PRIMARY KEY(c_id)
        );
    """
mycursor.execute(sql)

# Create the Products table
sql = """
        CREATE TABLE IF NOT EXISTS Products(
            p_id INT AUTO_INCREMENT,
            p_name VARCHAR(250),
            price INT,
            quantity INT,
            c_id INT,
            PRIMARY KEY(p_id),
            FOREIGN KEY(c_id) REFERENCES Category(c_id)
        );
    """
mycursor.execute(sql)

# Insert data into Category table
sql = "INSERT INTO Category(c_name) VALUES ('Electronics')"
mycursor.execute(sql)
mydb.commit()

# Insert data into Products table
sql = "INSERT INTO Products(p_name, price, quantity, c_id) VALUES ('Laptop', 1000, 100, 1)"
mycursor.execute(sql)
mydb.commit()

# Delete data from Products table
sql = "DELETE FROM Products WHERE p_name = 'Laptop'"
mycursor.execute(sql)
mydb.commit()

# Delete data from Category table
sql = "DELETE FROM Category WHERE c_id = 1"
mycursor.execute(sql)
mydb.commit()

# Select all data from Products table
sql = "SELECT * FROM Products"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

# Update the price of Products
sql = "UPDATE Products SET price = 0.3 * price + price"
mycursor.execute(sql)
mydb.commit()

# Select data from Products table where name is 'Laptop'
sql = "SELECT * FROM Products WHERE p_name = 'Laptop'"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

# Select p_name from Products table
sql = "SELECT p_name FROM Products"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

# Select c_name from Category table
sql = "SELECT c_name FROM Category"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)
