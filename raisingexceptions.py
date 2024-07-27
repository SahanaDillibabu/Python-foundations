def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


agevalue = int(input("enter age:"))
calculate_xfactor(agevalue)
if agevalue == None:
    pass
