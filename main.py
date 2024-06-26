# UPI: understand, plan, implement 

# Problem 1: Nested Constructors
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

head = Node(4,Node(3,Node(2)))
print(head.value)
print(head.next.value)
print(head.next.next.value)

# Problem 2: Find Frequency
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def count_element(head, val):
  current = head
  counter = 0
  while current:
    if current.value == val:
      counter += 1
    current = current.next
  return counter

head = Node(3,Node(1,Node(2,Node(1))))
print(count_element(head, 1))

# Problem 3: Remove Tail
class Node:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next


# Helper function to print the linked list
def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()


# I have a bug! 
def remove_tail(head):
  if head is None: # If the list is empty, return None
      return None
  if head.next is None: # If there's only one node, removing it leaves the list empty
      return None 

# Start from the head and find the second-to-last node
  current = head
  while current.next.next: 
      current = current.next

  current.next = None # Remove the last node by setting second-to-last node to None
  return head

head = Node(1,Node(2,Node(3,Node(4))))
remove_tail(head)

# Problem 4: Find the Middle
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
  if not head:
    return False

  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if fast.next is None:
      return slow.value
    else:
      return slow.next.value

head = Node(1,Node(2,Node(3,Node(4))))
print(find_middle_element(head))

# Problem 5: Is Palindrome?
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
  left = head
  current = head
  length = 1
  while current.next:
    current = current.next
    length += 1
  right = current #tail

  while left != right: 
    if left.value != right.value:
      return False
    else:
      # reassign right node
      i = length - 1
      curr = head
      right = head
      while i >= 0:
        right = curr.next
        i -= 1
      # reassign left node 
      left = left.next  
  return True

head = Node(1,Node(2,Node(1)))
print(is_palindrome(head))

head = Node(1,Node(2,Node(2)))
print(is_palindrome(head))

# Problem 6: Put it in Reverse
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
  left = head
  current = head
  length = 1
  while current.next:
    current = current.next
    length += 1
  right = current

  while left != right and right.next != left:
    left.value, right.value = right.value, left.value
    # reassign right node
    i = length - 1
    curr = head
    right = head
    while i >= 0:
      right = curr.next
      i -= 1
    # reassign left node 
    left = left.next

  return head

head = Node(1,Node(2,Node(3,Node(4))))
reverse(head)
print_list(head)

