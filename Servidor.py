import sys
import socket as s

def main():

    MAX_LINE = 256
    Server_port = 7000

    #cria o socket na configurações
    sin = s.socket(s.AF_INET,s.SOCK_STREAM)
    print("Socket configurado")

    #inicia o modo passivo
    sin.bind(('',Server_port)) 
    sin.listen(5)
    print("Ouvindo porta")
    #espera por conexão
    while(True):
        print("Agurdando conexão")
        new_s, addr = sin.accept()
        while(True):
            print("Coenctado")
            data = new_s.recv(MAX_LINE)
            new_s.sendall(data)

main()