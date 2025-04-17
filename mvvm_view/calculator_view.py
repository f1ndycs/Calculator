import tkinter as tk
from mvvm_viewmodel.calculator_viewmodel import CalculatorViewModel
from calculator_factory import CalculatorButtonFactory

class CalculatorUI(tk.Tk):
    def __init__(self, viewmodel: CalculatorViewModel):
        super().__init__()
        self.viewmodel = viewmodel
        self.viewmodel.set_observer(self.update_result)
        self.title("Простой калькулятор (MVVM)")
        self.geometry("400x750")
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge")
        entry.pack(pady=20, fill="x")

        self.history_listbox = tk.Listbox(self, height=5, font=("Arial", 14), bd=5, relief="ridge")
        self.history_listbox.pack(pady=10, fill="x")

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
                                                           command=lambda t=text: self.viewmodel.add_input(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        operations = [("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)]
        for (text, row, col) in operations:
            button = CalculatorButtonFactory.create_button(buttons_frame, text, row, col,
                                                           command=lambda t=text: self.viewmodel.add_input(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        equal_clear_frame = tk.Frame(self)
        equal_clear_frame.pack(pady=10)

        equal_button = CalculatorButtonFactory.create_button(equal_clear_frame, "=", 0, 0, command=self.on_equal_click)
        equal_button.grid(row=0, column=0, padx=5, pady=5)

        clear_button = CalculatorButtonFactory.create_button(equal_clear_frame, "C", 0, 1, command=self.on_clear_click)
        clear_button.grid(row=0, column=1, padx=5, pady=5)

        clear_history_button = CalculatorButtonFactory.create_button(self, "Очистить историю", 0, 0, width=20,
                                                                     command=self.on_clear_history_click)
        clear_history_button.pack(pady=10)

        self.bind("<Key>", self.on_key_press)

    def update_result(self, new_result):
        self.result_var.set(new_result)

    def on_equal_click(self):
        self.viewmodel.calculate()
        self.history_listbox.insert(tk.END, self.viewmodel.get_history()[-1])
        self.history_listbox.yview(tk.END)

    def on_clear_click(self):
        self.viewmodel.clear()

    def on_clear_history_click(self):
        self.viewmodel.clear_history()
        self.history_listbox.delete(0, tk.END)

    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key in "+-*/.":
            self.viewmodel.add_input(key)
        elif key == "\r":
            self.on_equal_click()
        elif key == "\x08":
            current = self.result_var.get()
            self.result_var.set(current[:-1])
