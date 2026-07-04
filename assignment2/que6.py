import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)

cur = con.cursor()

threshold = 24

query = "SELECT * FROM sensor_readings WHERE temperature < %s"
cur.execute(query, (threshold,))

for row in cur.fetchall():
    print(row)

con.close()
