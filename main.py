# UPI: understand, plan, implement 

# Problem 1: Prime Number
def is_prime(n):
  count = 2
  
  while count < n:
    if n % count == 0:
      return False
    count += 1

  return True

   
print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
  
# Two-Pointer Reverse List
def reverse_list(lst):
  pointer1 = 0
  pointer2 = len(lst) - 1
  while (pointer1 < pointer2):
    lst[pointer1],lst[pointer2] = lst[pointer2],lst[pointer1]
    
    pointer1 += 1
    pointer2 -= 1
    
  return lst
print(reverse_list([1,2,3,4,5]))

# Problem 3: Evaluating Solutions
  # two pointer solution has same time complexity as list slicing solution
  # two pointer solution has better space complexity then list slicing solution

# Problem 4: Move Even Integers
def sort_array_by_parity(nums):
  l = 0
  r = len(nums) - 1
  while (l < r):
    if (nums[l] % 2 != 0 and nums[r] % 2 == 0):
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
      r -= 1
    if nums[l] % 2 == 0:
      l += 1
    if nums[r] % 2 != 0:
      r -= 1 
  return nums
nums = [3,1,2,4]
nums2 = [1,2,3,4,5,6,7,8,9,10]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

# Problem 5: Palindrome
def first_palindrome(words):
  for word in words:
    if isPalindrome(word):
      return word
  return ''
  
def isPalindrome(word):
  i = 0
  j = len(word) - 1
  while i < j:
    if word[i] != word[j]:
      return False
    i += 1
    j -= 1
  return True
  
words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

# Problem 6: Remove Duplicates with O(1)
def remove_duplicates(nums):
  pointer1 = 0
  pointer2 = 1
  while pointer2 < len(nums):
    if (nums[pointer1] == nums[pointer2]):
      del nums[pointer2]
    else:
      pointer1 += 1
      pointer2 += 1
  return nums

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) 

