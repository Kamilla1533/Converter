import tkinter
import tkinter.messagebox

class TemperatureConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Converter")

        # Верхние виджеты
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text = "Введите температуру в Цельсиях:")
        self.temp_entry = tkinter.Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side="left")
        self.temp_entry.pack(side="left")

        # Нижние виджеты
        self.calc_button = tkinter.Button(self.main_window, text="Преобразовать", command=self.convert)
        self.quit_button = tkinter.Button(self.main_window, text="Выйти", command=self.main_window.destroy)

        self.quit_button.pack(side="bottom")
        self.calc_button.pack(side="bottom")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        celsius = float(self.temp_entry.get())
        fr = (celsius * 9 / 5) + 32
        tkinter.messagebox.showinfo("Результаты", str(celsius) + " градусов по Цельсию эквивалетно " + str(fr) + " градусам по Фаренгейту")

if __name__ == '__main__':
    temp_conv = TemperatureConverterGUI()
