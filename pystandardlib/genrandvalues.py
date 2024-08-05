import random
import string
print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3,4]))
print(random.choice([1,2,3,4]))
print(",".join(random.choice(string.ascii_letters + string.digits)))

numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)