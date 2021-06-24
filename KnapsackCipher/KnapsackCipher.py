###############################
# 제   목 : 컴퓨터시스템보안 과제 #
# 작 성 자 : 20181397 유찬영    #
# 설   명 : 배낭암호 구현        #
###############################

def createGF(array):
    b = []
    global n
    n = 900
    global r
    r = 37
    for i in array:
        b.append((i * r) % n) 
    return b

def permuteGF(arrayToPermute, subTable): # Permute
    answer = []
    for i in subTable: 
        answer.append(arrayToPermute[i - 1]) 
    return answer                            

def stringToAscii(string): # 문자열을 암호화 해주는 함수
    ascii_list = [] 
    new_string = bin(ord(string)) # Alice의 문자열을 7비트 ASCII코드를 사용하여 암호화
    for i in new_string:
        ascii_list.append(i)      # 부호화한 문자열을 새로운 리스트에 저장
    return list(map(int, ascii_list[2:])) 
        
def knapsackSum(public_key, Alice_key):
    sum = 0
    for i in range(len(public_key)):
        sum +=( public_key[i] * Alice_key[i])
    return sum

def expandEuclid(num1, num2): # 확장 유클리드 호제법 
    r1, r2 = num1, num2       # 레퍼런스 참조한 부분
    u1, u2 = 1, 0
    v1, v2 = 0, 1

    while(r2 > 0):
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r

        u = u1 - q * u2
        u1, u2 = u2, u

        v = v1 - q * v2
        v1, v2 = v2, v

    return u1 # num1의 역원을 return

def inv_knapsackSum(s_prime, array):
    newlist = []
    for i in list(reversed(array)): # 큰 수부터 비교하기 위함
        if s_prime > i:
            s_prime -= i
            newlist.append(1)
        elif s_prime < i:
            newlist.append(0)
        else:
            s_prime -= i
            newlist.append(1)
       
    return newlist

if __name__ == '__main__':
    alice_string = 'g' # A Message (Alice -> Bob)
    print('Alice가 bob에게 보낼 문자열 : ', alice_string)
    array = [7, 11, 19, 39, 79, 157, 313]
    
    substitution_table = [4, 2, 5, 3, 1, 7, 6]
    print('t : ', createGF(array))
    print('a : ',permuteGF(createGF(array), substitution_table)) # Public Key
    print('Bobs private', array)
    public_key = permuteGF(createGF(array), substitution_table) # 생성된 공개키를 변수에 저장

    print('Alice data : ', stringToAscii(alice_string))
    alice_key = stringToAscii(alice_string) # 앨리스가 입력한 문자열의 순서짝을 변수에 저장
    print('s = knapsackSum(a, x) = ',knapsackSum(public_key, alice_key)) 
    s = knapsackSum(public_key, alice_key)
    inverse_element = expandEuclid(r, n)
    s_prime = s * inverse_element % n
    print('s` = s * r^-1 mod n 결과 = ', s_prime)

    print('x` = ',inv_knapsackSum(s_prime, array))
    new_list = inv_knapsackSum(s_prime, array)

    print('x  = ',permuteGF(new_list, substitution_table))
    final_list = permuteGF(new_list, substitution_table)

    final_string = ''.join([str(_)for _ in final_list]) # 리스트를 문자열로 변환
    print('복호화한 결과 : ', chr(int(final_string, 2))) 