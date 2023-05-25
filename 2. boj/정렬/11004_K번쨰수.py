# 실버 5
'''
    음 .. 아주 간단한 문제 
    제한사항
        (1 <= n <= 5,000,000)
        (1 <= k <= n)
        (-10^9 ≤ Ai ≤ 10^9)
    결국 시간 복잡도 어떻게 할건지 물어보는 문제였다 

    병합정렬 -- 병합정렬 물어보는 문제였던 것 같은데
    퀵정렬 -- 여기서 퀵정렬은 시간초과
    파이썬 라이브러리 O(nlogn)을 보장해서 그냥 풀어낼 수 있었데

    돌려보니깐 파이썬 라이브러리가 병합정렬보다 두배 정도 빨랐다 
    이러면 그냥 파이썬 라이브러리가 쵝오인데 ...?
    굳 병합 정렬을 쓸 필요가 있나? 
'''


# 내가 푼 풀이
import sys

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

print(sorted(li)[k-1])






# 병합정렬로 푼 풀이 
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = list(map(int,input().split()))

def merge_sort(arr):

    if len(arr) <= 1: # 원소가 1개인 경우 종료
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i,j,k = 0,0,0

    # i, j 가 지칭하는 값 비교, 작은 값을 arr[k] 에 넣기
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1
        
        k += 1

    if i == len(left): # 한쪽 리스트가 끝난 경우 나머지 리스트를 넣어 줌
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
    return arr

arr = merge_sort(arr)

print(arr[K-1])