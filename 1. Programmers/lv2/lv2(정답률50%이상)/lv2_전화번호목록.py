
'''
    str.startswith() 함수 

    ** 이중 for문 대신 zip()함수를 사용하면 시간복잡도를 크게 줄일 수 있다 
'''


# 첫번째 풀이
    # 그냥 이중 for문 돌렸더니 - 바로 시간초과 ㅋㅋ
def solution1(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[j].find(phone_book[i]) == 0:
                return False

    return True

# 두번째 풀이
    # 진짜 python은 별의별 함수가 다 있다 

def solution2(phone_book):
    phone_book.sort()

    for i,j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False

    return True

# 세번째 풀이
def solution3(phone_book):

    phone_book.sort()

    for i,j in zip(phone_book, phone_book[1:]):
        if phone_book[j].find(phone_book[i]) == 0:
                return False
    
    return True