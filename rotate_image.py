#!/usr/bin/python

init_list = [[1,2,3],[4,5,6],[7,8,9]]

def rotate_matrix(matrix):
	'''Algo: 
	   	First: take transpose of the matrix
		Second: interchange row 0 and row 2
	'''

	matrix = zip(*matrix)
	return swap_rows(matrix)

def swap_rows(matrix):
	print matrix	
	row0, row2 = matrix[0], matrix[2]

	matrix[0] = row2
	matrix[2] = row0

	return matrix 

final_matrix = rotate_matrix(init_list)
print final_matrix

