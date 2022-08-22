import mysql.connector

mybd = mysql.connector.connect(
  host="localhost",
  user = input("Introduce tu usuario"),
  passwd = input("Introduce la contrasena")
)

mycursor = mybd.cursor()

mycursor.execute("CREATE DATABASE Banquito")

mycursor.close()

