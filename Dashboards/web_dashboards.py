from flask import Flask, jsonify
from modbus.modbus_reader import read_battery_data

app = Flask(__name__)

@app.route("/data")

def get_data():

    data = read_battery_data()

    return jsonify(data)


@app.route("/")

def home():

    return "BHMS Battery Monitoring System Running"


if __name__ == "__main__":

    app.run(host="0.0.0.0",port=5000)
