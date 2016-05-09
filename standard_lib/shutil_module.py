import shutil
"""print((help(shutil))
print(shutil.get_terminal_size())
print(shutil.disk_usage("C:"))
"""
j=0
t=True
while  t==True:
    di=input("\nEnter valid disk letter >>eg d:")
    print("\nDisk information of drive <",di,">")
    for i in shutil.disk_usage(di):
    #print("usage in giga byte")
        if j==0:
            print("Total space: ",i/1000000000,"GB")
        elif j==1:
            print("Used space: ",i/1000000000,"GB")
        else:
            print("Free space :",i/1000000000,"GB")
        j+=1
