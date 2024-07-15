class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

# Problem 1
tree = TreeNode(5, TreeNode(5), TreeNode(1))

# Problem 2
def check_tree(root):
  #Check if a root has a value for its left and right children along with itself 
  return root.val == (root.left.val * root.right.val)
print(check_tree(tree))

# Problem 3
def check_tree_2(root):
  if not root or not root.left or not root.right:
      return False
  return root.val == (root.left.val * root.right.val)

tree = TreeNode(5, TreeNode(1), TreeNode(5))
print(check_tree_2(tree))

# Problem 4
def right_most(root):
  curr = root
  while curr.right:
      curr = curr.right
  return curr.val

tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
print(right_most(tree))

# Problem 5
def right_most_rec(root):
  if not root.right:
      return root.val
  return right_most_rec(root.right)

print(right_most_rec(tree))

# Problem 6
def postorder_traversal(root):
  list = []
  traverse(root, list)
  return list

def traverse(root, list):
  if not root:
      return list
  else:
      traverse(root.left, list)
      traverse(root.right, list)
      list.append(root.val)

print(postorder_traversal(tree))

# Problem 7
def product_tree(root):
  value = 1
  return product_traverse(root, value)

def product_traverse(root, value):
  if not root:
      return value
  else:
      l = product_traverse(root.left, value)
      r = product_traverse(root.right, value)
      value *= root.val * l * r 
  return value

tree2 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(product_tree(tree2))                                            
