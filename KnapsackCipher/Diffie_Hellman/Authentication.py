from Diffie_Hellman.Alice1 import *
from Diffie_Hellman.Bob1 import *

def check():

    K_1 = Alice_Key_Generate()
    K_2 = Bob_Key_Generate()

    if K_1 == K_2:
        print("K1의 값은 ", K_1,"이며, ","K2의 값은 ", K_2, "이므로 서로 같습니다.")
    else:
        print("키가 서로 다릅니다.")

if __name__ == '__main__':
    check()