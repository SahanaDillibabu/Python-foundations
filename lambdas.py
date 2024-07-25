items = [
    ("Product1", 10),
    ("Product2",9),
    ("Product3", 12),
]

x=map(lambda item: item[1], items)
for item in x:
    print(item)

