
def fun1(number):
	def fun2():
		flag = False
		if number % 2 == 0:
			flag = True
		return flag
	return fun2

r1 = fun1(10)
print "The number is even" if r1() else "The number is odd"