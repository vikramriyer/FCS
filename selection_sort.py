def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

def select_sort(array):
    #step one, iterate through the array
    count = len(array)
    while  count != 0:
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
        count -= 1
    return array

print select_sort([22,1, 0, 11, 9, 22,9,5,8,22,1,4])
print select_sort(alist)

