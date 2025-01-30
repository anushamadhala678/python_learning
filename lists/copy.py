# You can use the built-in List method 'copy()' to copy a list.
list = ["apple", "banana", "cherry"]
mylist = list.copy()
print(mylist)

# Another way to make a copy is to use the built-in method 'list()'.
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
list = thislist[:]
print(mylist)