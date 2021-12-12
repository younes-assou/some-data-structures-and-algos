#!/usr/bin/python3
import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**30) # new thread will get stack of such size

result = []
def inordertraversal(tree, root=0):
  if root ==-1: return
  inordertraversal(tree, tree[root][1])
  result.append(tree[root][0])
  inordertraversal(tree, tree[root][2])

def isbst():
  for i in range(len(result)-1):
    if result[i+1]<result[i]: return False
  return True

def isBST(tree, rt=0):
  if rt == len(tree):return True
  result = None
  if tree[rt][1] != -1 and tree[rt][2] != -1:
    result = tree[tree[rt][1]][0] < tree[rt][0] <= tree[tree[rt][2]][0]
  elif tree[rt][1] == -1 and tree[rt][2] != -1:
    result = tree[rt][0] <= tree[tree[rt][2]][0]
  elif tree[rt][1] != -1 and tree[rt][2] == -1:
    result = tree[tree[rt][1]][0] < tree[rt][0]
  else:
    result =True
  return result and isBST(tree,rt+1)

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree)<=1: return True
  inordertraversal(tree)
  xx = isBST(tree)
  if xx:
    return isbst()
  return xx


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
