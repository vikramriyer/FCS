#!/usr/bin/python

def get_pair_simple(arr, sum):
	'''Algo: consider key as first elem and iterate by checking over others'''
	for i in arr:
		for j in arr:
			if i + j == sum and arr.index(i) != arr.index(j):
				return i, j

def get_pair_hash(arr, sum):
	'''
	Algo:
	  if sum - elem of array in hash and hash[elem] == 1
	  	then return the elem and sum - elem i.e. the pair
	  else
		iterate
	'''
	#initialize hashmap

	elem_hash = [0]*100000

	for i in range(0, len(arr)):
		remainder = sum - arr[i]
		if remainder >= 0 and elem_hash[remainder] == 1:
			return remainder, arr[i]
		elem_hash[arr[i]] = 1

# Driver code to run the program
sum = 22
arr = [5, 10, 12, 25, 6]
a, b = get_pair_simple(arr, sum)
print a, b
a, b = get_pair_hash(arr, sum)
print a, b


def get_pair_bst():
	'''
		Algo: store the input in a bst, searching will take logn i.e. for each elem logn search time
		Hence, time complexity = O(nlogn)
	'''
	pass


'''
input: 5 10 12 25 6
sum: 22
expected o/p: 10 12

Implementations:
Basic key based search: O(n^2)
BST: O(nlogn)
Hash Table implementation: O(n) => if length of array is known
'''