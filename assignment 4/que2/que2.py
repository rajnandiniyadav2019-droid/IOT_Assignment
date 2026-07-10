from flask import Flask, request
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smarthome"
)

@app.route('/update', methods=['POST'])
def update():

    light = request.form['light']
    fan = request.form['fan']
    temp = request.form['temperature']

    cur = conn.cursor()

    query = """
    INSERT INTO smarthome(light_status,fan_status,temperature)
    VALUES(%s,%s,%s)
    """

    cur.execute(query, (light, fan, temp))
    conn.commit()

    return "Data Added Successfully"

@app.route('/status')
def status():

    cur = conn.cursor()

    query = """
    SELECT light_status,fan_status,temperature
    FROM smarthome
    ORDER BY id DESC
    LIMIT 1
    """

    cur.execute(query)
    row = cur.fetchone()

    return f"""
    Light : {row[0]} <br>
    Fan : {row[1]} <br>
    Temperature : {row[2]} °C
    """

if __name__ == '__main__':
    app.run(debug=True)
