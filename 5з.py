def getvalue(dicti, pos):
    i = 0
    keys = list(dicti.keys())
    while i < len(keys):
        value1 = list(dicti.get(keys[i]))
        print(f"{keys[i]} : {value1[pos]}")
        i += 1

dict1 = {}
while True:
    lis = []
    a = input("Введите наименование изделия ")
    b = input("Введите материал изделия ")
    c = int(input("Введите цену изделия "))
    d = int(input("Введите количество изделий "))
    lis.extend([b, c, d])
    dict1.update({a: lis})
    a = input("Продолжить ввод? (д/н) ")
    if a == 'н':
        break
while True:
    print("Меню")
    print("Введите:")
    print("1 - просмотреть все названия и состав")
    print("2 - просмотреть все названия и цены")
    print("3 - просмотреть все названия и количества")
    print("4 - просмотреть всю информацию")
    print("5 - купить изделие")
    print("6 - выход")
    print("Ваш выбор? ")
    choice = int(input())
    if choice == 1:
        getvalue(dict1, 0)
    elif choice == 2:
        getvalue(dict1, 1)
    elif choice == 3:
        getvalue(dict1, 2)
    elif choice == 4:
        print(dict1)
    elif choice == 5:
        name = input("Введите наименование изделия, которое вы хотите купить ")
        value = dict1.get(name)
        if value == None:
            print("Такого изделия нет в наличии")
            continue
        else:
            while True:
                amount = int(input("Введите количество "))
                if amount > value[2]:
                    print(f"В наличии только {value[2]} шт.")
                else:
                    break
            print(f"Вы успешно приобрели {name} (материал - {value[0]}) ценой {value[1]} р. за шт. в количестве {amount} шт.")
            value[2] -= amount
            if value[2] == 0:
                dict1.pop(name)
            else:
                dict1.update({name: value})
    elif choice == 6:
        keys = list(dict1.keys())
        i = 0
        print("В изначальном списке остались:")
        while i < len(keys):
            print(keys[i])
            i += 1
        exit(0)
    else:
        print("Неверный ввод")
        continue
