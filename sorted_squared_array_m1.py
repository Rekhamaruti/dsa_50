#sorted squared array - Brute force method
'''
You are given array of integers in which each subsequent value is not less than the previous value. 
Write a function that takes this array as an input and returns a new array with the squares of 
each number sorted in ascending order
'''
def squared_sorted(array):
  n =len(array)
  res = []*n
  for i in range(n):
    res[i]=array[i]**2
  res.sort()
  return res

