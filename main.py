# Problem 1
def climb_stairs(n):
  if n == 0 or n == 1:
    return 1
  else:
   return climb_stairs(n-2) + climb_stairs(n-1)

print(climb_stairs(2))

# Problem 2
def find_error_nums(nums):
  i = 0
  j = 1
  while j < len(nums):
    if nums[i] == nums[j]:
      return [nums[i], nums[j] + 1]
    i += 1
    j += 1

print(find_error_nums([1,1]))

# Problem 3
class Node:
  def __init__(self, val=0, next=None):
      self.value = val
      self.next = next

def delete_nodes(head, m, n):
  curr = head
  prev = curr
  M = 0 # keeping
  N = 0 # deleting
  while curr.next:
    while curr.next and M < m:
      M += 1
      prev = curr
      curr = curr.next 

    while curr.next and N < n:
      N += 1
      curr = curr.next

    prev.next = curr
    M = 0
    N = 0
  return head
  
head = Node(1)
curr = head
i = 2
while (i <= 13):
  curr.next = Node(i)
  curr = curr.next
  i += 1

def printlink(head):
  curr = head
  while curr:
    if not curr.next: 
      print(curr.value)
    else:
      print(curr.value, end = "->")
    curr = curr.next

printlink(head)
head = delete_nodes(head, 2, 3)
printlink(head)

# Problem 4
class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right
    
def get_diameter(root):
  diameter = 0
  def dfs(root):
    nonlocal diameter
    if not root:
      return 0
    left = dfs(root.left)
    right = dfs(root.right)
    diameter = max(diameter, left + right)
    return max(left, right) + 1
    
  return dfs(root)
    

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(get_diameter(root))
#     1
#    / \
#   2   3
#  / \  
# 4   5

# Problem 5
def two_sum(numbers, target):
  left = 0
  right = left + 1
  while left < len(numbers):
    if right >= len(numbers):
      left += 1
      right = left + 1
    if numbers[left] + numbers[right] == target:
      return [left, right]
    right += 1

print(two_sum([1,2,3,4], 3))
