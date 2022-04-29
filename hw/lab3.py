import json
def todo_list():
    f = open('todo.json', 'w')
    f.close()
    t = []
    s = int(input("Выберите команду:\n 1) Добавить задачу\n 2) Список задач\n 3) Выход"))
    while s != 3:
        if s == 1:
            name = input('Сформулируйте задачу: ')
            category = input('Добавьте категорию к задаче: ')
            time = input('Добавьте время к задаче: ')
            t.append({"category": category, "name": name, "time": time})
            f = open("todo.json", "w")
            f.write(json.dumps(t))
            f.close()
        elif s == 2:
            f = open('todo list.json','r')
            tasks = json.load(f)
            f.close()
            for i in tasks:
                print('Задача: ', i["name"], 'Категория: ', i["category"], 'Дата: ', i["time"])
        else:
            print("Команды не существует!")
    print('Задачи сохранены в файл!')