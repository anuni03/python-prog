import tkinter
import socket
from tkinter import *
from threading import Thread
def receive():
    while True:
        try:
            msg=sock.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END,msg)
        except:
            print("There is an Error Receiving the message")
def send():  #when client presses send button
    msg=my_msg.get()
    my_msg.set("")  #empty the space so that client can enter other message
    sock.send(bytes(msg,"utf8")) #send the message to all other clients
    if msg=="#quit":
        sock.close()
        window.close()


def on_closing():
    my_msg.set("#quit")
    send()


window=Tk()
window.title("Chat Room Application")
window.configure(bg="blue")


message_frame=Frame(window,height=100,width=100,bg='pink')
message_frame.pack()

my_msg=StringVar()
my_msg.set("")

scr=Scrollbar(message_frame)
msg_list=Listbox(message_frame,height=15,width=100,bg='red',yscrollcommand=scr.set)
scr.pack(side=RIGHT,fill=Y)
msg_list.pack(side=LEFT,fill=BOTH)
msg_list.pack()
label=Label(window,text="Enter the message",fg="blue",font="Aerial",bg="pink")
label.pack()
entry_field=Entry(window,textvariable=my_msg,fg="red",width=50)
entry_field.pack()
send_button=Button(window,text="Send",font="Aerial",fg="white",command=send)
send_button.pack()
quit_button=Button(window,text="Quit",font="Aerial",fg="White",command=on_closing)
quit_button.pack()


Host='localhost'
port=8080
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((Host,port))
receive_thread=Thread(target=receive)
receive_thread.start()



mainloop()