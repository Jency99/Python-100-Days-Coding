import random

# solution 1
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = random.choice(friends)
print(random_friend)


# solution 2
random_index = random.randint(0,4)
print(friends[random_index])
