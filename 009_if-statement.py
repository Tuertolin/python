cars = ['fiat','ferrari','bmw','ford']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
       print("Hold the anchovies!")

age = 19
# age < 21
#True
# age <= 21
#True
#>>> age > 21
#False
#>>> age >= 21
#False

# Check multiple conditions
#➊ >>> age_0 = 22
#   >>> age_1 = 18
#➋ >>> age_0 >= 21 and age_1 >= 21
#   False
#➌ >>> age_1 = 22
#   >>> age_0 >= 21 and age_1 >= 21
#   True

"""
Checking Whether a Value Is in a List
---------------------------------------------
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
➊ >>> 'mushrooms' in requested_toppings
   True
➋ >>> 'pepperoni' in requested_toppings
   False

Checking Whether a Value Is Not in a List
---------------------------------------------
banned_users = ['andrew', 'carolina', 'david']
   user = 'marie'

➊ if user not in banned_users:
       print(f"{user.title()}, you can post a response if you wish.")

"""