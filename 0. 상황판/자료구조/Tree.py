a = "트리 구조"
"""
    자료 구조 - 복잡한 알고리즘 하나를 물어본다고 하면 보통 트리 구조를 많이 물어본다고 한다 
    
    1. 이진트리
    2. 이진탐색트리
    
    -- 결국 장점 = 왜 쓰냐? 
    --> 검색에서 ㅈㄴ 이득을 볼 수 있다  (이진트리 vs 배열) 특정 수를 검색해보자
    반부터 시작해야 훨씬 빠르게 접근을 할 수가 있겠지 ㅋㅋ 
    
"""

'''
<< Tree 구조 >>
    - 트리 = 그래프의 일종으로, 한 노드에서 시작한 순환이 없는 연결 그래프
    - ex) 
        .. 이진트리(binary tree)
        .. 이진탐색트리(Binary Search Tree)
        .. heap
    
    [용어 정리]
        - Node 
            .. Root Node
            .. (Parent Node vs Child Node)
            .. (leaf Node vs Internal node)
            .. sibling
        - Level, depth

    [이진트리 vs 이진탐색트리]
    
    [이진탐색트리 --> 탐색]
        1. 검색에서 ㅈㄴ 이득이다
            - 이진 탐색 트리's 탐색 시간 복잡도 : O(logN)
            - 배열's 탐색 시간 복잡도 : O(N)
            
        2. 
        
        ** 배열은 찾을 때 하나씩 다 찾아야하잖아
        -->  연결리스트로 구현하면 좋다
        

'''

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:

    # 1. root node 정의
    def __init__(self, head):
        self.current_node = None
        self.head = head

    # 2. Tree에 - 요소 삽입
    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 3. 검색 기능
    def search(self,value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False

# 자료 입력
head = Node(1)
bst = NodeMgmt(head)
bst.insert(2)
bst.insert(3)
bst.insert(4)

print(bst.search(4))
print(bst.search(8))



"""
면접 질문이 나오지 않을까? 
1. 이진 탐색트리가 무엇인가요? 
"""