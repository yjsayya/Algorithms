

# 첫번째 풀이
    # 아무 생각 없이 풀었더니 --> 시간초과 났음
    # 시간복잡도 고려해줘야할 것 같음
li = list(map(int,input().split()))
n = li[0]
k = li[1]

answer = ''
for i in range(1,n+1):
    answer += str(i)

print(int(answer) % k)


# 두번째 풀이
    # 시간복잡도 고려해보면 꽤 어려운 문제인 듯 하다 
    # 나머지 규칙이 있나...?
li = list(map(int,input().split()))
n = li[0]
k = li[1]

