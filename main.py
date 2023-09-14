def count(a, d):
    while True:
        d += a % 10
        a //= 100
        if a < 1:
            break
    return d

a = int(input("Введите натуральное число: "))
c = a
b = 0
d = 0
while True:
    b += 1
    c //= 10
    if c < 1:
        break
if b % 2 == 0:
    d = count(a, d)
else:
    a //= 10
    d = count(a, d)
print("Сумма чётных цифр натурального числа - ", d)
