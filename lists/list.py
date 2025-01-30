
# Change the second item:
list =  ["apple", "banana", "cherry"]
list[1] = "blackcurrent"
print(list)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:3] = ["blackcurrant", "watermelon"]
print(list)

#Change the second and third value by replacing it with one value:
list = ["apple", "banana", "cherry"]
list[1:3] = ["watermelon"]
print(list)

#insert Items
list = ["apple", "banana", "cherry"]
list.insert(2, "watermelon")
print(list)

#Append Items
list = ["apple", "banana", "cherry"]
list.append("orange")
print(list)

#Extend List
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove List Items
# The remove() method removes the specified item.

# Remove "banana":
list = ["apple", "banana", "cherry"]
list.remove("banana")
print(list)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:
# Remove the first occurrence of "banana":
list = ["apple", "banana", "cherry", "banana", "kiwi"]
list.remove("banana")
print(list)

# The pop() method removes the specified index.
# Remove the second item:
list = ["apple", "banana", "cherry"]
list.pop(1)
print(list)

#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


