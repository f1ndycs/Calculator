from mvvm_viewmodel.calculator_viewmodel import CalculatorViewModel
from mvvm_view.calculator_view import CalculatorView

if __name__ == "__main__":
    vm = CalculatorViewModel()
    app = CalculatorView(vm)
    app.mainloop()