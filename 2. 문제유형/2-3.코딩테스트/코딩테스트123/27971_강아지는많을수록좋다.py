
n = input()
cnt = 0

if n == 'X':
    print(0)
else:
    while True:
        n = 'X' + n[1:]
        cnt += 1

        if n == 'X' * len(n):
            break

        idx = n.index('O')
        n = 'O'*idx + 'X' + n[idx+1:]
        cnt += 1

    print(cnt % (1_000_000_007))