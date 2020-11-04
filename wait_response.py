import speedtest
import time
import csv
from datetime import datetime

st = speedtest.Speedtest()

def to_mb(bytes):
    return bytes/1000000

def get_speed():
    download_b = st.download()
    down_mb = to_mb(download_b)
    print("down in MB" + str(down_mb))

    upload_b = st.upload()

    up_mb = to_mb(upload_b)

    print("up in MB" + str(up_mb))

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

for i in range(10):
    time.sleep(in_minutes(1))
    write_speed()

