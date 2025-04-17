from mvvm_model.calculator_model import Calculator

class CalculatorViewModel:
    def __init__(self):
        self.calculator = Calculator()
        self.result = ""

    def on_button_click(self, text):
        if self.result == "Ошибка" or self.result == "0":
            self.result = text
        elif text.isdigit() and self.result.endswith(text):
            pass  # предотвращаем повтор одной и той же цифры
        else:
            self.result += text

    def on_operation_click(self, op):
        if not self.result or self.result in ["Ошибка", "0"]:
            return
        if self.result[-1] not in "+-*/":
            self.result += op

    def on_equal_click(self):
        if not self.result or self.result == "Ошибка":
            return None, None
        try:
            expression = self.result
            self.result = str(eval(self.result))
            return expression, self.result
        except:
            self.result = "Ошибка"
            return expression, "Ошибка"

    def on_clear_click(self):
        self.result = ""

    def on_backspace(self):
        if self.result and self.result != "Ошибка":
            self.result = self.result[:-1]
