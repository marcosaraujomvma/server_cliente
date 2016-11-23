from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Util.randpool import RandomPool
"""
rng = Random.new().read
RSAkey = RSA.generate(1024, rng)

"""
pool = RandomPool(2048)
pool.stir()
randfunc = pool.get_bytes
RSAkey= RSA.generate(2048, randfunc)

f = open("keypr.pem","w+")
f.write(RSAkey.exportKey("PEM"))
f.close()
f = open("keypu.pem","w+")
f.write(RSAkey.publickey().exportKey("PEM"))
f.close()
