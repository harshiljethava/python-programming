print("custom exception")
class FoundException(Exception):pass
found=False
try:
 for row,record in enumerate(record):
    for index,item in enumerate(field):
        if item== target:
            found=True
            raise FoundException()
except FoundException():
   print("found at({0},{1},{2}).format(row,column,index)")
""" break
        if found:
            break
    if found:
        break
if found:
 
else:
    print("not found")
"""
