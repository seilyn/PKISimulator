def Bob_Key_Generate():
    g = 7 
    p = 23
    y = 6
    R2 = (g ** y) % p
    f = open("Bob_Key.pem", 'w')
    f.write(str(R2))
    f.close()

    try: 
        fp = open('Alice_Key.pem','r')
        data = fp.read()
        data = int(data) # pem에서 추출한 값을 정수로 변환
        fp.close()
        K1 = (data ** y) % p
        print("Alice's K = ",K1)
        return K1

    except FileNotFoundError:
        print("Alice_Key.pem 파일이 없습니다.")
    