import time

time1 = int(input("Enter the time in second: "))

for i in range(time1,0,-1):
    second = i % 60
    minutes = int(i / 60) %60
    hour = int(i / 3600) % 24
    day = int(i/86400) % 30
    month = int(i/2592000) % 12
    year = int(i/2592000) %10000
    time.sleep(0.001)
    print(f"{year:02}:{month:02}:{day:02}:{hour:02}:{minutes:02}:{second:02}")
