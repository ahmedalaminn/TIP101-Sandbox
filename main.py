# Problem 1
def can_place_flowers(flowerbed, n):
  if len(flowerbed) < n:
    return False

  i = 0
  while i + 1 <= len(flowerbed) and n > 0:
    if i == 0:
      if flowerbed[i] == 0 and flowerbed[i+1] == 0:
        flowerbed[i] = 1
        n -= 1
    elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
      flowerbed[i] = 1
      n -= 1
    i += 1

  if flowerbed[-1] == 0 and flowerbed[-2] == 0:
    flowerbed[-1] = 1
    n -= 1
  if n <= 0:
    return True
  return False

flowerbed = [1,0,0,0,1]
print(can_place_flowers(flowerbed, 1))
flowerbed = [1,0,0,0,1]
print(can_place_flowers(flowerbed, 2))
    
# Problem 2
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def reverse(head):
  current = head
  prev = None
  while current:
    nxt = current.next
    current.next = prev
    prev = current
    current = nxt
  return prev

def print_ll(head):
  while head:
    if head.next:
      print(head.value, end = '->')
    else:
      print(head.value)
    head = head.next


node_1 = Node(1, Node(2, Node(3, Node(4))))
print_ll(node_1)

new_head = reverse(node_1)
print_ll(new_head)

# Problem 3
def valid_word_abbreviation(word, abbr):
  word_index = 0
  abbr_index = 0

  while word_index < len(word) and abbr_index < len(abbr):
    if abbr[abbr_index].isdigit():
      if abbr[abbr_index] == '0':
        return False
      num = ''
      while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
        num += abbr[abbr_index]
        abbr_index += 1
      num = int(num)
      word_index += num
    else:
      if word[word_index] != abbr[abbr_index]:
        return False #makes sure they are in the same place index wise
      word_index += 1
      abbr_index += 1
  return word_index == len(word) and abbr_index == len(abbr)

word = "internationalization"
abbr = "i12iz4n"
print(valid_word_abbreviation(word, abbr))
word = "apple"
abbr = "a2e"
print(valid_word_abbreviation(word, abbr))
# alr gn 
#W, lowkey pulled that out my ass, glad it worked, nice working with yall, peace

# Problem 4
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def check_root_sum(root):
  def helper(root):
    if root is None:
      return 0
    return root.val + helper(root.left) + helper(root.right)
  sum = helper(root) - root.val

  return True if sum == root.val else False

root = TreeNode(14, TreeNode(4, TreeNode(3), TreeNode(1)), TreeNode(6))
print(check_root_sum(root))

# Problem 5
def max_area(height):
  maximum = 0
  left = 0
  right = 1
  while left < len(height):
    if right >= len(height):
      left += 1
      right = left + 1
    else:
      length = right - left 
      width = min(height[left], height[right])
      if maximum < length*width:
        maximum = length*width
      right += 1
  return maximum 
      
print(max_area([1,8,6,2,5,4,8,3,7]))
print(max_area([1,1]))