import speedtest
import time
import csv
from datetime import datetime

st = speedtest.Speedtest()

def to_mb(bytes):
    return round(bytes / (10 ** 6), 2)

def get_speed():

    download_b = st.download()
    down_mb = to_mb(download_b)
    upload_b = st.upload()
    up_mb = to_mb(upload_b)
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    print("up in MB : " + str(up_mb) + " --  down in MB : " + str(down_mb) + " date : " + date )

    return up_mb, down_mb

def write_speed():
    with open('internet.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        speed = get_speed()
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")

        employee_writer.writerow([speed[0], speed[1], date])

def in_minutes(minutes):
    return minutes * 60

for i in range(1000):
    time.sleep(in_minutes(0.2))
    write_speed()

