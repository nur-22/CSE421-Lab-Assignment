import socket
import threading
port = 5060
data = 16
format = "utf-8"
disconnected_msg = "End"
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)

server_socket_address = (host_addr, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)

def calculate_salary(msg):
    if msg <= 40:
        salary = msg * 200
    else:
        base_salary = 8000
        extra_hours = msg - 40
        salary = base_salary + (extra_hours * 300)
    return salary

def handler(conn, addr):
   print("Connected to ",addr)
   connected = True

   while connected:
       initial = conn.recv(data).decode(format)
       print("Length of the message to be sent ", initial)
       if initial:
           msg_length = int(initial)
           msg = conn.recv(msg_length).decode(format)
           msg = int(msg)
           if msg == disconnected_msg:
                print("Terminating connection with ", addr)
                conn.send("Nice to meet you {addr}".encode(format))
                connected = False
           else:
                salary = calculate_salary(msg)
                conn.send(f"The salary is Tk {salary}".encode(format))


   conn.close()

def start():
   print("Server is starting")

   server.listen()
   print("Server is listening on", host_addr)

   while True:
       conn, addr = server.accept()
       print("Connected to", addr)

       thread =threading.Thread(target= handler, args= (conn, addr))
       thread.start()

start()

