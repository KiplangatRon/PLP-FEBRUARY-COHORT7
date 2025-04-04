# 1. Create an empty list
my_list = []

# 2. Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# 4. Extend with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Remove the last element
my_list.pop()

# 6. Sort in ascending order
my_list.sort() # (default), list already in ascending order

# 7. Find and print the index of 30
print(my_list.index(30))

# Optional: Print the final list to verify
print(my_list)
