import tkinter as tk

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Простой калькулятор")
        self.geometry("400x600")
        self.create_widgets()

    def create_widgets(self):
        # Поле вывода
        self.result_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge")
        entry.pack(pady=20, fill="x")

if __name__ == "__main__":
    app = SimpleCalculator()
    app.mainloop()