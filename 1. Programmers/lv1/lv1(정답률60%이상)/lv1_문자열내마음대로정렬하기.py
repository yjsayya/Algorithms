'''
    sorted() 함수의 정렬 시간 복잡도는 일반적으로 O(nlogn)이다.
    이는 대부분의 정렬 알고리즘의 시간 복잡도 상한선입니다.

    이거 알아두자
'''

def solution(strings, n):
        
    return sorted(strings, key=lambda x: (x[n], x))