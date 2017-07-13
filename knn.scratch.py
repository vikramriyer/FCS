import csv

with open('/home/vikram/Downloads/iris.data.txt','rb') as csvfile:
lines = csv.reader(csvfile)
for line in lines:
	print ', '.join(line)

'''
- load data
- split data into training and testing sets (67/33 randomly)
- 
'''

#References
#http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
#https://github.com/minsuk-heo/machinelearning/blob/master/machineLearningInAction/kNN.py