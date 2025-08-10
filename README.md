Python List Operations Example

This project demonstrates basic **Python list operations** such as creating a list, appending items, inserting elements at specific positions, extending the list with multiple elements, removing items, sorting the list, and finding the index of a specific value.

## 📜 Code Overview

### Steps performed:
1. **Create an empty list**
   my_list = []
2. Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
3.Insert a new element at index 1
my_list.insert(1, 15)
4. Extend the list with multiple elements
my_list.extend([50, 60, 70])
Remove the last element
my_list.pop()
5.Sort the list in ascending order
my_list.sort()
6.Find the index of the value 30
index_30 = my_list.index(30)
print("index of 30:", index_30)
7.Print the final list
print("my_list:", my_list)
index of 30: 3
my_list: [10, 15, 20, 30, 40, 50, 60]
