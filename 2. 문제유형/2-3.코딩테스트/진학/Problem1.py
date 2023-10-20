
def solution(n,ladder):
    ans = []

    for idx in range(n): # 0,1,2,3번 사람들
        loc = idx
        for arr in ladder:
            # 1. 위치가 양 끝에 있을 때;
            if loc == 0:
                if arr[loc] == 1: loc += 1
            elif loc == n-1:
                if arr[loc-1] == 1: loc -= 1
            # 2. 사이에 있을 때;
            elif arr[loc] == 1:
                loc += 1
            elif arr[loc-1] == 1:
                loc -= 1
        ans.append(loc+1)
    print(ans)
    return ans

solution(4,[[1,0,1],[0,1,0],[0,0,1],[0,0,0],[1,0,0]])
