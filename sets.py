numbers = [1,1,1,2,3,4,5,5,6,6,4]
first= set(numbers)
print(first)
#sets avoid repetition
#sets use curly brackets
second = {1,7}
print (first | second)
print (first & second)
print (first-second)
print (first ^ second) #semantic difference
#sets dont support indexing

if 1 in first:
    print("yes")