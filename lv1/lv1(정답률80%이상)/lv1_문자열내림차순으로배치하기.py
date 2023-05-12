# 깔끔하게 한줄 처리가 되긴 하는데 - 이게 시간복잡도에서 이득이 되는지는 모르겠음

def solution1(s):
    return ''.join(sorted(list(s), reverse=True))