import sys

n = int(sys.stdin.readline())
tree = dict()

for _ in range(n):
    root, left,right = sys.stdin.readline().rstrip().split()
    tree[root] = [left,right]

print(tree)

def preorder(root):
    # 1. 종료 조건
    if root == '.':
        return
    # 2. 문제에 대한 정의
    else:
        print(root, end='')
        preorder(left)
        preorder(right)


def inorder(root):
    # 1. 종료 조건
    if root == '.':
        return
    # 2. 문제에 대한 정의
    else:
        preorder(left)
        print(root, end='')
        preorder(right)

def postorder(root):
    # 1. 종료 조건
    if root == '.':
        return
    # 2. 문제에 대한 정의
    else:
        preorder(left)
        preorder(right)
        print(root, end='')

preorder('A')
inorder('A')
postorder('A')
