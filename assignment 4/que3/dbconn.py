import paho.mqtt.publish as publish

publish.single(
    "sensor/lm35",
    "30",
    hostname="localhost"
)

publish.single(
    "sensor/ldr",
    "450",
    hostname="localhost"
)
