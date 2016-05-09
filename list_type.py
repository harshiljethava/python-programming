os=["windows","linux","unix","solaris","android","mac","bsd","symbian","blackberry"]
print("sample list:",os)
print("Type of 'OS' list :",type(os))
print("os.insert('bada'):",os.insert(5,"bada"))
print(os)
os.append("Kali")
print(os)
linux_fav=["Ubuntu","Kubuntu"]
os.insert(7,linux_fav)
print("\n",os)
print(os[7])
print(os[7][0])
print(os[7][0][0])

print("os[-5][-1]:",os[-5][-1])
*directories, executable = "/usr/local/bin/gvim".split("/")
print(directories,"\n",executable)
print(type(directories))
print(type(executable))

os.reverse()
print(os)
os1=["windows","linux","unix","solaris","android","mac","bsd","symbian","blackberry"]
os1.sort()
print(os1)
os2=['a','b']
print(type(os2))
