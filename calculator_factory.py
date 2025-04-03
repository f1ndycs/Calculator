from simple_calculator import SimpleCalculator

class CalculatorFactory:
    @staticmethod
    def create_calculator(result_var, history_listbox):
        # Тут можно добавить логику для выбора типа калькулятора (если нужно)
        return SimpleCalculator(result_var, history_listbox)