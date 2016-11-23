from Crypto.PublicKey import RSA
#@diretorio = 
fpr = open("keypr.pem")
key = RSA.importKey(fpr.read())

fpu = open("keypu.pem")
public_key = RSA.importKey(fpu.read())

if key.has_private(): print "Private key"

if key.can_sign():print "PODE ASSINAR"

codificado = public_key.encrypt("4235319000000000000000000000000000000000000kkkkkkkk212121012012101201201255101502151502125015024154214014215440324154650412432145160513421316kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk0","senha")#codifica a string carro

print codificado

descodificado = key.decrypt(codificado)

print descodificado


assinatura = key.sign("carro","")

print assinatura



z = public_key.verify("carro",assinatura)


print z
