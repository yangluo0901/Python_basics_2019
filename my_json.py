import json
j = '{"city": "beijing", "name":"panda"}'
p = json.loads(j)
print(f"json to dictionary: {p}, type is {type(p)}")
d = {"city": "beijing", "name": "panda"}
j_1 = json.dumps(d)
print(f"dictionary to json: {j_1}, type is {type(j_1)}")