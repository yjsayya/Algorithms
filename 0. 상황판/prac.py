

def solution(numbers):
    li = [str(i) for i in numbers]
    return str(int("".join(sorted(li, key = lambda x : x*3))))
