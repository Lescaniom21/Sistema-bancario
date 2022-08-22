import mysql.connector

mi_conexion = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	# database = ""
    
    )
	

if mi_conexion.is_connected():
	print("Conexión establecida correctamente.")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("SHOW DATABASES")

for bd in mi_cursor:
	print(bd)

mi_cursor.close()

mi_conexion.close()

if not mi_conexion.is_connected():
	print("Conexión finalizada correctamente.")