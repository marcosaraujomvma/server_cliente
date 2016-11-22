from Crypto.PublicKey import RSA
from Crypto import Random
rng = Random.new().read
RSAkey = RSA.generate(1024, rng)
f = open("keyPrivate.der","w+")
f.write(RSAkey.exportKey("DER"))
f.close()
f = open("keyPublic.pem","w+")
f.write(RSAkey.publickey().exportKey("PEM"))
f.close()
