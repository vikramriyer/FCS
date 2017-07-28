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

def insert_sort(array):
    #step one, iterate through the array
    count = len(array)
    while  count != 0:
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
        count -= 1
    return array

print insert_sort([22,1, 0, 11, 9, 22,9,5,8,22,1,4])
print insert_sort(alist)
