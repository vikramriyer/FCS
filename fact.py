#!/usr/bin/python

def fact_rec(num):
  if num == 1:
    return num
  else:
    return num * fact(num-1)

def fact_ite(num):
  fact = 1
  fives = 0
  for i in range(num):
    fact *= i+1
  return fact

def primes(n):
  primfac = []
  d = 2
  while d*d <= n:
    while (n % d) == 0:
      primfac.append(d)  # supposing you want multiple factors repeated
      n //= d
    d += 1
  if n > 1:
    primfac.append(n)
  return primfac

def total_pairs(twos, fives):
  if twos < fives and twos != 0:
    value = twos
  elif twos >= fives and fives != 0:
    value = fives
  return value

var = fact_ite(100)
#print "Factorial: " + str(var)
prime_facs = primes(var)
twos = prime_facs.count(2)
fives = prime_facs.count(5)

print "No of trailing zeros: {}".format(total_pairs(twos, fives))