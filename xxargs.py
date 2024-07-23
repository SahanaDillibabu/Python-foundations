def save_user(**user): #double star allows for different value types/multiple word arguments
    print(user["name"])


save_user(id=1, name="John", age=22)