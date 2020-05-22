import math, random
def generator():
    digit = str(random.random())
    digit = digit.split('.')
    print("digit : ",digit)
    for i in range(len(digit)):
        otp = digit[1][-4:]
        return otp


result = generator()
print("OTP : ", result)
