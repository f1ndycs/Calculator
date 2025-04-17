from mvvm_view.calculator_view import CalculatorUI
from mvvm_viewmodel.calculator_viewmodel import CalculatorViewModel

if __name__ == "__main__":
    viewmodel = CalculatorViewModel()
    app = CalculatorUI(viewmodel)
    app.run()