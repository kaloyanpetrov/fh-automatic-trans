from fdp import FHDataPacket
import struct
import datetime as dt
import socket
import threading
import yaml


# receives the data package from FH4
UDP_IP = "10.10.10.193"
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


while True:
    data, address = sock.recvfrom(1024)
    # initializes the data to the FHDataPacket
    try:
        fdp = FHDataPacket(data)
    except struct.error as e:
        continue
    # creates real-time clock
    fdp.wall_clock = dt.datetime.now()
    fdp.wall_clock = fdp.wall_clock.strftime("%H:%M:%S")
    print(fdp.wall_clock, end=': ')
    print(f"{fdp.current_engine_rpm:.1f} RPM")
