import time

def generator():
    ntime = time.time_ns()
    ntime_len = int(len(str(ntime)))
    print("ntime : ",ntime)
    otp = str(int(ntime)/(ntime_len * ntime_len))
    otp = otp.split('.')[0][-6:]
    print("ntime len : ",ntime_len)
    print("otp : ", otp)

generator()

#print("result : ",result)