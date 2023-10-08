""""""
"""
    선형 -- 선형탐색 vs 이진탐색
    비선형 -- 이진 탐색 트리
    
    -- 정렬된 배열
    -- 시간복잡도 : O(logN)
"""

def binary_search(arr, target):
    left,right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1,4,6,12,15,17,22,26]
target = 17

idx = binary_search(arr,target)

if idx == -1:
    print("값이 없음")
else:
    print(idx,"에 위치")

