# find out what euclidean distance is and implement in python
'''

let's say X and Y are two points in 2d space with co-ordinates, X(x1, x2) and Y(y1, y2),
then the euclidean distance between the two points X and Y is calculated as:
dist = sqrt((x2-y2)^2 + (x1-y1)^2) 

so to generalize, if we have n dimensions
then ,

dist = sqrt(summation where i goes from i to n(xi-yi)^2)

'''
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import operator
import warnings
style.use('fivethirtyeight')

def euclidean_distance(vector1, vector2):
	if len(vector1) != len(vector2):
		print "Are you crazy? vectors are not valid!, exiting!"
		exit(0)
	dimensions = len(vector1)
	sum_of_the_squares = 0.0
	for i in range(dimensions):
		sum_of_the_squares += (vector1[i] - vector2[i])**2
	return sqrt(sum_of_the_squares)

train = {'k': [[1,2],[2,3],[3,1]], 'r': [[6,5],[7,7],[8,6]]}
test = [5,3]

def k_nearest_neighbors(data, predict, k=3):

	distance_point_map = {}
	if len(data) >= k: 
		warnings.warn('k is set to value less than total voters!')

	for group in data:
		for features in data[group]:
			distance = euclidean_distance(features, predict)
			distance_point_map[distance] = features

	sorted_map = sorted(distance_point_map.items(), key=operator.itemgetter(0))[:k]
	return [i[1] for i in sorted_map]

neighbors = k_nearest_neighbors(train, test)

color=5 #for closest points

[[plt.scatter(ii[0], ii[1], s=100, color='g') for ii in train[i]] for i in train]
for neighbor in neighbors:
	print neighbor, test
	plt.scatter(neighbor[0],neighbor[1], s=100, color='y')
plt.scatter(test[0],test[1],s=100, color='r')
plt.show()


# References
'''
http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
http://dataaspirant.com/2016/12/27/k-nearest-neighbor-algorithm-implementaion-python-scratch/
sentdex videos 13-19, python for machine learning
'''
