import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
indices = np.where(array1 == search_value)[0]
print(indices)
# Count occurrences in array1
count = 0
for i in range(len(array1)):
	if array1[i] == count_value:
		count+=1
#count = list(array1).count(count_value)
#count = sum(array1 == count_value)
print(count)
# Broadcasting addition
broad = array1 + broadcast_value
print(broad)

# Sort the first array
print(np.sort(array1))