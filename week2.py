#creating empty list
my_list=[]
#appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#changing index 1 element
my_list.insert(1,15)
#extending the list(adding more items to the list)
my_list.extend([50,60,70])
# removing the last item
my_list.pop()
#sortingthe elements in ascending order
my_list.sort()
#find and print the index of value 30
index_30=my_list.index(30)
print("index of 30:",index_30)

print("my_list:",my_list)
