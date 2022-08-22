import mysql.connector

mybd = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Banquito"
)

mycursor = mybd.cursor()

#mycursor.execute('DROP DATABASE Banco')

'''
# Creacion de tablas
mycursor.execute("CREATE TABLE Cliente (id_cli INT AUTO_INCREMENT PRIMARY KEY, nom_cli VARCHAR(250) not null, cedula_cli VARCHAR(12) not null, tel_cli VARCHAR(10) not null, edad_cli VARCHAR(3)not null, direc_cli VARCHAR(250), trabajo_cli VARCHAR(2), yearWork_cli VARCHAR(5))")

mycursor.execute('CREATE TABLE Prestamos(id_pres INT AUTO_INCREMENT PRIMARY KEY, id_cli INT not null, monto_pres VARCHAR(12) not null, tasainteres_pres INT not null, numcuotas_pres VARCHAR(3) not null, fechainicial_pres VARCHAR(12) not null, montopagado VARCHAR(15), fechafinal_pres VARCHAR(12))')


mycursor.execute('CREATE TABLE TarjetasCredito(id_tar INT AUTO_INCREMENT PRIMARY KEY, id_cli INT not null, nom_tar VARCHAR(20) not null, marcainternacional_tar VARCHAR(10), fechaexpedicion_tar VARCHAR(4) not null, digitos_tar VARCHAR(15) not null, cvv_tar VARCHAR(3) not null, fecha_vencimiento VARCHAR(4) not null)')

#mycursor.execute('ALTER TABLE Prestamos ADD COLUMN montopagado VARCHAR(15)')

mycursor.execute('CREATE TABLE Cuenta(id_cuenta INT AUTO_INCREMENT PRIMARY KEY, id_cli INT not null, estado_cuenta VARCHAR(10), oficial_cuenta VARCHAR(50), sucursal VARCHAR(50), balanceactual_cuenta VARCHAR(20), balancedisponible_cuenta VARCHAR(20))')

mycursor.execute('CREATE TABLE Movimientos(id_movi INT AUTO_INCREMENT PRIMARY KEY, id_cli INT not null, id_cuenta INT, monto_movi VARCHAR(10), descrip_movi VARCHAR(255), fecha_movi VARCHAR(12))')


mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)

#foreign keys
mycursor.execute("ALTER TABLE Prestamos ADD FOREIGN KEY (id_cli) REFERENCES Cliente(id_cli)")
mycursor.execute("ALTER TABLE TarjetasCredito ADD FOREIGN KEY (id_cli) REFERENCES Cliente(id_cli)")
mycursor.execute("ALTER TABLE Movimientos ADD FOREIGN KEY (id_cli) REFERENCES Cliente(id_cli)")
mycursor.execute("ALTER TABLE Cuenta ADD FOREIGN KEY (id_cli) REFERENCES Cliente(id_cli)")
mycursor.execute("ALTER TABLE Movimientos ADD FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)")

#insert tabla Cliente

sql='INSERT INTO Cliente (nom_cli, cedula_cli, tel_cli, edad_cli, direc_cli, trabajo_cli, yearWork_cli) VALUES (%s, %s, %s, %s, %s, %s, %s)'
var=[
    ('Clarissa Perez', '0014554543-2','8295645532','46', 'Ens. Las Rosas c/24','Asociacion Invenca', '8'),
    ('Carmen Martinez', '001456544-2','8295222232','40','Ens. Villa Rosita c/2','Supermercado Bravo', '2'),
    ('Ana Gonzalez', '4028555292-3','8095633221', '26','Ens. Violeta Calle Las Rosas','', ''),
    ('Brayan Montez', '0010806852-9','8295645532','43','Calle Los Proceres','UNPHU', '4'),
    ('Miguel Derne', '0012478542-5','8295645532','52','Piantini', 'UNIBE', '3')
]

mycursor.executemany(sql, var)

mybd.commit()
print(mycursor.rowcount, "ha sido insertado.")


#seleccionando tablas
mycursor.execute('SELECT * FROM Cliente')

myresult = mycursor.fetchall()

for x in myresult:
 print(x)

# mycursor.execute('ALTER TABLE Movimiento ALTER COLUMN fecha_movi VARCHAR(10)')

# insert Cuenta
hi='INSERT INTO Cuenta (id_cli, estado_cuenta, oficial_cuenta, sucursal, balanceactual_cuenta, balancedisponible_cuenta) VALUES (%s, %s, %s, %s, %s,%s)'
varia=[
    ('1', 'Activa','Francisca Mendoza','CORAL MALL','22000', '21500'),
    ('2', 'Inactiva','Francisca Mendoza','CORAL MALL','500', '0'),
    ('3', 'Activa','Pablo Castillo','MEGA CENTRO','10000', '9500'),
    ('4', 'Activa','Jose Cardenas','CORAL MALL','22000', '21500'),
    ('5', 'Activa','Melissa Topas','DOWNTOWN CENTER','1856520', '1000000'),
]

mycursor.executemany(hi, varia)

mybd.commit()
print(mycursor.rowcount, "ha sido insertado.")

#insert Movimientos

hey='INSERT INTO Movimientos (id_cli, id_cuenta, monto_movi, descrip_movi, fecha_movi) VALUES (%s, %s, %s, %s, %s)'
vari=[
    ('1', '1','2500','Deposito entrante', '2022-8-12'),
    ('3', '3','2500','Retiro en Efectivo', '2022-5-9')
]

mycursor.executemany(hey, vari)

mybd.commit()
print(mycursor.rowcount, "ha sido insertado.")




s = "INSERT INTO prestamos (id_cli, monto_pres, tasainteres_pres, numcuotas_pres, fechainicial_pres) VALUES (%s, %s, %s, %s, %s)"
va = [
  ('1', '39,800', '12.5', '12', '2020-5-20'),
  ('2', '348,938', '12.5', '5', '2017-5-19'),
  ('3', '43,783', '12.5%', '10', '1980-2-8'),
  ('4', '3,563', '12.5%', '4', '2005-6-17'),
  ('5', '67,814', '12.5%', '7', '2000-9-15'),
]

mycursor.executemany(s, va)

mybd.commit()
print(mycursor.rowcount, "was inserted.")

'''

#mycursor.execute('TRUNCATE Cuenta')
#mycursor.execute('TRUNCATE Movimientos')
#mycursor.execute('TRUNCATE Prestamos')
#mycursor.execute('TRUNCATE TarjetasCredito')

#mycursor.execute('TRUNCATE Cliente')

#seleccionando tablas

'''
mycursor.execute("CREATE TABLE Pagos (id_pago INT AUTO_INCREMENT PRIMARY KEY, id_cli INT not null, id_pres INT not null, monto_pago VARCHAR (20), fecha_pago VARCHAR (20))")

'''
s = "INSERT INTO Pagos (id_cli, id_pres, monto_pago, fecha_pago) VALUES (%s, %s, %s, %s)"
va = [
  ('3', '3', '15000', '1982-3-8'),
  ('4', '4', '250', '2005-8-8'),
  ('5','5','11050','2002-5-8')
]

mycursor.executemany(s, va)

mybd.commit()
print(mycursor.rowcount, "was inserted.")


mycursor.execute('SELECT * FROM Cliente')
myresult = mycursor.fetchall()

for x in myresult:
 print(x)

print('\n')


mycursor.execute('SELECT * FROM Cliente')
myresult = mycursor.fetchall()

for x in myresult:
 print(x)


mycursor.execute('SELECT * FROM Cuenta')
myresult = mycursor.fetchall()

for x in myresult:
 print(x)


mycursor.execute('SELECT * FROM Movimientos')
myresult = mycursor.fetchall()

for x in myresult:
 print(x)

mycursor.execute('SELECT * FROM Prestamos')
myresult = mycursor.fetchall()

for x in myresult:
 print(x)

#mycursor.execute('SELECT * FROM TarjetaCredito')


#mycursor.execute('ALTER TABLE Cliente ADD COLUMN salario_cli VARCHAR(12)')


#mycursor.execute('CREATE TABLE Historial (id_h INT AUTOINCREMENT )')