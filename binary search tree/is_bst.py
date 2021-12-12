#!/usr/bin/python3
import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

result=[]
def inordertraversal(tree, root=0):
  if root ==-1: return
  inordertraversal(tree, tree[root][1])
  result.append(tree[root][0])
  inordertraversal(tree, tree[root][2])

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree)==0: return True
  inordertraversal(tree)
  for i in range(len(result)-1):
    if result[i+1]<result[i]: return False
  return True


def main():
  nodes = int(input().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, input().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
