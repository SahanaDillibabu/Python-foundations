#dictionaries are collections of key value pairs
point = {"x":1, "y":2}
point = dict(x=1,y=2)
print(point["x"]) #cannot use numbers to access index
point["z"] = 20
if "a" in point:
    print(point["a"])
del point["x"]
print (point)
for key in point:
    print(key, point[key])
    