import csv
from datetime import datetime
from config.settings import LOG_FILE

def save_data(data):

    timestamp = datetime.now()

    row = [timestamp]

    row.extend(data["cells"])
    row.extend(data["bank_voltage"])
    row.extend(data["current"])
    row.extend(data["temps"])

    with open(LOG_FILE,"a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print("Data Saved")
