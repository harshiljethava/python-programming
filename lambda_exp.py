atom=[(2,4.00,"Helium"),(1,1.0,"Hydrogen"),
      (3,6.94,"Lithium"),(4,9.012,"Beryllium"),(5,10.81,"Boron")]
print("atom collections:",atom)
print(type(atom))
print("after using atom.sort():",atom.sort())
print(atom)
print("""with sort() method it is not possible to sort given list by name or
any other index position ,for that we have to make custom fun for this but
making custom fun is not ultimate solution ,for better result
we can use lambda expression  """)

#key=lambda l:(l[1],l[2])
atom.sort(key=lambda l:(l[2]))
print("\nusing lambda fun for sorting atom by index 2\n",atom)
print("\nlambda with silcing\n")
atom.sort(key=lambda l:(l[1:2]))
print(atom)

area=lambda b,h:(b*h*.5)
print("enter 2 int or float for area() fun:")
b=int(input())
h=int(input())
print(area(b,h))
