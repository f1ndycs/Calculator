class Calculator:
    def __init__(self):
        self.result = ""

    def add(self, value):
        self.result += value

    def evaluate(self):
        try:
            return str(eval(self.result))  # Внимание на использование eval
        except Exception:
            return "Ошибка"

    def clear(self):
        self.result = ""