from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def on_button_click(self, text):
        pass

    @abstractmethod
    def on_operation_click(self, operation):
        pass

    @abstractmethod
    def on_equal_click(self):
        pass

    @abstractmethod
    def on_clear_click(self):
        pass

    @abstractmethod
    def on_key_press(self, event):
        pass