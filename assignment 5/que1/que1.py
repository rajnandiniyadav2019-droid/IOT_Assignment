import paho.mqtt.publish as publish
import random
import time

while True:

    temp = random.randint(25,35)
    intensity = random.randint(100,1000)

    publish.single(
        "sensor/lm35",
        temp,
        hostname="localhost"
    )

    publish.single(
        "sensor/ldr",
        intensity,
        hostname="localhost"
    )

    print("Temperature:", temp)
    print("Intensity:", intensity)

    time.sleep(5)
