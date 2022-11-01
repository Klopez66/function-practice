#functions printing and returning
#print something in a function, its only for displaying
#some data, you are doing nothing with data

#when you return in a function, you are going to use it
# in another part of your program
from addfruit import add_fruit
from dividefruit import divide_fruit
from subtractfruit import subtract_fruit

apples = int(input("how many appes?"))
oranges = int(input("how many oranges?"))

# add fruit
fruitAdded = add_fruit(apples, oranges)
print(fruitAdded)
# subtract fruit
fruitSubtracted = subtract_fruit(apples, oranges)
print(fruitSubtracted)
# divide fruit
fruitDivided = divide_fruit(apples, oranges)
print(fruitDivided)
# display the added fruit, subtracted
fruitDisplay = display_fruit(fruitAdded, fruitSubtracted, fruitDivided)
