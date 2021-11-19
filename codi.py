import serial
import pynmea2
count = 0
port = 'COM7'
ser = serial.Serial(port, 9600, timeout=0)
ln = ''
while 1:
    count += 1
    s = ser.read()
    sr = ser.readline().decode('ascii', errors='replace')
    # print(sr.strip())

    if str(s)[2] != "'":
        if 'GNGLL' in str(sr.strip()):
            nmea = sr.strip()
            nmeaobj = pynmea2.parse(nmea)
            lat = nmeaobj.latitude
            lon = nmeaobj.longitude
            print('lat:', lat, 'lon:', lon)