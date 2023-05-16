


# 결국 못 풀었다 ...
def solution(people, limit):
    
    cnt = 0
    people.sort()
    idx = 1
    
    if people[-1] <= (limit/2):
        n = len(people)
        if n % 2 == 0:
            return n // 2
        else:
            return (n // 2) + 1
        
    else:
        for i in range(len(people)):
            if people[i] > (limit/2):
                idx = i
                break
        if idx % 2 == 0:
            return len(people[idx:]) + (len(people[:idx])//2)
        else:
            return len(people[idx:]) + (len(people[:idx])//2) + 1


def solution(people, limit):

    answer = 0
    people.sort()
    
    start = 0 
    end = len(people) - 1
    
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    
    return answer




# 투포인터
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer