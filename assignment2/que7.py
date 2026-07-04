import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture"
)

cur = con.cursor()

threshold = 35

query = "SELECT * FROM soil_moisture WHERE moisture_level < %s"
cur.execute(query, (threshold,))

for row in cur.fetchall():
    print(row)

con.close()
