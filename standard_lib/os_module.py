import os
"""for i in dir(os):
    print(i)

print(help(os))"""
print("before :",os.getcwd())
print(os.getpid())
#os.system("mkdir jarvis")
os.chdir("c:/python34")
print("after:",os.getcwd())
for i in os.listdir():
    print(i)
