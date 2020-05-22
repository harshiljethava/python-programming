print("enter number")
num=int(input())
primefac=[]
d=2
def findprime(num):
	global d
	while d*d <=num :
		while(num%d)==0:
			primefac.append(d)
			num//=d
		d=d+1
	
	if num>1:
		primefac.append(num)

	return primefac


print("\nPrime Factor : ",findprime(num)) 