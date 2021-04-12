def pizza_toppings(*toppings):
    print("The pizza toppings are:")
    for topping in toppings:
        print(f" -{topping}")

pizza_toppings('muzza')
pizza_toppings('muzza','peperonni')
