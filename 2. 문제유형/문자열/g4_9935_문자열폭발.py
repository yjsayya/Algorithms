
'''
    제한사항 
    - (1 <= s <= 1_000_000)
    - (1 <= bomb <= 36)
    시간복잡도 : O(N^2)은 당연히 시간초과
    시간복잡도 : O(N)으로 풀어냈다

    bomb이 별로 길지 않아서 두번째 풀이 시간 초과 없이 가능했다 
    
    ** 꼭 기억해두자  
    stack을 이용해서 문자열을 처음부터 끝까지 한번 씩 읽으면서 처리 
    pop()이 문자열을 합치는 것보다 훨씬 빠르니깐 pop()을 이용한다.
'''

# 첫번째 풀이 - 시간복잡도 고려 안 했더니 시간초과 났다 
# stri = input()
# bomb = input()

# while bomb in stri:
#     stri = stri.replace(bomb, '')

# if len(stri) == 0: print("FRULA")
# else: print(stri)


# 두 번째 풀이 
s = input()
bomb = input()

stack = []
bombLen = len(bomb)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-bombLen:]) == bomb:
        for _ in range(bombLen):
            stack.pop()

if stack: print(''.join(stack))
else: print('FRULA')