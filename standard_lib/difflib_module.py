import difflib
print(difflib)
sd1="This is sample string one for difflib"
sd2="life is awsome"
print(difflib.get_close_matches("is",sd1,n=20,cutoff=.25))
