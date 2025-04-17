class CalculatorViewModel:
    def __init__(self, model):
        self.model = model
        self.result_observer = None
        self.history = []

    def set_observer(self, callback):
        """Позволяет UI подписаться на изменения результата"""
        self.result_observer = callback

    def add_input(self, value):
        self.model.add(value)
        self._notify()

    def calculate(self):
        result = self.model.evaluate()
        self.history.append(f"{self.model.result} = {result}")
        self.model.result = result  # Заменяем текущую строку результатом
        self._notify()

    def clear(self):
        self.model.clear()
        self._notify()

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()

    def _notify(self):
        if self.result_observer:
            self.result_observer(self.model.result)