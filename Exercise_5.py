# PYTHON COLLECTIONS

# Create a list fruits = ["apple", "banana", "cherry"] .
    # Print the first fruit.
    # Replace "banana" with "orange"
    # Print the length of the list
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[1]="orange"
print(fruits)
print(len(fruits))



# Create a list of numbers from 1 to 10 .
    # Print the first three numbers using slicing
    # Print the last three numbers using slicing
list=[1, 6, 8, 32, 13, 9, 11]
print(list[0:3])
print(list[-3:])



# Start with numbers = [5, 2, 9, 1, 7] and do the following:
    # Sort the list in ascending order
    # Append the number 10 to the list
    # Remove the number 2 from the list
list=[5, 2, 9, 1, 7]
list.sort()
print(list)
list.append(10)
print(list)
list.pop(1)
print(list)



# Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1 .
names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names)



# Create a tuple coordinates = (10, 20) and print both elements
coordinates = (10, 20)
print(coordinates)


# Try to modify the tuple by setting coordinates[0] = 50 — note what happens
coordinates[0]=50 # 'tuple' object does not support item assignment.



# Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple
coordinates=list(coordinates)
print(coordinates)
coordinates=tuple(coordinates)
print(coordinates)



# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3 ?)
my_set = {1, 2, 3, 3, 4}
print(my_set) # It do not print the repeated value 3, which was assigned in the set initially.

# Add 5 to the set, remove 2 , and check if 4 is in the set
my_set.remove(2)
my_set.add(5)
print(my_set)



# Create two sets:
    # a = {1, 2, 3}
    # b = {3, 4, 5}
    # Find their:
        # Union
        # Intersection
        # Difference ( a - b )
a = {1, 2, 3}
b = {3, 4, 5}
c=a.union(b)
print(c)
c=a.intersection(b)
print(c)
c=a-b
print(c)



# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
    # Print the value of "name" .
    # Change "grade" to "A+" .
    # Add a new key "city" with value "Delhi"
student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"]="A+"
print(student)
student["city"]="Delhi"
print(student)



# Create a dictionary of three friends and their phone numbers. Use:
    # keys() to get all names
    # values() to get all numbers
    # items() to loop over key-value pairs and print them
friends={"Ashish":"4192", "Brijesh": "2165", "Harish":"0163"}
print(friends.keys())
print(friends.values())
print(friends.items())