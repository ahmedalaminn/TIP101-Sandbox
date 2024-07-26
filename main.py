from collections import deque
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
# Problem 1
def is_symmetric(root):
  if root is None:
    return True
    
  queue = deque([(root.left, root.right)])
  while queue:
    left, right = queue.popleft()
    if not left and not right:
      continue
    if not left or not right or left.val != right.val:
      return False

    queue.append((left.left, right.right))
    queue.append((left.right, right.left))

  return True


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(is_symmetric(root))
#       1
#     /   \
#    /     \
#   2       2
#  / \     / \
# 3   4   4   3

# Problem 2
def binary_tree_paths(root):
  paths = []

  def dfs_helper(node, path):
    if node is not None:
      path.append(node.val)
      if not node.left and not node.right:
        paths.append(list(path))
      else:
        dfs_helper(node.left, path)
        dfs_helper(node.right, path)
      path.pop()

  dfs_helper(root, [])
  return paths

print(binary_tree_paths(root))


# Problem 3
def min_diff_in_bst(root):
  def dfs(root, values):
    if not root:
      return values
    values.append(root.val)
    dfs(root.right, values)
    dfs(root.left, values)
    
  values = []
  dfs(root, values)
  
  values = sorted(values)
  min_diff = float('inf')
  for i in range(len(values) - 1):
      diff = abs(values[i + 1] - values[i])
      if diff < min_diff:
          min_diff = diff
  return min_diff


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(48)
root.right.left = TreeNode(12)
root.right.right = TreeNode(49)
print(min_diff_in_bst(root))

# Problem 4
def increasing_bst(root):
  def inorder(node, values):
      if not node:
          return
      inorder(node.left, values)
      values.append(node.val)
      inorder(node.right, values)

  values = []
  inorder(root, values)
  
  root = TreeNode(values[0])
  curr = root

  for val in values[1:]:
      curr.right = TreeNode(val)
      curr = curr.right
  return root

new_root = increasing_bst(root)

curr = new_root
while curr:
  print(curr.val, end = ' ')
  curr = curr.right
print()

# Problem 5
def can_split(root):
  def dfs_counter(root):
    if root is None:
      return 0
    return 1 + dfs_counter(root.left) + dfs_counter(root.right)

  return dfs_counter(root.left) == dfs_counter(root.right)
  
root = TreeNode(1)
root.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right = TreeNode(48)
root.right.right = TreeNode(49)
print(can_split(root))

  
    
