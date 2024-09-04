import socket

port = 5060
data = 16
format = "utf-8"
disconnected_msg = "End"
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)

server_socket_address = (host_addr, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)

def msg_send(msg):
   message = msg.encode(format)
   msg_length = len(message)
   msg_length = str(msg_length).encode(format)
   msg_length += b" "* (data - len(msg_length))

   client.send(msg_length)
   client.send(message)

   print(client.recv(2048).decode(format))

msg_send(f"IP address of the client is {host_addr} amd the device name is {hostname}")
msg_send(disconnected_msg)
