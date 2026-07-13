from tkinter import *
from tkinter import messagebox as mb


# перезапуск расчета
def ask_restart():
    answer = mb.askretrycancel(title="Вопрос", message="Выполнить еще один расчет?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()


# Функция сложения трех чисел
def summ():
    s1, s2, s3 = e1.get(), e2.get(), e3.get()

    # Фильтр контроля ввода
    if not s1.lstrip('-').isdigit() or not s2.lstrip('-').isdigit() or not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во все поля должны быть введены числа!")
        return

    res = int(s1) + int(s2) + int(s3)
    m1['text'] = f"{s1} + {s2} + {s3} = {res}"
    ask_restart()


# Функция умножения трех чисел
def multiply():
    s1, s2, s3 = e1.get(), e2.get(), e3.get()

    # Фильтр контроля ввода
    if not s1.lstrip('-').isdigit() or not s2.lstrip('-').isdigit() or not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во все поля должны быть введены числа!")
        return

    res = int(s1) * int(s2) * int(s3)
    m1['text'] = f"{s1} * {s2} * {s3} = {res}"
    ask_restart()




window = Tk()
window.title("Калькулятор")

# Текстовое пояснение
m = Label(height=3, text="Введите три числа и нажмите на кнопку для вычисления:")
m.pack()

# Три технологических поля ввода
e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()
e3.pack()

# Сценарий summ
b1 = Button(text="Сложить три числа", command=summ)
b1.pack()

#Сценарий multiply
b2 = Button(text="Умножить три числа", command=multiply)
b2.pack()

# Поле вывода результата
m1 = Label(height=3)
m1.pack()


window.mainloop()