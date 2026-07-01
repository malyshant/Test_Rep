import random
import tkinter as tk
from tkinter import messagebox


def check_color():
    # Список доступных цветов светофора
    colors = ["зеленый", "желтый", "красный"]

    # Получаем текст из поля ввода, убираем пробелы по краям и переводим в нижний регистр
    user_choice = entry.get().strip().lower()

    # Заменяем букву "ё" на "е", чтобы не было обидных ошибок при вводе
    user_choice = user_choice.replace("ё", "e")

    # Проверяем, корректный ли цвет ввел пользователь
    if user_choice not in colors:
        messagebox.showwarning(
            "Внимание", "Введите один из трех цветов: Зеленый, Желтый, Красный"
        )
        return

    # Компьютер делает свой случайный выбор
    computer_choice = random.choice(colors)

    # Формируем текст с результатами сравнения
    result_text = (
        f"Твой выбор: {user_choice.capitalize()}\n"
        f"Выбор компьютера: {computer_choice.capitalize()}\n\n"
    )

    # Сравниваем значения и выводим итог
    if user_choice == computer_choice:
        result_text += "🎉 МОЛОДЕЦ, УГАДАЛ! 🎉"
        messagebox.showinfo("Победа!", result_text)
    else:
        result_text += "❌ Увы, не угадал! Попробуй еще раз. ❌"
        messagebox.showerror("Промах", result_text)

    # Очищаем поле ввода для следующей попытки
    entry.delete(0, tk.END)


# --- Создание графического интерфейса (GUI) ---
root = tk.Tk()
root.title("Угадай цвет светофора")
root.geometry("400x250")
root.resizable(False, False)

# Инструкция для пользователя
label_instruction = tk.Label(
    root,
    text="Компьютер загадал цвет светофора.\nУгадай какой!",
    font=("Arial", 12, "bold"),
    pady=10,
)
label_instruction.pack()

label_hint = tk.Label(
    root,
    text="Доступные варианты: Зеленый, Желтый, Красный",
    font=("Arial", 10),
    fg="gray",
)
label_hint.pack()

# Поле для ввода текста
entry = tk.Entry(root, font=("Arial", 14), width=15, justify="center")
entry.pack(pady=15)
entry.focus()  # Сразу ставим курсор в поле ввода

# Кнопка "Проверить"
btn_check = tk.Button(
    root,
    text="Проверить",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=check_color,
)
btn_check.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()