import tkinter as tk
from calculator_factory import CalculatorButtonFactory

class CalculatorUI(tk.Tk):
    def __init__(self, calculator):
        super().__init__()
        self.calculator = calculator
        self.title("Простой калькулятор")
        self.geometry("400x750")  # Увеличиваем высоту окна для добавления кнопки очистки истории
        self.create_widgets()

    def create_widgets(self):
        # Поле вывода
        self.result_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge")
        entry.pack(pady=20, fill="x")

        # История вычислений
        self.history_listbox = tk.Listbox(self, height=5, font=("Arial", 14), bd=5, relief="ridge")
        self.history_listbox.pack(pady=10, fill="x")

        # Кнопки чисел
        buttons_frame = tk.Frame(self)
        buttons_frame.pack()

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 1), (".", 4, 0)
        ]

        for (text, row, col) in buttons:
            button = CalculatorButtonFactory.create_button(buttons_frame, text, row, col,
                                                           command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Кнопки операций
        operations = [
            ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)
        ]

        for (text, row, col) in operations:
            button = CalculatorButtonFactory.create_button(buttons_frame, text, row, col,
                                                           command=lambda t=text: self.on_operation_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Кнопки "=" и "C" в одной строке
        equal_clear_frame = tk.Frame(self)
        equal_clear_frame.pack(pady=10)

        equal_button = CalculatorButtonFactory.create_button(equal_clear_frame, "=", 0, 0, command=self.on_equal_click)
        equal_button.grid(row=0, column=0, padx=5, pady=5)

        clear_button = CalculatorButtonFactory.create_button(equal_clear_frame, "C", 0, 1, command=self.on_clear_click)
        clear_button.grid(row=0, column=1, padx=5, pady=5)

        # Кнопка очистки истории
        clear_history_button = CalculatorButtonFactory.create_button(self, "Очистить историю", 0, 0, width=20,
                                                                     command=self.on_clear_history_click)
        clear_history_button.pack(pady=10)

        # Настройка клавиш для работы с клавиатуры
        self.bind("<Key>", self.on_key_press)

    def on_button_click(self, text):
        current = self.result_var.get()

        # Если после вычисления или ошибки вводим новую цифру
        if current == "Ошибка" or current == "0":
            self.result_var.set(text)  # Сбрасываем строку и начинаем с нового числа
            return

        # Проверка на дублирование цифр
        if text.isdigit() and current.endswith(text):
            return

        self.result_var.set(current + text)

    def on_operation_click(self, operation):
        current = self.result_var.get()

        # Если после вычисления пытаемся добавить операцию, не добавляем
        if current == "Ошибка" or current == "0":
            return  # Не добавляем операцию после результата или ошибки

        if current and current[-1] not in "+-*/":
            self.result_var.set(current + operation)

    def on_equal_click(self):
        current = self.result_var.get()

        # Если строка пуста или ошибка, ничего не делаем
        if current == "" or current == "Ошибка":
            return

        try:
            result = str(eval(current))  # Выполняем операцию
            self.result_var.set(result)

            # Добавляем в историю
            self.history_listbox.insert(tk.END, f"{current} = {result}")
            self.history_listbox.yview(tk.END)  # Прокручиваем к последнему элементу истории
        except Exception as e:
            self.result_var.set("Ошибка")  # Если ошибка, выводим сообщение

    def on_clear_click(self):
        self.result_var.set("")  # Очищаем строку

    def on_clear_history_click(self):
        # Очистка истории
        self.history_listbox.delete(0, tk.END)

    def on_key_press(self, event):
        key = event.char
        current = self.result_var.get()

        # Проверка на дублирование операторов
        if key in "+-*/" and (current and current[-1] in "+-*/"):
            return

        # Проверка на дублирование цифр
        if key.isdigit() and current.endswith(key):
            return

        # Добавляем только цифры и допустимые символы
        if key.isdigit() or key in "+-*/.":
            self.on_button_click(key)
        elif key == "\r":  # Enter key
            self.on_equal_click()
        elif key == "\x08":  # Backspace key
            self.result_var.set(current[:-1])  # Удаляем последний символ
