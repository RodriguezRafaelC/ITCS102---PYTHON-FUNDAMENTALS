def greet(name):
  print(f"Hi {name}, are you good?")

def summation(x):
  sum = 0
  for y in range(x,0,-1):
    sum += y
  print(f"The sum of {x} is {sum}")

greet("Rafael")
greet("Rodriguez")
summation(18)