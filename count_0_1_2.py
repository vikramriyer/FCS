#!/usr/bin/python

l = [2, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0]

expected_list = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2]

def method_1(l):

	zeros = l.count(0)
	ones = l.count(1)
	twos = l.count(2)

	actual_list = []

	for i in range(0, zeros):
		actual_list.append(0)

	for i in range(0, ones):
		actual_list.append(1)

	for i in range(0, twos):
		actual_list.append(2)

	return actual_list


#Driver Code

if method_1(l) == expected_list:
	print "The list is sorted correctly."
else:
	print "Incorrect sorting"