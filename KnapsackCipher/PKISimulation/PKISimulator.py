from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
import base64
import pickle #리스트를 저장할 모듈 import 

# 간단하게 리스트로 -> [공개키, 서명] : 인증서 - genCertificate() 함수

def genCertificate(myPubKey, CAPrivKey):
    CAList = [myPubKey]
    hash = SHA256.new(str(myPubKey).encode('utf8'))
    sign = pkcs1_15.new(CAPrivKey).sign(hash)
    CAList.append(sign)
    return CAList    

def veriCertificate(aCertificate, CACertificate):
    h = SHA256.new(str(aCertificate[0]).encode('utf8'))

    try:
        pkcs1_15.new(CACertificate[0]).verify(h, aCertificate[1])
        return True
    except(ValueError, TypeError):
        return False
    
def init():
    # a.
    CAPrivKey = RSA.generate(2048)
    f = open('CAPriv.pem', 'wb')
    f.write(CAPrivKey.export_key('PEM', passphrase="!@#$"))
    f.close()

    # b.
    f = open('CAPub.pem', 'wb') 
    f.write(CAPrivKey.publickey().export_key('PEM'))
    f.close()

    # c.
    f = open('CAPub.pem', 'r')
    CAPublicKey = RSA.import_key(f.read())
    h = open('CAPriv.pem', 'r')
    CAPrivateKey = RSA.import_key(h.read(), passphrase="!@#$")
    f.close()
    h.close()

    with open('CACertCA.plk', 'wb') as j:
        root = genCertificate(CAPublicKey, CAPrivateKey)
        CA_pub,S_CA = root
        pickle.dump([str(CA_pub), S_CA], j)
    # print(str(public_key), signature)

    #d. 
    BobPrivKey = RSA.generate(2048)
    Bob = open('BobPriv.pem', 'wb')
    Bob.write(BobPrivKey.export_key('PEM', passphrase="####"))
    Bob.close()

    #e.
    h1 = open('BobPub.pem', 'wb')
    h1.write(BobPrivKey.publickey().export_key('PEM'))
    h1.close()
    #f. 
    q = open('BobPub.pem', 'r')
    BobPubKey = RSA.import_key(q.read())
    q.close()

    with open('BobCertCA.plk', 'wb') as c:
        BobCertificate = genCertificate(BobPubKey, CAPrivateKey)
        pickle.dump([str(BobCertificate[0]), BobCertificate[1]], c)
    #g.
    M = "I bought 100 doge coins."
    hash1 = SHA256.new(M.encode('utf8'))

    p = open('BobPriv.pem', 'r')
    bobPrivKey = RSA.import_key(p.read(), passphrase="####")
    BobSignature = pkcs1_15.new(bobPrivKey).sign(hash1)
    p.close()   

    p1 = open('BobCertCA.plk', 'rb')
    Bob_pub2, S_Bob_CA = pickle.load(p1)
    print("Bob Sent (", M, BobSignature, [BobPubKey, S_Bob_CA], ") to Alice.")
    p1.close()

    #h.
    print("Alice Received (", M, BobSignature, [BobPubKey, S_Bob_CA], ") from Bob.")

    #i.
    fp = open('CACertCA.plk', 'rb')
    RootCertification = pickle.load(fp)
    CA_pub_key, S_CA = RootCertification
    fp.close()

    #j. ===
    with open('CAPriv.pem', 'r') as cp:
        CAPrivateKey = RSA.import_key(cp.read(), passphrase="!@#$")

        hash2 = SHA256.new(str(CA_pub_key).encode('utf8'))
        sign1 = pkcs1_15.new(CAPrivateKey).sign(hash2)
    
    hash3 = SHA256.new(str(CAPublicKey).encode('utf8'))
    signature = pkcs1_15.new(CAPrivKey).sign(hash3)

    if veriCertificate(root, root):
        print("검증 완료")
    else:
        print("검증 실패")
        return
    #k.
    if veriCertificate(BobCertificate, root):
        print("Bob 검증 완료")
    else:
        print("Bob 검증 실패")
        return

    #i.
    if veriCertificate([M, BobSignature], BobCertificate):
        print("메시지 검증 완료")
    else:
        print("메시지 검증 실패")
        return
    #m.
    print("Good job. Well done!")

if __name__ == '__main__':
    init()