
'''
heapq

종류 
    - 최소힙(최솟값 뽑아내줌)
    - 최대힙(최댓값 뽑아내줌)
    시간 복잡도 : O(log(n)) 보장

하나씩 삭제할때마다 내부적으로 이진 트리의 재배치가 일어나기 때문에
가장 작은 값에 접근할때는 heap[0]으로 접근하면 된다 

# python에서는 heapq를 별개의 자료구조가 아닌 그냥 list를 통해서 구현한다(갓이썬)
# 그냥 list를 생성한 다음 heapq 모듈의 함수를 호출할 때마다 리스트 인자를 넘겨주기만 하면 된다.

heappush() 
    - 시간 복잡도 : O(logn(n))
    - 내부적으로 이진 트리에 원소를 추가

heapop()
    - 시간 복잡도 : O(logn(n))
    - 가장 작은 값 
'''
import heapq

li = []
heapq.heapify(li)
heapq.heappush(li, 4)
heapq.heappush(li, 1)
heapq.heappush(li, 2)
heapq.heappush(li, 67)
heapq.heappush(li, 7)

print(li)   # [1, 4, 2, 67, 7] : 이진 트리 형태로 저장
# 1 / 4,2 / 67, 7

heapq.heappop(li)
print("1 ", end=" ")
print(li)
heapq.heappop(li)
print("2 ", end=" ")
print(li)
heapq.heappop(li)
print("3 ", end=" ")
print(li)