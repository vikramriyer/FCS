# This program uses Greedy programming paradigm to solve the knapsack problem

# profit greedy (max profit)

# greedy about weights (least weight)

# greedy about profit/weight, scale the values
# i.e. what is the value per unit for each object
# there is a catch here that, the object even though having max profits, can't be placed fully because knapsack size may be more than the objects size, hence we place that obj completely and if there is place, we try to fit the next max one and so on

# where is it applicable in real world
# lets say you want to transmit some object over the internet and there are limited number of packets available, but sufficient to send your data, but your data has to be transmitted in chunks because entire data size is greater than packet size, in this case, initially you will break the data into the max size that can fit the packet and send it, and lastly the smaller chunk will be sent => internet download manager uses this concept

# implementation ALGO
'''
1. take the input in the format,
dict of tuples where dict key is the object name/number/id and values are list of [profit, weight], the size of the knapsack
2. for each object, find the profit/weight ratio and append to the list,
so now the list will look like [profit, weight, profit/weight]
3.1 first fit the object having max p/w ratio
    - if knapsack size is less than no of objects, split and fit
    - if knapsack size is equal, fit
    - if knapsack size is less, fit and go to next largest(p/w) object
    - repeat until the knapsack is full and finally print the profit
4. profit calculation formula: P += p(p/w)
'''
import operator

def calculate_profit(data, object_profit_by_weight_map, knapsack_size):

	profit = 0.0
	sorted_object_profit_by_weight_map = sorted(object_profit_by_weight_map.items(), key=operator.itemgetter(1), reverse=True)

	for object in sorted_object_profit_by_weight_map:
		
		object = object[0]

		if knapsack_size == 0:
			print "Knapsack is now full!"
			return profit
		elif knapsack_size < data[object][1]:
			profit += object_profit_by_weight_map[object]*knapsack_size
			knapsack_size = 0
		elif knapsack_size == data[object][1]:
			profit += data[object][0]
			knapsack_size -= 0
		else:
			profit += data[object][1]*object_profit_by_weight_map[object]
			knapsack_size -= data[object][1]
	return profit

def calculate_profit_by_weight(data):
	object_profit_by_weight_map = {}
	for object in data:
		profit_by_weight = round(data[object][0]/float(data[object][1]), 2)
		object_profit_by_weight_map[object] = profit_by_weight
	return object_profit_by_weight_map

def knapsack(data, knapsack_size):
	
	# calculate the profit/weight for each object and store in data
	object_profit_by_weight_map = calculate_profit_by_weight(data)

	# fit the knapsack with apt object to maximiza the profit and return the profit
	print calculate_profit(data, object_profit_by_weight_map, knapsack_size)

def main():
  
  #create the input
  input = {'1': [10, 2], '2': [5, 3], '3': [15, 5], '4': [7, 7], '5': [6, 1], '6': [18, 4], '7': [3, 1]}
  knapsack_size = 15
  knapsack(input, knapsack_size)

if __name__ == "__main__":
  main()
