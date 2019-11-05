import socket

HEADERSIZE=10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen()


while True:
    clientsocket, adress= s.accept()
    print(f"connection from {adress} has been established")
    
    msg = "welcome to the server"
    msg = f'{len(msg):<{HEADERSIZE}}'+ msg
    
    clientsocket.send(bytes("welcome to the server","utf-8"))
    clientsocket.close()
    
