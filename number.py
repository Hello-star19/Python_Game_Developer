#x= [17, 19 , 7 , 15, 10, 9 , 21, 22, 27, 23]

import random
x = random.sample(range(0, 100), 10)

print(x)


even_sqaure = []
odd_sqaure = []
for number in x:
    if number%2 == 0:
        even_sqaure.append(number**2)
    else:
        odd_sqaure.append(number**2)

print("The even squares are: ", even_sqaure)
print("The odd squares are: ", odd_sqaure)


x2 = [47, 41, 22, 74, 47, 41, 13, 98, 66, 41, 13]
print(x2, type(x2), len(x2))

unique_items = set(x2)
print(unique_items, type(unique_items), len(unique_items))
