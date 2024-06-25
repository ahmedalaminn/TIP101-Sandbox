# UPI: understand, plan, implement 

# Problem 1: Pokemon Class
class Pokemon():
  def  __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp # hit points
    self.damage = damage # The amount of damage this pokemon does to its opponent every attack

  def attack(self, opponent):
    if (opponent.hp - self.damage <= 0):
      opponent.hp = 0
      print(opponent.name + 'fainted')
    else:
      opponent.hp -= self.damage
      print(self.name + ' dealt ' + str(self.damage) + ' damage to ' +  opponent.name)
    pass

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

# Problem 2: Convert to Linked List
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def create_linked_list(array):
  nodes = []
  for each_element in array:
    nodes.append(Node(each_element)) #Adds new node to nodes list
  #Create Linked List
  for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
  print_ll(nodes[0])

def print_ll(head):
  curr = head
  result = ""
  while curr:
    result += curr.value
    result += ' -> '
    curr = curr.next
  result += 'None'
  print(result)


def main():
  array = ["pikachu", "jigglypuff"]
  create_linked_list(array)

# Problem 3: Add First
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def add_first(head, new_node):
  temp = head
  head = new_node
  head.next = temp
  return head

node_1 = Node(1)
node_1.next = Node(2)
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

# Problem 4: Get Tail
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def get_tail(head):
  curr = head
  if head is None:
    return None
  else:
    while curr.next is not None:
      curr = curr.next
  return curr.value


# linked list: num1->num2->num3
num1 = Node("num1")
head = num1
head.next = Node("num2")
head.next.next = Node("num3")
tail = get_tail(num1)
print(tail)

# Problem 5: Replace Node
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def ll_replace(head, original, replacement):
  current = head
  while current:
    if current.value == original:
      current.value = replacement
    current = current.next

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
print(num1.value, num1.next.value, num1.next.next.value)

