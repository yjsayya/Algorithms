""""""
"""

"""

import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

def binary_search(arr, target):
    left,right = 0, len(arr)-1
    mid = (left + right) // 2

    while left < right:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

left,right = 0,2
diff = arr[0] - arr[1]
while left < right:
    if diff < arr[right] - arr[left]:
        right += 1
    else:
        pass

# 10 10 20 10 30