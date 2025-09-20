name = 'John'

def hello():
  print("Hello from modules.py!")
  print("My name is", name)

def add_three_numbers(a, b, c):
  if a != 0 and b != 0 and c != 0:
    return a + b + c
  else:
    return "Error: One of the numbers is zero!"