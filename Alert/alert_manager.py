from config.settings import MAX_CELL_VOLTAGE, MIN_CELL_VOLTAGE, MAX_TEMPERATURE


def check_alerts(data):

    cells = data["cells"]
    temps = data["temps"]

    for i,v in enumerate(cells):

        if v > MAX_CELL_VOLTAGE:
            print(f"ALERT : Cell {i+1} Over Voltage")

        if v < MIN_CELL_VOLTAGE:
            print(f"ALERT : Cell {i+1} Under Voltage")

    for i,t in enumerate(temps):

        if t > MAX_TEMPERATURE:
            print(f"ALERT : Temperature Sensor {i+1} High")
