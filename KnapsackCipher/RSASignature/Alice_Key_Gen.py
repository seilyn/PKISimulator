from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256

AlicePrivKey = RSA.generate(2048)
f = open('AlicePrivKey.pem', 'wb')
f.write(AlicePrivKey.export_key('PEM', passphrase="!@#$"))
f.close()
f = open('AlicePubKey.pem', 'wb')
f.write(AlicePrivKey.publickey().export_key('PEM'))
f.close()