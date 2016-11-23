# -*- coding: utf-8 -*-
#Servidor Socket com thread concorrentes
#Servidor pode ser usado para linux e windows
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python 2.7
import socket, ssl, thread,time
from Crypto.Hash import SHA

ts = 0
lista = []

def teste(newsock,fromaddr):
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.bind(('', 8081))
    #sock.listen(1)
    #newsock, fromaddr = sock.accept()
    conn = ssl.wrap_socket(newsock, server_side=True, certfile='chaves/certificado-chave.pem', keyfile='chaves/certificado-chave.pem')#certificado
    conn.setblocking(0)
    fpu = open("chaves/medidor01_Publickey.pem")
    while True:
        try:
            buf = conn.read(512)#recebe os dados ja decodificado
            if buf == '':
                #print("nenhuma mensagem para receber!")
                
                break
            else:
                split = buf.split(";")
                id_medidor =  split[0]
                leitura =  split[1]
                print leitura
                ts_medidor = split[2]
                print ts_medidor
                assinatura_str_tupla = split[3]
                assinatura_str = assinatura_str_tupla[1:len(assinatura_str_tupla)-2]
                assinatura_long = long(assinatura_str)
                print assinatura_long
                print type (assinatura_long)
                msg = ("%s;%s"%(str(leitura),str(ts_medidor)))
                hash = SHA.new(msg).digest()
                print msg
                print hash
                #fpu = open("chaves/medidor01_Publickey.pem")
                public_key = RSA.importKey(fpu.read())
                print public_key
                #print fpu
                assinatura_long_tupla = (assinatura_long,)
                print assinatura_long_tupla
                z = public_key.verify(hash,assinatura_long_tupla)
                
                print buf
                print z
                
                """
                arq = open('lista.txt','w')
                ts = time.time()
                print ("ID;NºPCT;TSM;TSS\n%s;%s"%(buf,ts))
                lista.append("%s;%s\n"%(buf,ts))
                #print(lista)
                arq.writelines(lista)
                arq.close()
                """
                
        except:
            pass
            
    conn.close()
    thread.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8081))
sock.listen(1)
print("Servidor Funcionando!")

while True:
    newsock, fromaddr = sock.accept()
    #con, cliente = tcp.accept()
    
    thread.start_new_thread(teste,tuple([newsock,fromaddr]))
    print("Abriu nova Thread!")




