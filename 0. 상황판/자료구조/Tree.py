a = "트리 구조"
"""
    자료 구조 - 복잡한 알고리즘 하나를 물어본다고 하면 보통 트리 구조를 많이 물어본다고 한다 
    
    1. 이진트리
    2. 이진탐색트리
    
    -- 결국 장점 = 왜 쓰냐? 
    --> 검색에서 ㅈㄴ 이득을 볼 수 있다  (이진트리 vs 배열) 특정 수를 검색해보자
    반부터 시작해야 훨씬 빠르게 접근을 할 수가 있겠지 ㅋㅋ 
    
"""

# --> 한번 구현해보도록 하자


# 1. 노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 2. 이진 탐색 트리에 데이터 넣기
class NoneMgmt:
    def __init__(self,head):
        self.head = head

    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break

            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

BST_NodeMgmt(head)