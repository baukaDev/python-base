while True:

  input_node = input("Enter something: ")

  if input_node.lower() == "exit":
    print("Exiting...")
    break

  if input_node.strip() == "check":
    with open("data/node.txt", 'r') as f:
      content = f.read().strip()
      if content == "":
        print('Файл пустой')
      else:
        print("Все записи:")
        print(content)
    continue

  if input_node == "clear":
    with open("data/node.txt", 'w') as f:
      pass
    print("Все записи удалены.")
    continue

  if input_node.lower().startswith("del "):
    to_delete = input_node[4:].strip()
    with open("data/node.txt", 'r') as f:
      lines = f.readlines()
    with open("data/node.txt", 'w') as f:
      deleted = False
      for line in lines:
        if line.strip() != to_delete:
          f.write(line)
        else:
          deleted = True
      if deleted:
        print(f"Запись '{to_delete}' удалена.")
      else:
        print(f"Запись '{to_delete}' не найдена.")
      continue

  double_check = False
  with open("data/node.txt", "r") as f:
    for line in f:
      if input_node.strip() == line.strip():
        print(f"Такая запсись уже есть: {line.strip()}")
        double_check = True
        break

  if not double_check:
    with open("data/node.txt", "a") as f:
      f.write(input_node + "\n")
    print("Запись добавлена.")