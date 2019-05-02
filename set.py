# declare a set
set1 = set([1,2,3,4,5]) # this can be seen as cast a list [1,2,3,4,5] to a set
# or
set1 = {1,2,3,4,5} # can not use this method to declare a empty set since {} is used to declare a new dict
# remove duplicates
list1 = [1,2,3,3,3,5,5,1,2,2]
set_no_duplicate = set(list1)
print("remove duplicates:")
print(set_no_duplicate)
print("convert it back to list type:")
print(list(set_no_duplicate))

# compare duplicates between two sets
print("compare and remove duplicates between to sets")
set2 = {2,5,6,7}
print(set1 - set2)
print(set1 | set2)
print(set1 & set2)
print(set1 ^ set2)
