import random
import my_module

# Random integer
random_integer = random.randint(1,10)
print(random_integer)

print(my_module.my_favorite_number)

#Random floating point numbers between 0 and 1
random_number_0_to_1 = random.random() # 0<=n<1(1 is not inclusive)
print(random_number_0_to_1)

random_number = random.random() * 10 # 0<=n<10
print(random_number)

#Random floating point number
random_floating_number = random.uniform(1,10) #0<=n<=10 (10 is inclusive)
print(random_floating_number)

# creating heads or tail program
random_integer = random.randint(0,1)
if random_number == 0:
    print('head')
else:
    print('tail')
