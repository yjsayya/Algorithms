'''
    제한사항 - M, N(1 ≤ M ≤ N ≤ 99)
    ** 제한사항이 그리 크지 않아서 그냥 개 ㅈㄹ 노가다로 풀었고 잘 맞았다 
        - 하지만 당연히 이게 좋은 풀이는 아니라고 생각한다
        - 다른 사람은 어떻게 풀었는지 한번 보자 ㅋㅋ 

    아이디어 - [21, two one] 이렇게 정리한다음에 정렬하고 출력하는게 더 좋네 그러네 ... 

'''

# # 1. 입력 받기
# m,n = map(int,input().split())

# # 2. dic 만들기
# dic1 = dict()
# dic1[0] = "zero"
# dic1[1] = "one"
# dic1[2] = "two"
# dic1[3] = "three"
# dic1[4] = "four"
# dic1[5] = "five"
# dic1[6] = "six"
# dic1[7] = "seven"
# dic1[8] = "eight"
# dic1[9] = "nine"

# dic2 = dict()
# dic2['zero'] = '0'
# dic2['one'] = '1'
# dic2['two'] = '2'
# dic2['three'] = '3'
# dic2['four'] = '4'
# dic2['five'] = '5'
# dic2['six'] = '6'
# dic2['seven'] = '7' 
# dic2['eight'] = '8'
# dic2['nine'] = '9'

# # 3. 숫자 --> 알파벳
# li = []
# for i in range(m,n+1):
#     if len(str(i)) == 1:
#         li.append(dic1[i])
#     else:
#         word = ''
#         for j in str(i):
#             word += dic1[int(j)]
#             word += ' '
#         li.append(word.rstrip())

# # 4. 사전 순으로 정렬
# li = sorted(li)

# # 5. 알파벳 --> 숫자
# num = []
# for i in li:
#     if ' ' not in i:
#         num.append(int(dic2[i]))
#     else:
#         a,b = i.split(' ')
#         num.append(int(dic2[a]+dic2[b]))

# # 6. 조건에 맞게 출력
# x = 1
# for i in num:
#     if x == 10:
#         print(i, end='\n')
#         x = 1
#     else:
#         print(i, end=' ')
#         x += 1


# 다른 사람 풀이
# m, n = map(int, input().split())

# dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
#         '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

# lst = []

# for i in range(m, n+1):
#     itoa = ' '.join([dict[j] for j in str(i)])
#     lst.append([i, itoa])
    
# lst.sort(key=lambda x:x[1])

# for i in range(len(lst)):
#     if i%10 == 0 and i!= 0:
#         print(sep = '\n')
#     print(lst[i][0], end=' ')


# 3번째 풀이 -- 위에 풀이를 보고 내가 다시 한번 풀어봤다 
m,n = map(int,input().split())

dic = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
        '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

li = []
for i in range(m, n+1):
    a = [i]
    if len(str(i)) == 1:
        a.append(dic[str(i)])
    else:
        word = ''
        for j in str(i):
            word += (dic[j] + ' ')
        a.append(word.rstrip())

    li.append(a)

li = sorted(li, key= lambda x : x[1])

x = 1
for i in li:
    if x == 10:
        print(i[0], end='\n')
        x = 1
    else:
        print(i[0], end=' ')
        x += 1
