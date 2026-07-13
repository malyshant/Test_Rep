# n = int(input('> '))
# while n != 1000:
#     print(n)
#     n = int(input('> '))

# n = int(input('> '))  # присваиваем значение переменной n
# sm = 0  # создаем переменную для суммы чисел
# count = 0 # переменная для счетчика чисел (итераций)
# cnt = 0
# while n != 0:  # выполняется пока n не равна 0
#     if n % 2 == 0:  # условие для обработки только четных чисел
#         sm += n  # увеличиваем значение sm  на число в n
#         count += 1  # четных чисел поступило
#     cnt += 1  # всего чисел поступило
#     n = int(input('>> '))  # # присваиваем значение переменной n
# print(f'Сумма:{sm}, кол-во:  {count}')
# prod = input('Заберите продукт: ')
# refr = ''
# count = 0
# while prod.lower() != 'stop':
#     refr += prod + ' '
#     count += 1
#     prod = input('Заберите продукт: ')
# res = refr.split()
# for product in res:
#     print(product)
# n = 123
# sn = str(n)
# sm = 0
# for s in sn:
#     sm += int(s)
# print(sm)

""" sm = 3 + 2 + 1
123  % 10 = 3
    // 10 = 12  % 10 = 2
                //10 = 1  % 10 = 1
                         // 10 = 0
"""
n = int(input('> '))
nn = n
sm = 0
cnt = 0
while n > 0:
    rem = n % 10
    sm += rem
    cnt += 1
    n = n // 10
print(f'в числе {nn} {cnt} ц. суммой {sm}')
n = int(input('> '))
res = 0
while n > 0:
    rem = n % 10
    res = res * 10 + rem
    n //= 10  # получение целой части от деления
    print(res)