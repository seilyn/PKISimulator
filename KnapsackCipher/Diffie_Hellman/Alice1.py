def Alice_Key_Generate():
    g = 7 
    p = 23
    x = 3
    R1 = (g ** x) % p
    f = open("Alice_Key.pem", 'w')
    f.write(str(R1))
    f.close()
    
    try: 
        fp = open('Bob_Key.pem','r')
        data = fp.read()
        data = int(data) # pem에서 추출한 값을 정수로 변환
        fp.close()
        K2 = (data ** x) % p
        print("Bob's K = ",K2)
        return K2

    except FileNotFoundError:
        print("Bob_Key.pem 파일이 없습니다.")
