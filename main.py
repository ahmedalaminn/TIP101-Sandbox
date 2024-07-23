class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right
     
# Problem 1
def is_univalued(root):
  if not root:
    return False
    
  root_val = root.val
  
  def dfs(root):
    if not root:
      return True
    elif root.val != root_val:
      return False
    else:
      return dfs(root.left) and dfs(root.right)

  return dfs(root)

root = TreeNode(5, TreeNode(5, TreeNode(5)), TreeNode(5))
print(is_univalued(root))

# Problem 2
def height(root):
  if not root:
    return 0
  return 1 + max(height(root.left), height(root.right))

print(height(root))

# Problem 3
class TreeNode():
   def __init__(self, key, value, left=None, right=None):
       self.key = key
       self.val = value
       self.left = left
       self.right = right

def insert(root, key, value):
  if root:
    if key > root.key:
      if root.right:
        return insert(root.right, key, value)
      else:
        root.right = TreeNode(key, value)
    elif key < root.key:
      if root.left:
        return insert(root.left, key, value)
      else:
        root.left = TreeNode(key, value)
    else:
        root.val = value
  return root

root = TreeNode(10, 'Ahmed', TreeNode(9, 'Cat'), TreeNode(11, 'Dog'))
insert(root, 10, 'Zhanna')
print(root.val)

# Problem 4
def remove_bst(root, key):
  
  def inorder_successor(root):
    curr = root
    while curr.left: 
      curr = curr.left
    return curr

  if root is None:
    return root
  elif key < root.key:
    root.left = remove_bst(root.left, key)
  elif key > root.key:
    root.right = remove_best(root.right, key)
  else:
    # Case 1: Node with no children (leaf node)
    if root.left is None and root.right is None:
        return None
    # Case 2: Node with only one child
    elif root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    # Case 3: Node with two children
    else:
        temp = inorder_successor(root.right)
        root.key = temp.key
        root.right = remove_bst(root.right, temp.key)
      
    return root

# Problem 5
def inorder_successor(root, current):
  if current:
    return None
  elif current.right: # if node has right subtree
    curr = current.right
    while curr.left: 
      curr = curr.left
    return curr
  else: # if node doesn't have right subtree
    inorder_successor = None
    curr = root
    while curr != current:
      if curr.key > current.key:
        inorder_successor = curr
        curr = curr.left
      else:
        curr = curr.right
        
    return curr

# Problem 6
def merge_trees(self, root1, root2):
  if not root1 and not root2:
    return None
  elif not root1: 
    return root2
  elif not root2: 
    return root1
  else:
    merged = TreeNode(root1.val + root2.val)
    merged.left = merge_trees(root1.left, root2.left)
    merged.right = merge_trees(root2.right, root2.right)
  return merged
    

    
