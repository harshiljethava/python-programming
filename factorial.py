print("Enter your number")
num=int(input())
ans=1
def fact(num):
	global ans
	for i in range(num):
		if(num>1):
			
			ans=num*fact(num-1)
		else:
			return 1

	return ans

fact(num)
print("Factorial :",ans)