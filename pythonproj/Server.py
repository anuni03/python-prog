import socket
from threading import Thread

host='localhost'
client={} #to store all clients connected in the chat room
address={}
port=8080
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))
def broadcast(msg,prefix=""):
    for x in client:
        x.send(bytes(prefix,"utf8")+msg)



def handle_client(conn,address):
    name=conn.recv(1024).decode()
    welcome="Welcome "+name+".You can type #quit if you want to leave the chat room"
    conn.send(bytes(welcome,"utf8"))
    msg=name+" has recently joined the Chat Room."
    broadcast(bytes(msg,"utf8"))
    client[conn]=name
    while True:
        msg=conn.recv(1024)
        if msg!=bytes("#quit","utf8"):
            broadcast(msg,name+":")
        else:
            conn.send(bytes("#quit","utf8"))
            conn.close()
            del client[conn]
            broadcast(bytes(name+" has left the Chat Room","utf8"))

def accept_client_conections():
     while True:
        client_conn,client_address=sock.accept()
        print(client_address,"Has connected")
        client_conn.send("Welcome to the chat room,Please type your name to continue".encode('utf8'))
        address[client_conn]=client_address
        Thread(target=handle_client,args=(client_conn,client_address)).start()

if __name__=="__main__":  #first thing to execute
    sock.listen(5)  #shows that server can listen to maximum 5 request at a time
    print("The server is running and listening to clients request")



    t1=Thread(target=accept_client_conections) #execute two task at the same time
    t1.start()
    t1.join()   #to connect multiple client one after the other 