''''''
"""
    1. 이중 for문 - 완전탐색으로 풀기
        - 제한사항이 100만개이기 때문에 이용 불가능
    2. Hash를 이용한 완전탐색
        - hash의 경우 탐색에서 시간복잡도에서 이득이니깐 백만개면 문제 없이 가능하겠지
        - 출제 의도는 Hash 였던 것 같다
    3. 정렬 한번 하고 찾기
        .. str.find() 함수 사용
        .. str.startswith() 함수 사용
            - python은 정말 별의 별 함수가 다 있다 
            - 접두어의 길이가 m일 때; 시간복잡도 : O(m) 
        
    +a) for i,j in zip(phone_book, phone_book[1:) 이런 형태도 기억해두자
"""


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

    for i, j in zip(phone_book, phone_book[1:]):
        if j.find(i) == 0:
            return False

    return True

# 이렇게 Hash로 푸는게 정석인 듯 하다
def solution4(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer