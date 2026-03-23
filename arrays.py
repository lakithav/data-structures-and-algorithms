from array import *

arr = array('i', [1, 2, 3, 4, 5])
print(arr)


# Adding an element to the end of the array
arr.append(12)
print(arr)

# Inserting an element at a specific position
arr.insert(1,10)
print(arr)

# Extending the array with another array
arr.extend([6, 7, 8])
print(arr)

for i in arr:
    print(i)


# Removing an element from the array
arr.remove(3)
print(arr)

# Removing an element at a specific position
arr.pop(1)
print(arr)