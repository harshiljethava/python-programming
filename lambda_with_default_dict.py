import collections
print("Lambda with default dict")
print("""what happen when we  access default dictionary with non existing key ,
it will create suitable item with given key,
same thing can be possible with lambda fun too !""")

account_bal=collections.defaultdict(lambda:"no balance in this account")
print("account_bal[4]:",account_bal[4])
account_bal[3]=1000
print("account_bal[3]:",account_bal[3],"RS")
