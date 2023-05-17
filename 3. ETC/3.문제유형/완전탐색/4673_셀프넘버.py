# 셀프 넘버 : 이런 걸 (ex)(13 --> 1+3+13 = 17)
# 생성자가 없는 셀프 넘버를 모두 뽑아내라

# 2231 분해합이랑 같은 유형의 문제
def d(n):
    answer = n
    for i in str(n):
        answer += int(i)
    return answer

answer = [i for i in range(1,10001)]

for i in range(1,10000):
    try:
        answer.remove(d(i))
    except ValueError:
        pass

for i in answer:
    print(i)



# 난이도 : 하 
# 그냥 1부터 10000까지 직접 셀프넘버를 구하고 10000 에서 하나씩 제거하면 되겠네 
# 완전 탐색 