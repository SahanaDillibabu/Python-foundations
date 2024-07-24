inputa = int(input("enter number"))

def fizzbuzz(inputa):
    if inputa % 3 == 0 and inputa % 5 == 0:
         return ("fizzbuzz")
    elif inputa % 3 == 0:
        return ("fizz")
    elif inputa % 5 == 0:
        return ("buzz")
    else:
         return ("none")
        

print(fizzbuzz(inputa))


