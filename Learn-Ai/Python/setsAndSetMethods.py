# Declaration on Sets
a1 = {3, 4, 5, 5, 5, 5, 5, 5, 5}
a2 = {3, 23, 5}
print(a1) # {3, 4, 5}
print(a2) # {3, 23, 5}

# Set methods
# print(a1.clear()) # set()
# Uncomment this line if you want to remove everything from a1 👆
print(a1.pop()) # Return a random element from the set
print(a1.add(2)) # Add a new element to the set
print(a1.union(a2)) # Add every element that is in a2 and is not in a1 to a1
print(a1.intersection(a2)) # Print the list of common elements in the two sets

"""
To understand all the methods of sets in Python, please learn about set theory in Mathematics
	                                    (◕‿◕)
"""
