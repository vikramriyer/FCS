#!/usr/bin/python

'''
Solution: Update a new matrix with the cumulative sum of previous positions

Algo: 
if i - 1 < 0 and j - 1 < 0 i.e. no rows and columns before current one, keep the value as it is 
if i - 1 < 0, no rows before current one, current value to be updated with a[i][j] + a[i, j-1] value
if j - 1 < 0, no cols before current one, current value to be updated with a[i][j] + a[i-1, j] value
else current value to be updated with max(a[i-1, j], a[i][j-1])
'''

matrix = [
  [1, 5, 1, 7],
  [4, 2, 3, 8],
  [10, 1, 1, 9],
  [4, 0, 6, 0]
]
'''
matrix = [
  [1, 5],
  [4, 2]
]
'''

nrows = len(matrix)
ncols = len(matrix[0])

def max(x, y):
  if x >= y:
    return x
  else:
    return y

print matrix

for i in range(0, nrows):
  for j in range(0, ncols):
    print i, j
    if i - 1 < 0 and j - 1 < 0:
      continue
    elif i - 1 < 0:
      matrix[i][j] += matrix[i][j-1]
    elif j - 1 < 0:
      matrix[i][j] += matrix[i-1][j]
    else:
      matrix[i][j] += max(matrix[i-1][j], matrix[i][j-1])

print "The max possible value is: {}".format(matrix[nrows-1][ncols-1])