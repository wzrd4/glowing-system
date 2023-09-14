a = input("Введите первое слово для проверки на анаграммы: ")
b = input("Введите второе слово: ")
c = list(a)
d = list(b)
if len(c) != len(b):
    print("Слова не анаграммы")
else:
    i = 0
    while i < len(c):
        flag = False
        j = 0
        while j < len(d):
            if c[i] == d[j]:
                del c[i]
                del d[j]
                flag = True
                break
            j += 1
        if not flag:
            i += 1
if len(c) == len(d) == 0:
    print("Слова анаграммы!")
else:
    print("Не являются анаграммами")