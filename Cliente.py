import sys
import socket as s

def main():

    MAX_LINE = 256
    host='localhost'
    hp=""
    buf=b''
    Server_port = 7000
    fp = open('menssagem_cliente.txt', 'r')
        
    
    #LEMBRETE: argc pode ser obtido pelo tamanho de argv 
    if(len(sys.argv)==2):
        host=sys.argv[1]
    else:
        raise RuntimeError("usage: simplex-talk host\n")
    
    print("Achou o Endereço")

    #Pega o endereço IP
    hp= s.gethostbyname(host)
    if(hp==""):
        raise RuntimeError("simplex-talk: unknown host:" + str(host)+ "\n" )
    print("Achou o IP")

    #cria o socket na configurações
    sin = s.socket(s.AF_INET,s.SOCK_STREAM)
    print("Socket configurado")

    #faz a conexão
    try:
        sin.connect((hp, Server_port))
        print("Conectado a " + str(hp) + " port: " + str(Server_port))
    except:
         raise RuntimeError("simplex-talk: connect")
    
    sin.sendall(buf) 
    #loop principal para receber e enviar mensagens

    buf = fp.read(MAX_LINE//8-1)
    while(buf!=''):
        sin.sendall(buf.encode(encoding="utf-8"))
        buf = fp.read(MAX_LINE//8-1)
    print("mensagem enviada")
main()        
          