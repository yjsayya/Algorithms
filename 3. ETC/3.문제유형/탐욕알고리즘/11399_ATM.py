# 시간복잡도 고려 안해줘도 되는 것 같다
# 1 <= n <= 1000
# 1 <= person <= 1000


# 첫번째로 푼 풀이
n = int(input())
people = list(map(int, input().split()))
answer = 0

people.sort()
# for i in range(1,len(people)+1):
#     answer += sum(people[:i])

# 이렇게 푸는 것이 시간복잡도에서 유리하지 않나 싶다
m = len(people)
for i in range(m):
    answer += people[i] * (m - i)

print(answer)



# 1
# 1+2 = 3
# 1+2+3 = 6
# 1+2+3+3 = 9
# 1+2+3+3+4 = 13
