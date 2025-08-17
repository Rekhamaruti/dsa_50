#Monotonic array
def monotonic_array(array):
  n = len(array)
  if n == 0:return False #if the given array is empty
  first = array[0]
  last = array[n-1]
  if first > last:
    #monotonic decreasing
    for i in range(n-1):
      if array[i]<array[i+1]:return False
  elif first == last:
    for i in range(n-1):
      if array[i]!=array[i+1]:return False
  else:
    for i in range(n-1):
      if array[i]>array[i+1]:return False
      return False
  return True
