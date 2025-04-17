import tkinter as tk
from mvvm_viewmodel.calculator_viewmodel import CalculatorViewModel
from mvvm_model.calculator_factory import CalculatorButtonFactory

class CalculatorUI(tk.Tk):
    def __init__(self, viewmodel: CalculatorViewModel):
        super().__init__()
        self.viewmodel = viewmodel
        self.title("Простой калькулятор")
        self.geometry("400x750")
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar(value=self.viewmodel.result)
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge")
        entry.pack(pady=20, fill="x")

        self.history_listbox = tk.Listbox(self, height=5, font=("Arial", 14), bd=5, relief="ridge")
        self.history_listbox.pack(pady=10, fill="x")

        buttons_frame = tk.Frame(self)
        buttons_frame.pack()

        # Числа и точка
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 1), (".", 4, 0)
        ]

        for (text, row, col) in buttons:
            button = CalculatorButtonFactory.create_button(buttons_frame, text, row, col,
                                                           command=lambda t=text: self.handle_input(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        operations = [("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)]

        for (text, row, col) in operations:
            button = CalculatorButtonFactory.create_button(buttons_frame, text, row, col,
                                                           command=lambda t=text: self.handle_operation(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        equal_clear_frame = tk.Frame(self)
        equal_clear_frame.pack(pady=10)

        equal_button = CalculatorButtonFactory.create_button(equal_clear_frame, "=", 0, 0, command=self.handle_equal)
        equal_button.grid(row=0, column=0, padx=5, pady=5)

        clear_button = CalculatorButtonFactory.create_button(equal_clear_frame, "C", 0, 1, command=self.handle_clear)
        clear_button.grid(row=0, column=1, padx=5, pady=5)

        clear_history_button = CalculatorButtonFactory.create_button(self, "Очистить историю", 0, 0, width=20,
                                                                     command=self.handle_clear_history)
        clear_history_button.pack(pady=10)

        self.bind("<Key>", self.handle_key)

    def update_view(self):
        self.result_var.set(self.viewmodel.result)

    def handle_input(self, text):
        self.viewmodel.on_button_click(text)
        self.update_view()

    def handle_operation(self, op):
        self.viewmodel.on_operation_click(op)
        self.update_view()

    def handle_equal(self):
        expression, result = self.viewmodel.on_equal_click()
        self.update_view()
        if expression and result:
            self.history_listbox.insert(tk.END, f"{expression} = {result}")
            self.history_listbox.yview(tk.END)

    def handle_clear(self):
        self.viewmodel.on_clear_click()
        self.update_view()

    def handle_clear_history(self):
        self.history_listbox.delete(0, tk.END)

    def handle_key(self, event):
        key = event.char
        if key.isdigit() or key in "+-*/.":
            self.handle_input(key)
        elif key == "\r":
            self.handle_equal()
        elif key == "\x08":
            self.viewmodel.on_backspace()
            self.update_view()
