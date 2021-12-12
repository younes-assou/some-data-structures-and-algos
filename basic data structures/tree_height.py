# python3
import sys
import threading

class Node:
    # Constructor to create a new node
    def __init__(self):
        self.parent = None
        self.children = []

    def addChild(self,child):
        child.parent = self
        self.children.append(child)

def compute_height(n, parents):
    # Replace this code with a faster implementation
    nodes = [None for i in range(n)]
    for i in range(n):
        nodes[i] = Node()
    root = -1
    for child_index in range(n):
        parents_index = parents[child_index]
        if parents_index==-1:
            root = child_index
        else:
            nodes[parents_index].addChild(nodes[child_index])
    lastnode =None
    if root == -1: return 0
    q = []
    q.append(nodes[root])
    while len(q)!=0:
        node = q.pop(0)
        for n in node.children:
            q.append(n)
        lastnode = node
    height = 1
    while lastnode.parent !=None:
        height+=1
        lastnode = lastnode.parent
    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
