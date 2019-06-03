"""
filters : easy weay to filter out a collection of items. based on a function result.

filter(function,data)
"""

list_grades = ["A","B","C","F","A","F"]

# filtering out the f's from our list

def filter_Func(item):
  return item != "F"

# using a filters
print(list(filter(filter_Func,list_grades)))


# using a for loop

filtered_list = []

for i in list_grades:
    filtered_list.append(filter_Func(i))
print(filtered_list)
"""
printing trues, and falses 
"""

filter_list1 = []

for i in list_grades:
    if i != "F":
        filter_list1.append(i)
print(filter_list1)


# using list comprehension

print([ i for i in list_grades if i != "F" ])