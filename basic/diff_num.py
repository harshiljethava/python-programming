number = int(input("enter n : "))
if number > 17 :
    temp = number - 17
    temp = temp * 2
    print("result : ",temp)
else:
    temp = abs(number - 17)
    print("result : ",temp)
