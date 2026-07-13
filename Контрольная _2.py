def add(x, y): return x + y


def sub(x, y): return x - y


def mul(x, y): return x * y


def div(x, y): return "Ошибка: Деление на ноль" if y == 0 else x / y


def save_history(line):
    with open("calculations.txt", "a", encoding="utf-8") as f:
        f.write(line + "\n")


def read_history():
    try:
        with open("calculations.txt", "r", encoding="utf-8") as f:
            print(f.read().strip())
    except FileNotFoundError:
        print("История пуста....")


print("Выберите операцию:")
print("1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Просмотр истории вычислений")

ch = input("Введите номер операции (1/2/3/4/5): ").strip()

if ch == '5':
    print("История вычислений:")
    read_history()
elif ch in ('1', '2', '3', '4'):
    n1 = int(input("Введите первое число: "))
    n2 = int(input("Введите второе число: "))

    if ch == '1':
        res = f"Результат: {n1} + {n2} = {add(n1, n2)}"
    elif ch == '2':
        res = f"Результат: {n1} - {n2} = {sub(n1, n2)}"
    elif ch == '3':
        res = f"Результат: {n1} * {n2} = {mul(n1, n2)}"
    elif ch == '4':
        res = f"Результат: {n1} / {n2} = {div(n1, n2)}"

    print(res)
    if "Ошибка" not in res:
        save_history(res)
else:
    print("Неверный ввод")