
# 미리 계산해서 -- 시간복잡도 아주 ㅇㄷ일 듯 
# 내 풀이가 가장 좋은 풀이라고 생각함 ㅋㅋㅋ

def solution(price, money, count):
    
    answer = price * (count+1) * count / 2 - money
    
    if answer < 0:
        return 0
    else:
        return answer