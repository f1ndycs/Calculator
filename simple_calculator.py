from ui import CalculatorUI
from calculator import Calculator

class SimpleCalculator:
    def __init__(self):
        self.calculator = Calculator()
        self.ui = CalculatorUI(self.calculator)

    def run(self):
        self.ui.mainloop()