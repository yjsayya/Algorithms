# 이거보다 더 깔끔할 수가 있나? 

def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]