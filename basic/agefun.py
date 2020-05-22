def person(name,age):
	print("name: ",name)
	print("age : ",age)

def varfun(*args):
	for i in args:
		print(i)

def cal(a,b):
	add = a + b
	sub = a - b
	avg = (a + b)/2
	return add ,sub,avg



