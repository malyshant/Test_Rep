from tkinter import *
from tkinter import messagebox

# Глобальные настройки пера
line_width = 5  # Начальное значение толщины


def update_width():
    """Изменение толщины пера с проверкой """
    global line_width
    try:
        new_width = int(width_entry.get())
        if new_width > 0:
            line_width = new_width
        else:
            messagebox.showerror(
                "Ошибка", "Толщина линии должна быть больше нуля"
            )
    except ValueError:
        # Ловим ошибку
        messagebox.showerror("Ошибка", "Введите целое число для толщины")


def draw_circle():
    """Круг с выбранной толщиной линии"""
    fill_color = fill_color_entry.get()
    outline_color = outline_color_entry.get()
    # Передаем глобальную  line_width в параметр width
    canvas.create_oval(
        50,
        50,
        150,
        150,
        outline=outline_color,
        fill=fill_color,
        width=line_width,
    )


def draw_triangle():
    fill_color = fill_color_entry.get()
    outline_color = outline_color_entry.get()
    canvas.create_polygon(
        50,
        150,
        100,
        50,
        150,
        150,
        outline=outline_color,
        fill=fill_color,
        width=line_width,
    )


def draw_square():
    fill_color = fill_color_entry.get()
    outline_color = outline_color_entry.get()
    canvas.create_rectangle(
        50,
        50,
        150,
        150,
        outline=outline_color,
        fill=fill_color,
        width=line_width,
    )


def clear_canvas():
    canvas.delete("all")


# Инициализация окна графического редактора
window = Tk()
window.title("Графический редактор")
window.geometry("450x600")

canvas = Canvas(window, width=300, height=200, bg="white")
canvas.pack(pady=10)

# Инструменты выбора цвета (из листинга)
Label(window, text="Цвет заливки:").pack()
fill_color_entry = Entry(window)
fill_color_entry.pack(pady=5)
fill_color_entry.insert(0, "blue")

Label(window, text="Цвет обводки:").pack()
outline_color_entry = Entry(window)
outline_color_entry.pack(pady=5)
outline_color_entry.insert(0, "black")

# --- NEW  Управление толщиной пера ---
Label(window, text="Толщина линии:").pack(pady=5)

width_entry = Entry(window)
width_entry.pack(pady=5)
width_entry.insert(0, str(line_width))  # Установка дефолтного значения на экран

width_button = Button(
    window, text="Установить толщину", command=update_width
)
width_button.pack(pady=5)
# ---------------------------------------------

# Кнопки  фигур
circle_button = Button(window, text="Окружность", command=draw_circle)
circle_button.pack(pady=5)

triangle_button = Button(window, text="Треугольник", command=draw_triangle)
triangle_button.pack(pady=5)

square_button = Button(window, text="Квадрат", command=draw_square)
square_button.pack(pady=5)

clear_button = Button(window, text="Очистить", command=clear_canvas)
clear_button.pack(pady=5)

window.mainloop()