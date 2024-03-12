import tkinter as tk
from tkinter import *
from CLIENT_RegistrationClient import *
import threading

root = tk.Tk()

# Fill out Client_Info
client_private_ip = "0.0.0.0"
client_listening_port = get_free_port()
client_nickname = "Aakash"

server_host = "127.0.0.1"
server_port = 9999

client_info = Client_Info(client_nickname, client_private_ip, client_listening_port)
client = RegistrationClient(server_host, server_port, client_info)

def register():
    response = client.register_with_server(client_info)

    if(response) == ResponseTypes.SUCCESS:
        end = "Succesfully registered " + client_nickname
    else:
        end = f"Nickname '{client_nickname}' already existing in server"

    answer = tk.Label(frame, text=end,anchor=NW, bg="#FFC0CB", font=("Helvetica", 11), width= 60, height=20,wraplength=500)
    answer.place(x=235,y=150)

def retrieve():
    response = client.request_client_info(client_nickname)

    client.listen_for_connections(client_listening_port)
    
    # listening_thread = threading.Thread(target=client.listen_for_connections(client_listening_port))
    # listening_thread.start()
    
    answer = tk.Label(frame, text=response,anchor=NW, bg="#FFC0CB", font=("Helvetica", 11), width= 60, height=20,wraplength=500)
    answer.place(x=235,y=150)


def retrieve_all():
    response = client.request_all_clients()
    
    answer = tk.Label(frame, text=response,anchor=NW, bg="#FFC0CB", font=("Helvetica", 11), width= 60, height=20,wraplength=500)
    answer.place(x=235,y=150)

def deregister():
    response = client.deregister_with_server(client_nickname)
    
    answer = tk.Label(frame, text=response,anchor=NW, bg="#FFC0CB", font=("Helvetica", 11), width= 60, height=20,wraplength=500)
    answer.place(x=235,y=150)



canvas = tk.Canvas(root, height=700, width=700, bg="#FFC0CB")
canvas.pack()

#Title of app
title = tk.Label(canvas, text="Netwok mapper", font=("Helvetica", 24), bg="#FFC0CB",fg="black" )
title.place(x=235, y= 20)

#Frame of whole app
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Entries
#Host IP adress entry
host_ip = tk.Label(frame, text="Host IP", font=("Helvetica", 14), bg="#FFFF00", width= 17,)
host_ip.place(x=10,y=20)
ipEntry = tk.Entry(frame,bg="#FFFF00",font=("Helvetica", 14), width=17,
                   textvariable=tk.StringVar(root, value="127.0.0.1"))
ipEntry.place(x=10,y=55)

#Host port entry
host_port = tk.Label(frame, text="Host Port", font=("Helvetica", 14), bg="#FFFF00", width= 17,)
host_port.place(x=10,y=100)
hostPortEntry = tk.Entry(frame,bg="#FFFF00",font=("Helvetica", 14), width=17,
                         textvariable=tk.StringVar(root, value="9999"))
hostPortEntry.place(x=10,y=135)


#Nickname entry
nickname = tk.Label(frame, text="Nickname", font=("Helvetica", 14), bg="#FFFF00", width= 17,)
nickname.place(x=10,y=180)
nameEntry = tk.Entry(frame,bg="#FFFF00",font=("Helvetica", 14), width=17,
                     textvariable=tk.StringVar(root, value="TestUser"))
nameEntry.place(x=10,y=215)

defaultAmount = tk.StringVar(root, value="10")

#Port entry
# port = tk.Label(frame, text="Port", font=("Helvetica", 14), bg="#FFFF00", width= 17,)
# port.place(x=10,y=255)
# portEntry = tk.Entry(frame,bg="#FFFF00",font=("Helvetica", 14), width=17,
#                      textvariable=tk.StringVar(root, value="5050"))
# portEntry.place(x=10,y=290)



#Buttons
#Add commands to buttons

#Register
register = tk.Button(frame, text="Register", width=25, height=2, fg= "white", bg="#000000",
                    command= register) 
register.place(x=10,y=350)

Deregister = tk.Button(frame, text="Deregister", width=25, height=2, fg= "white", bg="#000000",
                       command=deregister) 
Deregister.place(x=10,y=400)

retrieve_client = tk.Button(frame, text="Retrieve Client", width=25, height=2, fg= "white", bg="#000000",
                            command=retrieve) 
retrieve_client.place(x=10,y=450)

retrieve_all_clients = tk.Button(frame, text="Retrieve All Clients", width=25, height=2, fg= "white", bg="#000000",
                                 command=retrieve_all) 
retrieve_all_clients.place(x=10,y=500)

stress = tk.IntVar
connection = tk.IntVar
# Test checkboxes
stressTest = tk.Checkbutton(frame,text = "Stress test",activebackground="black" , activeforeground="blue" 
                 ,bg="#263D42",bd=10, 
                 onvalue = 1, offvalue = 0, variable=stress)
stressTest.place(x=400, y=25)

connectionTest = tk.Checkbutton(frame,text = "Connection test",activebackground="black" , activeforeground="blue" 
                 ,bg="#263D42",bd=10, 
                 onvalue = 1, offvalue = 0, variable=connection)
connectionTest.place(x=400, y=70)

root.mainloop()