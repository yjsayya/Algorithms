''''''
"""
    선형구조
    하나의 node -- (data, 다음노드의주소) 이런 식으로 구현
    
"""

'''
    노드에는 일단 데이터 자체가 두개가 필요하기 때문에 class를 통해서 구현해야한다
    
'''
class Node:
    # 생성자
    def __int__(self,data, next=None):
        self.data = data
        self.next = next

# # 노드 연결하기
node1 = Node(1)
node2 = Node(2)

node1.next = node2
head = node1

class Node:

    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data) # 마지막 끝에 데이터가 붙겠네 ㅇㅋ

node = head
while node.next:
    print(node.data)
    node = node.next

print(node.data)