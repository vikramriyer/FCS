def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
#insertionSort(alist)
#print(alist)


'''
Alogrithm:

    at any point, the LHS should be smaller than the element and RHS should be greater than the element
    Questions:
    1. where to start, i.e. the position in an array
    2. 

'''

