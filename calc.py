class Calculator:

  def add(self, a, b):
    return a + b
  
  def subtract(self, a, b):
    return a - b
  
  def multiply(self, a, b):
    return a * b
  
  def divide(self, a, b):
    if b == 0:
      return "Error! Division by zero."
    else:
      return a / b
    
while True:
  try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
  except ValueError:
    print("Invalid input. Please enter numeric values.")
    continue

  operation = input("Enter operation (+, -, *, /): ")

  calc = Calculator()
  if operation == "+":
    print("Result:", calc.add(a,b))
  elif operation == "-":
    print("Result:", calc.subtract(a,b))
  elif operation == "*":
    print("Result:", calc.multiply(a,b))
  elif operation == "/":
    print("Result:", calc.divide(a,b))
  else:
    print("Invalid operation.")