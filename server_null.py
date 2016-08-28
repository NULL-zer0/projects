#imports
import socket
import time
import random
import base64
import sys
import os

#make by NULL
#Todos projetos sao de estudos e sem nenhuma intencao de danificar algum sistema
#caso alguem utilize a ferramenta para atos ilicitos nao me responsabilizo pelos atos !
#Version 1.0
#Simples Server + commands

def main(): #main
    print("1 - Random port(5000-6000)")
    print("2 - Define your port")
    x = input("Choice ->")
    if x == 1:
        port = int(random.randint(5000,6000))
    elif x == 2:
        port = int(input("Enter port-> "))
    else:
        port = int(random.randint(5000,6000))

    host = '127.0.0.1'
    print("Port -> "+str(port))

    clients = []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    s.setblocking(0)

    sair = False
    print "Server Started."
    while not sair:
        try:
            data, addr = s.recvfrom(2048)
            dat = base64.b64decode(data)
            if "/quit" in str(dat): #/quit
                sair = True
            if addr not in clients: #add client
                clients.append(addr)
            if "/s_restart" in dat: #restart server
                print("Restarting. . .")
                os.system("clear")
                return main()
            #if "/s_datamod" in dat:
             #  for client in clients:
              #      dat = dat + " #modific"
                #    s.sendto(str(dat), client)
                  #  print(str(dat))
            print time.ctime(time.time()) + str(addr) + " " + str(dat)
            #print(str(data))
            for client in clients:
                s.sendto(data, client)
        except:
            pass
        
    s.close()
main()
