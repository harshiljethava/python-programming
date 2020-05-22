from datetime import date
s1_year = int(input("Enter year : "))
s1_month = int(input("Enter month :"))
s1_day = int(input("Enter day : "))
s1 = date(s1_year,s1_month,s1_day)
print(s1)

s2_year = int(input("Enter year : "))
s2_month = int(input("Enter month :"))
s2_day = int(input("Enter day : "))
s2 = date(s2_year,s2_month,s2_day)

print(s2)
if s2 < s1:
    raise ValueError(f"End date is small than start date")
else:
    days = s2-s1
    print("Days : ",days)
