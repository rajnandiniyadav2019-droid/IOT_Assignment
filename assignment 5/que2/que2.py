from flask import Flask, request
import mysql.connector
import paho.mqtt.publish as publish

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="fitness"
)

TOPIC = "health/status"

# 1. Add User
@app.route('/add', methods=['POST'])
def add():

    try:
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        steps = request.form['steps']
        pulse = request.form['pulse']
        oxygen = request.form['oxygen']
        temperature = request.form['temperature']

        cur = conn.cursor()

        query = """
        INSERT INTO users
        (name,age,city,steps,pulse,oxygen,temperature)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """

        cur.execute(query,
        (name,age,city,steps,pulse,oxygen,temperature))

        conn.commit()

        publish.single(TOPIC,
                       "/add SUCCESS",
                       hostname="localhost")

        return "User Added"

    except:
        publish.single(TOPIC,
                       "/add FAILURE",
                       hostname="localhost")
        return "Error"


# 2. All Users
@app.route('/all')
def all_users():

    try:
        cur = conn.cursor()

        cur.execute("SELECT * FROM users")

        data = cur.fetchall()

        publish.single(TOPIC,
                       "/all SUCCESS",
                       hostname="localhost")

        return str(data)

    except:
        publish.single(TOPIC,
                       "/all FAILURE",
                       hostname="localhost")
        return "Error"


# 3. Single User
@app.route('/info')
def info():

    try:
        name = request.args.get("name")

        cur = conn.cursor()

        query = "SELECT * FROM users WHERE name=%s"

        cur.execute(query,(name,))

        data = cur.fetchone()

        publish.single(TOPIC,
                       "/info SUCCESS",
                       hostname="localhost")

        return str(data)

    except:
        publish.single(TOPIC,
                       "/info FAILURE",
                       hostname="localhost")
        return "Error"


# 4. Update City
@app.route('/update')
def update():

    try:
        name = request.args.get("name")
        city = request.args.get("city")

        cur = conn.cursor()

        query = """
        UPDATE users
        SET city=%s
        WHERE name=%s
        """

        cur.execute(query,(city,name))

        conn.commit()

        publish.single(TOPIC,
                       "/update SUCCESS",
                       hostname="localhost")

        return "City Updated"

    except:
        publish.single(TOPIC,
                       "/update FAILURE",
                       hostname="localhost")
        return "Error"


# 5. Maximum Steps
@app.route('/steps')
def max_steps():

    try:
        cur = conn.cursor()

        query = """
        SELECT *
        FROM users
        ORDER BY steps DESC
        LIMIT 1
        """

        cur.execute(query)

        data = cur.fetchone()

        publish.single(TOPIC,
                       "/steps SUCCESS",
                       hostname="localhost")

        return str(data)

    except:
        publish.single(TOPIC,
                       "/steps FAILURE",
                       hostname="localhost")
        return "Error"


if __name__ == '__main__':
    app.run(debug=True)
