import paho.mqtt.client as mqtt
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smarthome"
)

def on_message(client, userdata, msg):

    sensor = msg.topic
    value = msg.payload.decode()

    cur = conn.cursor()

    query = """
    INSERT INTO sensor_data(sensor,value)
    VALUES(%s,%s)
    """

    cur.execute(query, (sensor, value))
    conn.commit()

    print(sensor, value)

client = mqtt.Client()

client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("sensor/lm35")
client.subscribe("sensor/ldr")

client.loop_forever()
