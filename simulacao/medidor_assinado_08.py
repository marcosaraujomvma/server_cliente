# -*- coding: utf-8 -*-
#Cliente socket
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Util.randpool import RandomPool
import socket,time,random
from Crypto.Cipher import AES
import base64

fpr = open("chaves/medidor01_Privatekey.pem")
key = RSA.importKey(fpr.read())

fpu = open("chaves/keyPublic.pem")
public_key = RSA.importKey(fpu.read())

"""
BLOCK_SIZE=32


pool = RandomPool(1024)
pool.stir()
randfunc = pool.get_bytes
key= RSA.generate(1024, randfunc)#gera a chave aqui

print key



def encrypt(message, passphrase):
    h = SHA256.new()
    h.update(passphrase)
    key = h.digest()[0:16]
    
    IV = Random.new().read(16)
    aes = AES.new(key, AES.MODE_CFB, IV)
    criptograma = IV + aes.encrypt(message)
    return criptograma

"""

print("Pode Codificar? ",key.can_encrypt())

print("Pode Assinar? ",key.can_sign())

print("E privada? ",key.has_private())




print 'Para sair use CTRL+X\n'


id_medidor = raw_input("Digite o Id do Medidor: ")

server = raw_input("Digite o IP do Servidor: ")

HOST = server    # Endereco IP do Servidor
PORT = 6001           # Porta que o Servidor esta

for i in range(1):
 
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    
    ts = time.time()
    time.sleep(1)
    
    
    hash = SHA256.new(str(ts)).digest()
    
    signature = key.sign(hash,"")
    
    leitura = random.randint(1,6)#gera a leitura aletorio
    #n, e, d = key.n, key.e, key.d 
    msg = "%s;%s;%s;%s"%(signature,ts,id_medidor,leitura)
    msg2 = "%s;%s"%(id_medidor,msg)
    #msgcod = encrypt(msg,"medidor")
    msg_codificada = public_key.encrypt(msg2,"")
    #print base64.encodestring(str(msg_codificada))
    tcp.send(str(msg_codificada))
    
    print "Pacote %i Enviado!"%i
    print "Leitura: %i Kwh"%leitura
    tcp.close()
    #tcp.connect(dest)
