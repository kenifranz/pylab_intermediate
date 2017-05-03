pizzas =['macaroni', 'beef','chicken','fruit']
for pizza in pizzas:
	print(pizza)
	print (pizza.title(), "is sweet")
	print ("I love" , pizza.title() + "\n")
print("You see!, I really like pizza!!!")

# Make a copy of pizza
friend_pizzas = pizzas[:]
print()
print(friend_pizzas)

# Add new pizza on the menu
pizzas.append('peperoni')
friend_pizzas.append('mixed')

# Print out the final message in loop

for pizza in pizzas:
	print('My favourite pizza is',pizza)
print()

for pizza in friend_pizzas:
	print('My favourite pizza is',pizza)

print()





