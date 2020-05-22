import math,random

def generator():
    string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    otp = ""
    for i in range(6):
        otp += random.choice(string)
    return otp

result = generator()
print("OTP : ",result)