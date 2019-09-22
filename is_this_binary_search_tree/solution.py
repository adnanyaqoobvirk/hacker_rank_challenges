 
import sys

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
  max_, min_ = check_binary_search_tree(root)
  return False if max_ == sys.maxsize or min_ == -1 else True
  
def check_binary_search_tree(node):
    left_max = left_min = node.data
    if node.left:
        if node.data > node.left.data:
            left_max, left_min = check_binary_search_tree(node.left)
            if node.data <= left_max:
              left_max, left_min = sys.maxsize, -1
        else:
            left_max, left_min = sys.maxsize, -1
    
    right_max = right_min = node.data
    if node.right:
        if node.data < node.right.data:
            right_max, right_min = check_binary_search_tree(node.right)
            if node.data >= right_min:
              right_max, right_min = sys.maxsize, -1
        else:
            right_max, right_min = sys.maxsize, -1
    
    return max(left_max, right_max), min(left_min, right_min)
        
