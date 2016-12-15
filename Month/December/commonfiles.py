import os

one=os.listdir("./1/")
two=os.listdir("./2/")

print list(set(two) - set(one))