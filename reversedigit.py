print("enter your number")
num=int(input())

def reversedigit(num):
	drev=int();rem=int()
	
	while(num>0):
		print(num)
		rem=num%10
		print("rem:",rem)
		drev=drev*10+rem
		num=int(num/10)

	return drev

print("Reverse of digit :,",reversedigit(num))

		
