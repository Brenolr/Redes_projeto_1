import socket as s

def main():

    MAX_LINE = 256
    Server_port = 7000
    data=b""
    Max_Pending=5
    #cria o socket na configurações
    sin = s.socket(s.AF_INET,s.SOCK_STREAM)
    print("Socket configurado")

    #inicia o modo passivo
    sin.bind(('',Server_port)) 
    sin.listen(Max_Pending)
    print("Ouvindo porta")
    #espera por conexão
    while(1):
        conect=True
        print("Agurdando conexão")
        new_s, addr = sin.accept()
        print("Conectado com " + str(addr))
        
        fp = open('menssagem_servidor.txt', 'a')
        data=b'0'

        while(data!=b''):
            data = new_s.recv(MAX_LINE)
            print(data.decode(encoding='utf-8'))
            fp.write(data.decode(encoding='utf-8'))
        fp.close()
        new_s.close
main()