''''''
"""
    구현문제
    -- 솔직히 이 정도는 쉽게 풀 수 있어야지 ...
    -- 이건 좀 반성할 필요가 있다 
"""

def solution(s):
    ans = []

    s = s[2:-2]
    s = s.split('},{')

    for i in sorted(s, key=len):
        li = i.split(',')
        for j in li:
            if int(j) not in ans:
                ans.append(int(j))

    return ans


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
