from tkinter import *
from time import strftime
from tkinter import messagebox
import pygame as pg


# =====================================================================
# БЛОК 1: ФУНКЦИИ ЛОГИКИ (Что делает программа при событиях)
# =====================================================================

def click_start_button():
    """Срабатывает при нажатии на кнопку 'Включить'."""
    global target_alarm_time
    # .get() забирает текст из поля ввода, .strip() убирает случайные пробелы
    target_alarm_time = input_field.get().strip()

    # Показываем всплывающее окошко с подтверждением
    messagebox.showinfo('Статус', f'Будильник успешно установлен на: {target_alarm_time}')


def click_stop_button():
    """Срабатывает при нажатии на кнопку 'Выключить'."""
    global target_alarm_time
    target_alarm_time = ''  # Сбрасываем записанное время будильника
    input_field.delete(0, END)  # Полностью очищаем поле ввода от текста
    pg.mixer.music.stop()  # Принудительно выключаем музыку
    messagebox.showinfo('Статус', "Будильник полностью отключён")


def update_time_loop():
    """Главный бесконечный движок программы. Срабатывает раз в секунду."""
    global target_alarm_time

    # 1. Получаем у системы точное время в формате Строки (например, '14:30:05')
    now_system_time = strftime('%H:%M:%S')

    # 2. ПРОВЕРКА (Идея Евгения): если будильник заведен и совпал с текущим временем
    if target_alarm_time == now_system_time:
        target_alarm_time = ''  # Сбрасываем будильник, чтобы он не пел на следующей секунде
        pg.mixer.music.play()  # Включаем проигрывание нашей музыки

    # 3. Обновляем текст на экране: подставляем живое время в нашу текстовую метку
    clock_label.config(text=now_system_time)

    # 4. МАГИЯ ТАЙМЕРА: просим окно через 1000 миллисекунд (1 сек) снова вызвать эту же функцию
    clock_label.after(1000, update_time_loop)


# =====================================================================
# БЛОК 2: НАСТРОЙКА АУДИО (Подготовка плеера)
# =====================================================================
pg.mixer.init()  # Инициализируем звуковой движок Pygame
pg.mixer.music.load('alarm.wav')  # Загружаем аудиофайл (должен лежать в папке с проектом)

# =====================================================================
# БЛОК 3: ГРАФИЧЕСКИЙ ИНТЕРФЕЙС (Создание окошка и виджетов)
# =====================================================================

# 1. Создаем главное окно и называем его понятным словом 'window'
window = Tk()
window.title('Инженерный Будильник')
window.config(bg='black')  # Фон окна — черный

# 2. Математика центрирования окна на экране
SCREEN_WIDTH = window.winfo_screenwidth()  # Ширина твоего монитора
SCREEN_HEIGHT = window.winfo_screenheight()  # Высота твоего монитора
WINDOW_WIDTH = 400  # Желаемая ширина нашего окна
WINDOW_HEIGHT = 250  # Желаемая высота нашего окна

# Вычисляем координаты для открытия ровно по центру экрана
pos_x = SCREEN_WIDTH // 2 - WINDOW_WIDTH // 2
pos_y = SCREEN_HEIGHT // 2 - WINDOW_HEIGHT // 2
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{pos_x}+{pos_y}')

# 3. Виджет 1: Крупное табло для отображения часов
clock_label = Label(window, text='00:00:00')
clock_label.config(font=('Arial', 50), fg='lime', bg='black')
clock_label.pack(pady=10)  # pady=10 делает небольшой пустой отступ сверху и снизу

# 4. Виджет 2: Однострочное поле для ввода времени будильника
input_field = Entry(window)
input_field.config(width=10, justify='center', font=('Arial', 20))
input_field.pack(pady=5)

# 5. Виджет 3: Кнопка включения будильника
btn_start = Button(window)
btn_start.config(width=12, text='Включить', font=('Arial', 10), command=click_start_button)
btn_start.pack(pady=5)

# 6. Виджет 4: Кнопка выключения будильника и музыки
btn_stop = Button(window)
btn_stop.config(width=12, text='Выключить', font=('Arial', 10), command=click_stop_button)
btn_stop.pack(pady=5)

# =====================================================================
# БЛОК 4: ЗАПУСК ПРОГРАММЫ
# =====================================================================

target_alarm_time = ''  # Изначально будильник пустой (не заведен)

update_time_loop()  # Делаем ПЕРВЫЙ ручной запуск часов, чтобы запустить бесконечный цикл обновления
window.mainloop()  # Включаем постоянное отображение окна на экране (без этого окно сразу закроется)