from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
import base64
import RSASignature.Alice_Key_Gen

f = open('AlicePrivKey.pem', 'r')
AlicePrivKey = RSA.import_key(f.read(), passphrase="!@#$")
f.close()
f = open('BobPubKey.pem', 'r')
BobPubKey = RSA.import_key(f.read())
f.close()
message = 'To be signed'

h = SHA256.new(message.encode('utf-8'))
signature = pkcs1_15.new(AlicePrivKey).sign(h)
signature = base64.b64encode(signature).decode("utf-8")

fp1 = open('AliceMessage.txt', 'w')
fp1.write(message)

fp2 = open('AliceSignature.sig', 'w')
fp2.write(signature)

fp1.close()
fp2.close()
# print("Alice sent (", message, signature, ") to Bob.")