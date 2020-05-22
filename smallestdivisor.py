print("enter your number")
num=int(input())

def smalldiv(num):
	i=int(1)
	print(num)
	for i in range(2,num+1):
		if ((num%i)==0):
			ans=i
			break
	return i

print("Smallest divisor of num ",smalldiv(num))
