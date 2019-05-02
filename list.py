# list, mutable, data can be altered, like arraylist in java
# Tuple is unmutable
list1 = [1,2,3,"hello world","10.001",True]
print(list1)

# index
print(list1[2])
list1[2] = 4
print(list1[2])

# list.append()
list1.append("append an element")
print(list1)

# list.insert(), insert an element before the postion request
list1.insert(1,"inserted")
print(list1)

# list.extend()
list1.extend(["extend1", "extend2"])
print(list1)

# sublist
print(list1[6:8])
print(list1[-4:-2])

# list.remove(element)
list1.remove("hello world")
print(list1)

# list.pop(index)
list1.pop(len(list1)-1)
print(list1)
