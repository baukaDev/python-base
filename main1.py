# for i in range(10):
#   print(i)

# for i in range(1, 9):
#   print(i)

# for i in range(1, 9, 2):
#   print(i)

#################################################################################

# count = 0
# word = "Python"
# for i in word:
#   print(i * 3)
#   if (i == "h"):
#     print("Found it!")
#     count += 1

# print("Count:", count)

#################################################################################

# i = 0
# while (i < 10):
#   print(i)
#   i += 1


# while True:
#   line = input("Enter text: ")
#   if(line == "stop"):
#     break


#################################################################################

# for i in range(1, 11):
#   if (i == 5):
#     break

#   if (i % 2 == 0):
#     continue
#   print(i)

#################################################################################

# found = None
# for i in "hello":
#   if(i == "l"):
#     found = True
#     break
#   else:
#     found = False
# print(found)


################################################################################# СПИСОК list

# nums = [3,5,1,7,9, True, 'hello', 5.5, [ 1,2,3] ]
# nums[1] = 10

# print(nums[-1])
# print(nums[-1][1])


# numbers = [4,2,3]
# numbers.append(5)
# numbers.insert(1, True)

# numbers.extend([1,2,3])

# numbers.sort()
# numbers.reverse()

# numbers.pop()
# numbers.pop(1)
# numbers.remove(3)

# numbers.clear()

# print(numbers.count(3))
# print(len(numbers))

# print("#########################")

# nums = [4,2,3,4,5,4]
# for i in nums:
#   print(i)

# n = int(input("Длина списка: "))
# data = []
# for i in range(n):
#   str_i = "Введите элемент #" + str(i) + ": "
#   data.append(input(str_i))

# print(data)

############################## Функции строк. Индексы и срезы ################################################### СПИСОК list

# word = "football, basketball, volleyball"
# print(len(word))
# print(word.lower())
# print(word.upper())
# print(word[0])
# print(word.count("l"))

# print(word.isupper())
# print(word.islower())

# print(word.capitalize())

# print(word.find("l"))

# print(word.replace("l", "r"))

# print(word.split())
# print(word.split(","))

# print("#########################")

# hobbys = word.split(", ")
# for i in range(len(hobbys)):
#   hobbys[i] = hobbys[i].capitalize()

# res =  " || ".join(hobbys)
# print(res)

#####################################

# nums = [4,2,3,4,5,4]
# for i in range(len(nums)):
#   for j in range( i + 1, len(nums)):
#     num1 = nums[i]
#     num2 = nums[j]
#     # print(num1, num2)
#     if (num1 + num2 == 9) and (num1 != num2):
#       print(num1, "+", num2, "= 9")
#       break

##################### Словари (dict) и работа с ними ######################
country = {'code': 'RU', "name": "Russia", "population": 144}
# country = dict(code='RU', name='Russia', population=144)
# print(country)

# print(country.items())

# for key, value in country.items():
#   print(key, ":", value)

# for key in country:
#   print(key, ":", country[key])

# country.pop("code")
# country.popitem()
# print(country)

person = {
  'user_1': {'name': 'Alice', 'age': 30, 'address': ['Street 1', 'City A'], 'grades': {'math': 90, 'science': 85}},
  'user_2': {'name': 'Bob', 'age': 25, 'address': ['Street 2', 'City B'], 'grades': {'math': 80, 'science': 88}},
  'user_3': {'name': 'Charlie', 'age': 35, 'address': ['Street 3', 'City C'], 'grades': {'math': 95, 'science': 92}},
}

for user_id, user_info in person.items():
  name = user_info['name']
  age = user_info['age']
  city = user_info['address'][1]
  math_grade = user_info['grades']['math']
  science_grade = user_info['grades']['science']
  
  print(f"User ID: {user_id}")
  print(f"Name: {name}")
  print(f"Age: {age}")
  print(f"City: {city}")
  print(f"Math Grade: {math_grade}")
  print(f"Science Grade: {science_grade}")
  print("-----------------------")


##################### Множества (set и frozenset) ######################