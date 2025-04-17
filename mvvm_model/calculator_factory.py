from tkinter import Button

class CalculatorButtonFactory:
    @staticmethod
    def create_button(master, text, row, col, width=5, height=2, command=None):
        return Button(master, text=text, font=("Arial", 18), width=width, height=height, command=command)