my_set = {1, 2, 3, 'apple', 'banana', 'apple'}

# Access elements (Note: Sets are unordered, so indexing is not supported)
# print(my_set[0])  # This will raise a TypeError

# Add and remove elements
my_set.add('cherry')
print(my_set)

my_set.remove('banana')
print(my_set)

# Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))
print(set1.intersection(set2))