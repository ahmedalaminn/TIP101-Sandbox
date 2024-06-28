# UPI: understand, plan, implement

# Problem 1
def countdown(n):
  if n > 0:
    print(n)
    countdown(n - 1)

print("Problem 1")
countdown(5)
print()

def countdown_iterative(n):
  for i in range(n):
    print(n - i)

countdown_iterative(5)

# Problem 2
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)
  
print(fibonacci(6))

# Problem 3
def list_product(lst):
  if not lst: 
    return 1
  return lst[-1] * list_product(lst[:-1])

print(list_product([1, 2, 3, 4, 5]))

# Problem 4
def is_power_of_four(n):
  if n == 1:
    return True
  return is_power_of_four(n // 4) if n % 4 == 0 else False

print(is_power_of_four(16))

# Problem 5
def binary_search_recursive(arr, target, left, right):
  if left > right:
      return -1  # Base case: target not found within bounds

  # find middle index of list
  mid = (left + right) // 2

  # If the middle element is the target, return its index
  if arr[mid] == target:
      return mid
  # If the target is less than the middle element, search the left half
  elif arr[mid] > target:
      return binary_search_recursive(arr, target, left, mid - 1)
  # If the target is greater than the middle element, search the right half
  else:
      return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_iterative(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    middle = (left + right) // 2
    if arr[middle] == target:
      return middle
    elif arr[middle] > target:
      right = middle - 1
    else:
      left = middle + 1
  return -1
  
print(binary_search_iterative([1, 3, 5, 7, 9, 11, 13, 15], 5))

# Time complexities for both recursive and iterative is O(log n). Space complexity for iterative is O(1), for recurive is O(log n)

# Problem 6
def find_ceiling(lst, x):
  if lst[-1] <= x:
    return lst[-1]
  return find_ceiling(lst[:-1], x)

print(find_ceiling([1, 3, 5, 7, 9, 10, 13, 15], 11))
