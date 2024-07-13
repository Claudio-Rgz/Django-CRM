import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '.Imapenguin9',
)

# Cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE segurosvillanueva")

print("DataBase set up correctly.")