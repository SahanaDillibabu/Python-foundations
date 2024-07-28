letters = ["a","b","c"]

#add
letters.append("d") #add an item at the end of a list
letters.insert(0,"k") #add an item anywhere in a list
print(letters)

#remove
letters.pop() #remove item at the end of a list
letters.remove("b") #remove item when you know name but not index
del letters[0:2] #remove items with range
print(letters)
