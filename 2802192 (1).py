import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

turtle.width(10) #What does this line do?

length = 5

for count in range(300):
  color = random.choice(colors) #Choose a random color
  turtle.forward(length)
  turtle.right(135)
  turtle.color(color) # Why is color spelt like this?
  length = length + 5
