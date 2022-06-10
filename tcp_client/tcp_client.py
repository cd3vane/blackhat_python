import socket

target_host = "google.com"
target_port = 80

# Create a socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect client to target
client.connect((target_host, target_port))

# Send data
client.send(b"GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n")

# Receive data
response = client.recv(4096)

print(response)
