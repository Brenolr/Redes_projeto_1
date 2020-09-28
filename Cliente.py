import sys
import socket as s

def main():

    MAX_LINE = 256
    host=''
    hp=""
    buf=b""
    Server_port = 5432
    
    #LEMBRETE: argc pode ser obtido pelo tamanho de argv 
    if(len(sys.argv)==2):
        host=sys.argv[1]
    else:
        raise RuntimeError("usage: simplex-talk host\n")
    
    print("achou o Endereço")

    #Pega o endereço IP
    hp= s.gethostbyname(host)
    if(hp==""):
        raise RuntimeError("simplex-talk: unknown host:" + str(host)+ "\n" )
    print("achou o IP")

    #cria o socket na configurações
    sin = s.socket(s.AF_INET,s.SOCK_STREAM)
    print("Socket configurado")

    #faz a conexão
    try:
        sin.connect((hp, Server_port))
        print("conectado")
    except:
         raise RuntimeError("simplex-talk: connect")
    
    #loop principal para receber e enviar mensagens
    buf = sin.recv(MAX_LINE)
    if(buf!=b""):
        sin.sendall(buf)
    print("Primeira Passagem pelo Loop")

    while(buf!=b""):
        sin.recv(MAX_LINE)
        buf[MAX_LINE-1]=b'0'
        sin.sendall(buf)
        print("No Loop")

main()        
          