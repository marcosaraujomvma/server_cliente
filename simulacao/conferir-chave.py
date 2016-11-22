from Crypto.PublicKey import RSA
#@diretorio = 
fpr = open("keyPrivate.der")
key = RSA.importKey(fpr.read())

fpu = open("keyPublic.pem")
public_key = RSA.importKey(fpu.read())

if key.has_private(): print "Private key"

if key.can_sign():print "PODE ASSINAR"

codificado = public_key.encrypt("carro","senha")#codifica a string carro

print codificado

descodificado = key.decrypt(codificado)

print descodificado


assinatura = key.sign("carro","")

print assinatura



z = public_key.verify("carro",assinatura)


print z
