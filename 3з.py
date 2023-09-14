while True:
    a = int(input("Введите натуральное число >= 2 "))
    if a < 2:
        print("Ошибка!:")
    else:
        break
i = 0
li = []
print(f"Введите {a} целых чисел ")
while i < a:
    b = input()
    li.append(b)
    i += 1
li2 = []
for i in range(len(li)):
    if i == 0:
        li2.append(li[i + 1])
    elif i == len(li) - 1:
        li2.append(li[len(li) - 2])
    else:
        li2.append(int(li[i - 1]) + int(li[i + 1]))
print(f"Итоговый список: {li2}")