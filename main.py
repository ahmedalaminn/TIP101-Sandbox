# Problem 1
from collections import defaultdict

def is_valid(s):
  hashmap = {')': '(', '}': '{', ']': '['}
  stack = []
  for i in s:
    if i in hashmap:
      if hashmap[i] != stack.pop():
        return False
    else:
      stack.append(i)

  if not stack:
    return True
  
  return False
  
s = "()"
print(is_valid(s))
s = "()[]{}"
print(is_valid(s))
s = "()[]{}"
print(is_valid(s))
s = "(]"
print(is_valid(s))

# Problem 2
def max_profit(prices):
  slow = 0 
  fast = slow + 1
  max_profit = 0
  
  while slow < len(prices):
    if fast >= len(prices):
      slow += 1
      fast = slow + 1
    else:
      if prices[fast] > prices[slow] and prices[fast] - prices[slow] > max_profit:
        max_profit = prices[fast] - prices[slow]
      fast += 1

  return max_profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))
prices = [7,6,4,3,1]
print(max_profit(prices))

# Problem 3
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def shuffle_merge(head_a, head_b):
  start_node = Node(value = None)
  current = start_node
  
  while head_a and head_b:
    current.next = head_a
    head_a = head_a.next
    current = current.next

    current.next = head_b
    head_b = head_b.next
    current = current.next

  if head_a:
    current.next = head_a

  if head_b:
    current.next = head_b

    
  return start_node.next
  
root1 = Node(1)
root1.next = Node(2)
root1.next.next = Node(3)
root2 = Node(4)
root2.next = Node(5)
root2.next.next = Node(6)

new_node = shuffle_merge(root1, root2)
current = new_node
while current.next:
  print(current.value, end = "->")
  current = current.next
print(current.value)

# Problem 4
def group_anagrams(strs):
  res = defaultdict(list)

  for word in strs:
    hashmap = [0] * 26

    for character in word:
      if character in hashmap:
        hashmap[ord(character) - ord('a')] += 1
      else:
        hashmap[ord(character) - ord('a')] = 1

    res[tuple(hashmap)].append(word)
     
  return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
lst = group_anagrams(strs)
res = []
for i in lst:
  res.append(i)
print(res)

strs = [""]
lst = group_anagrams(strs)
res = []
for i in lst:
  res.append(i)
print(res)

strs = ["a"]
lst = group_anagrams(strs)
res = []
for i in lst:
  res.append(i)
print(res)

# Problem 5
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def sum_numbers(root):
  lst = []
  def dfs(root, string = ''):
    if root is None:
      return lst.append(string) #yeppp!!
    else:
      string += str(root.val) 
    dfs(root.left, string)
    dfs(root.right, string)
    
  dfs(root)
  return sum(int(path) for path in lst) // 2
# the problem can be fixed with just halving!!!!! lmaaaao ig that works hahahhaa goodnight! goodnight
# lets go!! Thanks guys!
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sum_numbers(root))

root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
root.right = TreeNode(0)
print(sum_numbers(root))