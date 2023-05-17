
# ** idea : 어쨌든 동전 개수를 최소로 하기 위해선 5의 개수가 많아야 한다!!
# 돈이 5보다 작은 경우 --> 예외처리 해주면 된다

# 첫번째 푼 풀이 --> 잘 푼 것 같다
cnt = 0
money = int(input())

if money == 3 or money ==1:
    print(-1)
else:
    while money >= 5:
        cnt += (money // 5)
        money %= 5

    if money % 2 == 0:
        cnt += (money // 2)
    else:
        cnt = cnt - 1 + ((money + 5) // 2)

    print(cnt)