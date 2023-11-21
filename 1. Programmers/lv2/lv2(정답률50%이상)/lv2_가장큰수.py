""""""
"""
    1. 문자열로 모두 바꿔주고
    2. 각 문자열을 x3을 기준으로 정렬한 후
    3. str(int()) 처리해서 리턴한다 
        --> 맨앞에 0이 나올 수 있기 때문에
"""
def solution(numbers):
    li = [str(i) for i in numbers]
    return str(int("".join(sorted(li, key = lambda x : x*3))))