print("How many number you want to sum ?")
num=int(input())
val=[]
def sumnum(num,val):
	sum=0
	i=0
	print(num)
	for i in range(num):
		print("Enter no ",i+1,":")
		j=int(input())
		val.insert(i,j)
		sum+=val[i]
		i+1
	return sum
		

print("Total Addition :",sumnum(num,val))
