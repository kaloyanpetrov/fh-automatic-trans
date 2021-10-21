import socket

# receives the data package from Forza Horizon 4
UDP_IP = "10.10.10.193"
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print('received data: ' + str(data))
