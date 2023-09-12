
'''
    제한사항 (1 <= n <= 100)

    idea : 시간복잡도가 별로 높지 않아사 - 해당 수열을 100항 까지 그냥 구해버렸다
    시간복잡도 : O(200)
'''

n = int(input())

li1 = [1,1,1,2,2]
for i in range(95):
    li1.append(li1[-1] + li1[-5])

li2 = [int(input()) for _ in range(n)]

for j in li2:
    print(li1[j-1])