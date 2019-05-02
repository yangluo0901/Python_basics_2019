a = (1,2,"hello world")
#a[1] = 10
# Tuple cannot be altered, error

# dict, similar hash map in java, {key,value}
dict1 = {"name":"yang",
    "age":28,
    "gender":"male"}

# get value
print(dict1["name"])
print(dict1.get("name"))

# change value
dict1["name"] = "Ran"
print(dict1)

# get values
print(type(dict1.values()))

# get items {key,value}
print(dict1.items())

# if key exists

print("age" in dict1)

# add an element
dict1["height"] = "5'7''"
print(dict1)

# pop(key)
