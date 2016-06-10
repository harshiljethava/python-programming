print("Enter your number")
num=int(input())
def digitadd(num):
	rem=int(0)
	while(num>0):
		rem+=num%10
		num=int(num/10)

	return rem

print("Addition of digit : ",digitadd(num))
