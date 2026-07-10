from flask import Flask, request

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    temperature = request.form['temperature']
    intensity = request.form['intensity']

    with open("temperature.txt", "a") as f:
        f.write(temperature + "\n")

    with open("intensity.txt", "a") as f:
        f.write(intensity + "\n")

    return "Data Stored Successfully"

@app.route('/temperature')
def temperature():
    with open("temperature.txt", "r") as f:
        data = f.read()
    return data

@app.route('/intensity')
def intensity():
    with open("intensity.txt", "r") as f:
        data = f.read()
    return data

if __name__ == '__main__':
    app.run(debug=True)
