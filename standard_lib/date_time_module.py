from datetime import date
now=date.today()
print(date.today())
dob_en=input("enter your birth date in yyyy-m-dd format eg.1995-2-13")
dob_en=dob_en.split("-")
"""for i in dob_en:
    i=int(i)
    print(i)
    print("value of ",i,": ",type(i))
 """   
dob=date(int(dob_en[0]),int(dob_en[1]),int(dob_en[2]))
age=now-dob
print("Date of birth: ",dob)
print("Today`s date:",now)
print("Age in days:",age)

