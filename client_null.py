#imports
import socket
import threading
import time
import random
import os
import sys
import base64

#make by NULL
#Todos projetos sao de estudos e sem nenhuma intencao de danificar algum sistema
#caso alguem utilize a ferramenta para atos ilicitos nao me responsabilizo pelos atos !
#Version 1.0
#Simples Client + commands

def varses(): #variables
    global t, temp, thlock, offf, passed
    t = str(time.ctime(time.time()))
    tempo = t[10:19]

    thlock = threading.Lock()
    offf = False
    passed = False

def comandos(cmd): #commands
    if cmd == "/ip":
        print(host+":"+str(port2))
        
    if cmd == "/rT":
        print(str(recvT))
        
    if cmd == "/conn":
        global addr, data
        print(str(s))
        print(str(addr))
        
    if cmd == "/quit" or cmd == "/exit":
        global server, s, alias
        encoded = str(base64.b64encode(alias +" >>> "+ "EXITED"))
        s.sendto(encoded, server)
        print("Exit...")
        sys.exit(1)
        
    if cmd == "/time":
        print("Time:"+str(tempo))
        
    if cmd == "/restart":
        global server, s, alias
        encoded = str(base64.b64encode(alias +" >>> "+ "EXITED"))
        s.sendto(encoded, server)
        os.system("clear")
        main()
    
def recev(name, sock): #recev th
    
    while not offf:
        try:
            thlock.acquire()
            while True:
                global data, addr
                data, addr = sock.recvfrom(1024)
                dat = base64.b64decode(str(data))
                if dat[0:defec] != alias:
                    print (str(dat))
        except:
            pass
        finally:
            thlock.release()
            
def main(): #main
    varses()
    host = '127.0.0.1'
    port2 = int(random.randint(5000,6000))
    print("Your port-> "+str(port2))
    port = int(input("Server port-> "))
    server = ('127.0.0.1',port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port2))
    s.setblocking(0)
    recvT = threading.Thread(target=recev, args=("RecvThread",s))
    recvT.start()

    alias = raw_input("ID-> ")
    message = "<>> ENTERED <<>"
    os.system("clear")
    print("Welcome to 1337Chat")
    defec = len(alias)

    while message != 'q':
        if message != '':
            encoded = str(base64.b64encode(alias +" >>> "+ message))
            s.sendto(encoded, server)
        message = raw_input("")
        thlock.acquire()
        comandos(message)
        thlock.release()
        
    offf = True
    recvT.join()
    s.close()
    
main()
