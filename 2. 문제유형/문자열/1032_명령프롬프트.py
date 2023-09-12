# 아주 어렵지 않은 문제
    # 생각보다 굉장히 잘 풀었다 깔끔하게
    # 첫번째 단어만 list[]
    # 나머지는 그냥 문자열로 받아서 처리 했음 - 문자열은 수정이 어려워서 이렇게 함

# 첫번째로 푼 풀이
# n = int(input())
# firstFile = list(input())
# files = [" "] * (n-1)
#
# if n != 1:
#     for i in range(n-1):
#         files[i] = input()
#
#     nameLen = len(files[0])
#     for j in files:
#         for k in range(nameLen):
#             if firstFile[k] != j[k]:
#                 firstFile[k] = '?'
#
# print("".join(firstFile))

# -------------------------------------------------
# 이렇게 firstFile을 그냥 문자열로 처리해도 큰 문제는 없을 것 같다 
n1 = int(input())
firstFile1 = input()
files = [" "] * (n1-1)

if n1 != 1:
    for i in range(n1-1):
        files[i] = input()

    nameLen = len(files[0])
    for j in files:
        for k in range(nameLen):
            if firstFile1[k] != j[k]:
                firstFile1 = firstFile1.replace(firstFile1[k], "?")

print(firstFile1)



