'''
to_21 = [i for i in range(1, 22)]
print to_21

odds = to_21[::2]
print odds

middle_third = to_21[len(to_21)/3:len(to_21)-(len(to_21)/3)]
print middle_third

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

print ~88

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item


def is_int(x):
    return True if x == int(x) else False

print is_int(7.2)


def factorial(x):
    fact = 1
    while x != 1:
        fact = fact * x
        x -= 1
    return fact

print factorial(5)

def median(lst):
    lst.sort()
    print lst
    mid1 = lst[len(lst)/2-1]
    if len(lst) % 2 == 0:
    	mid1 = lst[len(lst)/2-1]
    	mid2 = lst[len(lst)/2]
    	if mid1 != mid2:
        	return (float(mid1) + mid2) / 2
    else:
    	mid1 = lst[len(lst)/2]
    return mid1

#print median([6, 8, 12, 2, 23])

def is_narcissistic(num):
	pass

board = [['0']*5]*5

print board
board = []

for i in range(5):
    board.append(['0'] * 5)

print board
def reverse(text):
    rev = ''
    for i in range(len(text)-1, -1, -1):
        rev += text[i]
    return rev

print reverse("abc")

def anti_vowel(text):
    text = text.replace('a','')
    text = text.replace('A','')
    text = text.replace('e','')
    text = text.replace('E','')
    text = text.replace('o','')
    text = text.replace('O','')
    text = text.replace('i','')
    text = text.replace('I','')
    text = text.replace('u','')
    text = text.replace('U','')
    
    return text


print anti_vowel("Hey You!")

f = open('/data/GATE-2018/FOCUS/file2.txt','w')
x = (1,2)
f.write(str(x))
f.close()

f = open('/data/GATE-2018/FOCUS/file1.txt','r')
print f.read()
print '****'
f.seek(0)
print f.read()
f.close()
'''
import os

#print os.getcwd()
#print os.listdir(os.getcwd())
#print '****************************'
#print [i for i in os.walk(os.getcwd())]
print os.stat('/home/data/GATE-2018/FOCUS/.git')
#print dir(os)
