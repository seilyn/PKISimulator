from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256


import RSASignature.Alice

# Bob side (key generation)

BobPrivKey = RSA.generate(2048)
f = open('BobPrivKey.pem', 'wb')
f.write(BobPrivKey.export_key('PEM', passphrase="!@#$"))
f.close()
f = open('BobPubKey.pem', 'wb')
f.write(BobPrivKey.publickey().export_key('PEM'))
f.close()

# Bob side (receive message)
f = open('BobPrivKey.pem', 'r')
BobPrivKey = RSA.import_key(f.read(), passphrase="!@#$")
f.close()
f = open('AlicePubKey.pem', 'r')
AlicePubKey = RSA.import_key(f.read())
f.close()


fp = open('Z:\Computer System Security\KnapsackCipher\KnapsackCipher\AliceSignature.sig', 'r')
data = fp.read()
print(data)
fp.close()

fp1 = open('Z:\Computer System Security\KnapsackCipher\KnapsackCipher\AliceMessage.txt', 'r')
message = fp1.read()
fp2 = open('Z:\Computer System Security\KnapsackCipher\KnapsackCipher\AliceSignature.sig', 'r')
signature = fp2.read()


h = SHA256.new(message.encode('utf-8'))
# print("Bob received message (", message, signature, ")from Alice.")

try:
    pkcs1_15.new(AlicePubKey).verify(h, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is not valid.")

fp1.close()
fp2.close()