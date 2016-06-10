import sys,time
print(type(dir()))

for i in range(1,len(dir())):
    print("\n",i," :",dir(i[1]))
print("\n\nDirectory of sys: \n",dir(sys))
print("\n\nDirectory of time: \n",dir(time))
