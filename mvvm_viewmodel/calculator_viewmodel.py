from mvvm_model.calculator_model import Calculator

class CalculatorViewModel:
    def __init__(self):
        self.calculator = Calculator()
        self.result = ""

    def on_button_click(self, text):
        current = self.result
        if current == "Ошибка" or current == "0":
            self.result = text
        else:
            self.result = current + text

    def on_operation_click(self, operation):
        current = self.result
        if current == "Ошибка" or current == "0":
            return
        if current and current[-1] not in "+-*/":
            self.result = current + operation

    def on_equal_click(self):
        current = self.result
        if current == "" or current == "Ошибка":
            return
        try:
            self.result = str(eval(current))  # Выполняем операцию
        except Exception as e:
            self.result = "Ошибка"

    def on_clear_click(self):
        self.result = ""
