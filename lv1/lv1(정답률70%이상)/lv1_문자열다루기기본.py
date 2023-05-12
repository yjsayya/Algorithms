# [정규표현식 ㅎ]
#     str.isdigit() - 숫자 확인
#     str.isalpha() - 영어, 한글 확인
#     str.isupper() - 영어 대문자 확인
#     str.islower() - 영어 소문자 확인
#     str.isalnum() - 영어, 한글, 숫자 확인
#         param - x
#         return - boolean

def solution(s):
    
    if len(s)==4 and s.isdigit():
        return True
    elif len(s) == 6 and s.isdigit() :
        return True
        
    return False