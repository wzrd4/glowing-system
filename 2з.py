a=input("Введите текст")
b = a.split(' ')
i = 0
while i < len(b):
    if b[i].endswith('а'):
        del b[i]
        continue
    i += 1
a = ' '.join(b)
print(f"Итоговый текст: {a}")