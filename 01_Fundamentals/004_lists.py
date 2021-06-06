bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'GT']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

print(bicycles[-1].title())

message = f"My first bike was a {bicycles[-1].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'zanella', 'susuki']
print( motorcycles, "\n")

motorcycles[0] = "ducati"
print( motorcycles, "\n")

motorcycles.append("Honda")
for x in motorcycles:
    print(x.title())

print("\n")
motorcycles.insert(1 , "triumph")
print( motorcycles)

del motorcycles[0]
print( motorcycles)

# The pop() method removes the last item in a list, but it lets you work with that item after removing it.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('triumph')
print(motorcycles)

