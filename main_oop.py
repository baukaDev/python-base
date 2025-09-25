class Building:
  year = None
  city = None

  def __init__(self, year, city):
    self.year = year
    self.city = city
  def get_info(self):
    print(f"Year: {self.year}")
    print(f"City: {self.city}")


class School(Building):
  pupils = 0

  def __init__(self, year, city, pupils):
    super(School, self).__init__(year, city)
    self.pupils = pupils

  def get_info(self):
    super().get_info()
    print(f"Pupils: {self.pupils}")
    print("-----------------------")

class House(Building):
  pass

class Shop(Building):
  pass


school = School(1990, "New York", 500)
school.get_info()
house = House(2000, "Los Angeles")
shop = Shop(2010, "Chicago")
shop.get_info()