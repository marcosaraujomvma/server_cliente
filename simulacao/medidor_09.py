# -*- coding: utf-8 -*-
#Cliente socket enviando mensagem de um numero aleatorio
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket, ssl, hashlib, time, random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA

CERT="33ae2a21f4c676cc14cf4473372fa365"
sock = socket.socket()
sock.settimeout(2)
sock.connect(('localhost', 8082))
conn = ssl.wrap_socket(sock)
fpr = open("chaves/medidor01_Privatekey.pem")
key = RSA.importKey(fpr.read())

id_medidor = input("qual é id do medidor?")

if hashlib.md5(conn.getpeercert(True)).hexdigest() != CERT:
    conn.close()
    print 'CERT diferente do esperado, tentando me hackearrrrrrr'
else:
    print 'Conectado!'
    for i in range(1):
        time.sleep(1)
        ts = time.time()
        leitura = random.randint(1,6)
        msg = ("%s;%s"%(str(leitura),str(ts)))
        hash = SHA.new(msg).digest()
        signature = key.sign(hash,"")
        msg_ass = "%s;%s;%s"%(str(id_medidor),msg,str(signature))
        conn.write(msg_ass)
        print 'enviado'
        print msg_ass
    conn.close()
