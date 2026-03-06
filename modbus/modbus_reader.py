from pymodbus.client import ModbusTcpClient
from config.settings import BHMS_IP, MODBUS_PORT

client = ModbusTcpClient(BHMS_IP, port=MODBUS_PORT)

def read_registers(start, count):

    if not client.connect():
        print("Connection Failed")
        return None

    result = client.read_holding_registers(start, count)

    if result.isError():
        print("Modbus Error")
        return None

    return result.registers


def read_battery_data():

    cell_voltages = read_registers(0,15)
    bank_voltage = read_registers(20,1)
    current = read_registers(30,1)
    temperatures = read_registers(40,15)

    data = {
        "cells":cell_voltages,
        "bank_voltage":bank_voltage,
        "current":current,
        "temps":temperatures
    }

    return data


if __name__ == "__main__":

    data = read_battery_data()
    print(data)
