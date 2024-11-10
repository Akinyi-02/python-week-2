#Creating an empty list
my_list = []
print("My empty list:", my_list)

#Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending 10, 20, 30, 40:", my_list)

#Inserting the value 15
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

#Extending the list
my_list.extend([50, 60, 70])
print("Extending with [50, 60, 70]:", my_list)

#Removing the last element from the list
my_list.pop()
print("Removing the last element:", my_list)

#Sorting the list in ascending order
my_list.sort()
print("Step 6 - After sorting in ascending order:", my_list)

#Finding and printing the index of the value 30
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")