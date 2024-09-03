first = int(input('Любое первое число:'))
second = int(input('Любое второе число:'))
third = int(input('Любое третье число:'))
if first == second and first == third:
    print('Если все числа равны между собой, то вывести', 3)
elif first == second or second == third or first == third:
    print('Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести:', 2)
else:
    print('Если равных чисел среди 3-х вообще нет, то вывести', 0)