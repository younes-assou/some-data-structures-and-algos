# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(input())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, input().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inordertraversal(self,root=0):
    if root ==-1: return
    self.inordertraversal(self.left[root])
    self.result.append(self.key[root])
    self.inordertraversal(self.right[root])

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.inordertraversal()
    return self.result

  def preordertraversal(self,root=0):
    if root ==-1: return
    self.result.append(self.key[root])
    self.preordertraversal(self.left[root])
    self.preordertraversal(self.right[root])

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preordertraversal()
    return self.result

  def postordertraversal(self,root=0):
    if root ==-1: return
    self.postordertraversal(self.left[root])
    self.postordertraversal(self.right[root])
    self.result.append(self.key[root])

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postordertraversal()
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()