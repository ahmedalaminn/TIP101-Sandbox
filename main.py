# Problem 1: Hello Hello
def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)

def repeat_hello_iterative(n):
  while n > 0:
    print("Hello")
    n -= 1

repeat_hello_iterative(5)
repeat_hello(5)

# Problem 2: Factorial Cases 
def factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))

# Problem 3: Recursive Sum
def sum_list(lst):
  if not lst:
    return 0
  else:
    return lst[0] + sum_list(lst[1:])
    
print(sum_list([1,2,3,4,5]))

#Problem 4: Recursive Power of 2
def is_power_of_two(n):
  if n == 1:
    return True
  else:
    return is_power_of_two(n/2) if n%2 == 0 else False
      
print(is_power_of_two(63))

#Problem 5: Binary Search I
def binary_search(lst, target):
  left = 0
  right = len(lst) - 1
  while left <= right:
    middle = (left+right) // 2
    if lst[middle] == target:
      return middle
    elif lst[middle] < target:
      left = middle + 1
    else:
      right = middle - 1
  return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10], 7))

