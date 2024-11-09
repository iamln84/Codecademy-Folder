# Len's Slice Pizza Stop

# Toppings options
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushtooms"]

# Prices
prices = [2, 6, 1, 3, 2, 7, 2]

# $2 Price Count
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Length of toppings list
num_pizzas = len(toppings)
print(num_pizzas)

# Printing a string
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

# two - dimensional list

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7,  "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sorting & Slicing Pizzas
pizza_and_prices.sort()
print(pizza_and_prices)

# Cheapest Pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# Priciest Pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Removing the priciest pizza / New topping
pizza_and_prices[6] = [2.5, "peppers"]
print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

# Three lowest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)