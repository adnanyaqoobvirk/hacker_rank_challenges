# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
common_ancestor = None

def lca(root, v1, v2):
  get_common_ancestor(root, v1, v2)
  global common_ancestor
  return common_ancestor

def get_common_ancestor(node, v1, v2):
  node_exist = False
  if node.info == v1 or node.info == v2:
    node_exist = True
  
  left_node_exist = False
  if node.left:
      left_node_exist = get_common_ancestor(node.left, v1, v2)
  
  right_node_exist = False
  if node.right:
      right_node_exist = get_common_ancestor(node.right, v1, v2)
      
  if (left_node_exist and right_node_exist) or (node_exist and right_node_exist) or (left_node_exist and node_exist):
    global common_ancestor
    common_ancestor = node
    return False
  else:
    return left_node_exist or right_node_exist or node_exist 
