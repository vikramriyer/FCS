#!/usr/bin/python

def sequential_search(alist, item):

  # method 1, pythonic way
  for i in alist:
    if item == i:
      return True

  # method 2, c way
  position = 0
  found = False
  while position < len(alist) and not found:
    if alist[position] == item:
      found = True
      break
    position += 1

  return found

def binary_search(alist, item):
  '''
  take three pointers
  start, mid, last
  if element < mid, recursively call alist[:mid]
  if element > mid, recursively call alist[mid+1:]

  some more conditions:
  if len(alist) is zero then return
  '''

  print "List is: {}".format(alist)
  start = 0
  last = len(alist) - 1

  if len(alist) == 0:
    return False
  else:
    mid = len(alist)/2
    if alist[mid] == item:
      return True
    else:
      if item < alist[mid]:
        return binary_search(alist[:mid], item)
      else:
        return binary_search(alist[mid+1:], item)

alist = [1, 5, 9, 11, 200, 201, 551]
print binary_search(alist, 551)