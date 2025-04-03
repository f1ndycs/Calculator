import tkinter as tk

class SimpleCalculator:
    def __init__(self, result_var, history_listbox):
        self.result_var = result_var
        self.history_listbox = history_listbox

    def on_button_click(self, text):
        current = self.result_var.get()
        if text.isdigit() and current.endswith(text):
            return
        self.result_var.set(current + text)

    def on_operation_click(self, operation):
        current = self.result_var.get()
        if current and current[-1] not in "+-*/":
            self.result_var.set(current + operation)

    def on_equal_click(self):
        try:
            current = self.result_var.get()
            result = str(eval(current))  # Выполняем операцию
            self.result_var.set(result)

            # Добавляем в историю
            self.history_listbox.insert(tk.END, f"{current} = {result}")
            self.history_listbox.yview(tk.END)  # Прокручиваем к последнему элементу истории
        except Exception as e:
            self.result_var.set("Ошибка")

    def on_clear_click(self):
        self.result_var.set("")

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
            self.result_var.set(current[:-1])