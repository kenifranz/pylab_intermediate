my_food =['ugali','mboga','wali','githeri']
friends_food = my_food[:]

print ("My favourite food are:")
print(my_food)

print("\nMy friend's  favourite food are:")
print(friends_food)

print()

my_food.append('chai')
friends_food.append('mkate')

print ("My favourite food are:")
for food in my_food:
    print (food)

print()

print("\nMy friend's  favourite food are:")
# print(friends_food)
for food in friends_food:
    print (food)
