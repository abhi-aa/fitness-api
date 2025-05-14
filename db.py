import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password_here",  # Replace this with the password you set
    database="fitness"              # Make sure you've created this DB
)

cursor = conn.cursor()
