search_graph = {
        1: {2, 3, 4},
        2: {1, 5, 6},
        3: {1, 7},
        4: {1, 8},
        5: {2, 9},
        6: {2, 10},
        7: {3},
        8: {4},
        9: {5},
        10: {6},
        }
root = 1

def dfs(graph, root):
    visitedList = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visitedList:
            visitedList.append(n)
            stack += graph[n] - set(visitedList)

    return visitedList

a = 'awefabjev'
li = [i for i in a]

from itertools import permutations as perm
b = perm(li,3)

for i in b:
    print(i)