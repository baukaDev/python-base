class Cat: 
  # name = None
  # age = None
  # isHappy = None

  def __init__(self, name, age, isHappy = None):
    self.self_data(name, age, isHappy)
    self.get_data()

  def self_data(self, name, age, isHappy = None):
    self.name = name
    self.age = age
    self.isHappy = isHappy
  
  def get_data(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Is Happy: {self.isHappy}")
    print("-----------------------")


cat1 = Cat("Murzik", 3, True)
cat2 = Cat("Barsik", 5, False)
cat2 = Cat("Barsik", 5)

