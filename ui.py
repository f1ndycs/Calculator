import tkinter as tk
from calculator_factory import CalculatorFactory

class SimpleCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Простой калькулятор")
        self.geometry("400x700")  # Увеличиваем высоту окна
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
            button = tk.Button(buttons_frame, text=text, font=("Arial", 18), width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Кнопки операций
        operations = [
            ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)
        ]

        for (text, row, col) in operations:
            button = tk.Button(buttons_frame, text=text, font=("Arial", 18), width=5, height=2,
                               command=lambda t=text: self.on_operation_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Кнопки "=" и "C" в одной строке
        equal_clear_frame = tk.Frame(self)
        equal_clear_frame.pack(pady=10)

        equal_button = tk.Button(equal_clear_frame, text="=", font=("Arial", 18), width=5, height=2,
                                 command=self.on_equal_click)
        equal_button.grid(row=0, column=0, padx=5, pady=5)

        clear_button = tk.Button(equal_clear_frame, text="C", font=("Arial", 18), width=5, height=2,
                                 command=self.on_clear_click)
        clear_button.grid(row=0, column=1, padx=5, pady=5)

        # Настройка клавиш для работы с клавиатуры
        self.bind("<Key>", self.on_key_press)

        # Инициализация калькулятора через фабрику
        self.calculator = CalculatorFactory.create_calculator(self.result_var, self.history_listbox)

    def on_button_click(self, text):
        self.calculator.on_button_click(text)

    def on_operation_click(self, operation):
        self.calculator.on_operation_click(operation)

    def on_equal_click(self):
        self.calculator.on_equal_click()

    def on_clear_click(self):
        self.calculator.on_clear_click()

    def on_key_press(self, event):
        self.calculator.on_key_press(event)