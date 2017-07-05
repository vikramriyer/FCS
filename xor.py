#!/usr/bin/python

def xor_n_square(l):
  x = {}
  for elem in l:
    if l.count(elem) > 1:
      x[elem] = str(l.count(elem)) + " times"
  print "Occurances of elements in the list are as shown below: \n{}".format(x)

def xor_n_logn(l):
    
  l.sort()

  #method 1
  x = set(l)
  
  if len(l) != len(x):
    print "duplicates exist"

  #method 2
  for i in range(0, len(l) - 2):
    xor = l[i] ^ l[i+1]
    if xor == 0:
      print "duplicates found"
      exit(0)

def xor_n(l):
  pass

l = [0, 1, 0, 7, 4, 4, 6]
xor_n_square(l)
#xor_n_logn(l)
#xor_n(l)