import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)

cur = con.cursor()

while True:
    print("\n----- SENSOR READINGS CRUD -----")
    print("1. Insert Record")
    print("2. Display All Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Display Records Below Threshold")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        temp = float(input("Enter Temperature: "))
        hum = float(input("Enter Humidity: "))

        query = """
        INSERT INTO sensor_readings
        (temperature, humidity)
        VALUES (%s, %s)
        """

        cur.execute(query, (temp, hum))
        con.commit()

        print("Record Inserted Successfully")

    elif choice == 2:
        cur.execute("SELECT * FROM sensor_readings")

        rows = cur.fetchall()

        print("\nID\tTemp\tHumidity\tTimestamp")
        for row in rows:
            print(row)

    elif choice == 3:
        rid = int(input("Enter ID to Update: "))
        temp = float(input("Enter New Temperature: "))
        hum = float(input("Enter New Humidity: "))

        query = """
        UPDATE sensor_readings
        SET temperature=%s, humidity=%s
        WHERE id=%s
        """

        cur.execute(query, (temp, hum, rid))
        con.commit()

        print("Record Updated Successfully")

    elif choice == 4:
        rid = int(input("Enter ID to Delete: "))

        query = "DELETE FROM sensor_readings WHERE id=%s"

        cur.execute(query, (rid,))
        con.commit()

        print("Record Deleted Successfully")

    elif choice == 5:
        threshold = float(input("Enter Threshold Temperature: "))

        query = """
        SELECT * FROM sensor_readings
        WHERE temperature < %s
        """

        cur.execute(query, (threshold,))

        rows = cur.fetchall()

        print("\nRecords Below Threshold:")
        for row in rows:
            print(row)

    elif choice == 6:
        print("Program Exited")
        break

    else:
        print("Invalid Choice")

con.close()
