import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

mycursor = mydb.cursor()

# Create database
sql = "CREATE DATABASE IF NOT EXISTS SHOP"
try:
    mycursor.execute(sql)
except:
    print("error")

# Connect to the SHOP database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="SHOP"
)

mycursor = mydb.cursor()

# Create Category table
sql = """
        CREATE TABLE IF NOT EXISTS Category (
            c_id INT AUTO_INCREMENT,
            c_name VARCHAR(250),
            PRIMARY KEY(c_id)
        );
    """
mycursor.execute(sql)

# Create Products table with a foreign key reference to Category
sql = """
        CREATE TABLE IF NOT EXISTS Products (
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
sql = "INSERT INTO Category (c_name) VALUES ('Home Appliances')"
mycursor.execute(sql)
mydb.commit()

# Insert data into Products table with a different product
sql = "INSERT INTO Products (p_name, c_id, price, quantity) VALUES ('Refrigerator', 1, 1200, 50)"
mycursor.execute(sql)
mydb.commit()

# Delete data from Products table
sql = "DELETE FROM Products WHERE p_name = 'Refrigerator'"
mycursor.execute(sql)
mydb.commit()

# Select all data from Products table
sql = "SELECT * FROM Products"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

# Update Products table
sql = "UPDATE Products SET price = 0.3 * price "
mycursor.execute(sql)
mydb.commit()

# Select data from Products table where p_name is 'Refrigerator'
sql = "SELECT * FROM Products WHERE p_name = 'Refrigerator'"
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
