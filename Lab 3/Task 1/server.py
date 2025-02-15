import socket

port = 5060
data = 16
format = "utf-8"
disconnected_msg = "End"
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)

server_socket_address = (host_addr, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)

server.listen()
print("Our server is listening")

while True:
   conn, addr = server.accept()
   print("Connected to ",addr)
   connected = True
   while connected:
       initial = conn.recv(data).decode(format)
       print("Length of the message to be sent ", initial)
       if initial:
           msg_length = int(initial)
           msg = conn.recv(msg_length).decode(format)
           if msg == disconnected_msg:
               print("Terminating connection with ", addr)
               conn.send("Nice to meet you {addr}".encode(format))
               connected = False
           else:
               print(msg)
               conn.send("Received your message". encode(format))

   conn.close()
