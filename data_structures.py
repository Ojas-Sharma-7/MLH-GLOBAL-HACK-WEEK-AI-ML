# Creating a List with
# the use of multiple values
List = ["GHW", "For", "ML"]
print("\nList containing multiple values: ")
print(List)

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List2 = [['GHW', 'For'], ['AI']]
print("\nMulti-Dimensional List: ")
print(List2)

# accessing a element from the
# list using index number
print("Accessing element from the list")
print(List[0])
print(List[2])

# accessing a element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])


# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'GHW', 4, 'For', 6, 'MLH'])
print("\nSet with the use of Mixed Values")
print(Set)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
	print(i, end =" ")
print()

# Checking the element
# using in keyword
print("Geeks" in Set)

String = "Welcome to GHW AI/ML from MLH"
print("Creating String: ")
print(String)

# Printing First character
print("\nFirst character of String is: ")
print(String[0])

# Printing Last character
print("\nLast character of String is: ")
print(String[-1])
