import tkinter
import tkinter.messagebox

class TemperatureConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Converter")

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Верхние виджеты
        self.prompt_label = tkinter.Label(self.top_frame, text = "Введите температуру в градусах по Цельсию:")
        self.temp_entry = tkinter.Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side="left")
        self.temp_entry.pack(side="left")

        # Серединные виджеты
        self.descr_label = tkinter.Label(self.mid_frame, text="Преобразовано в градусы по Фаренгейту:")

        self.value = tkinter.StringVar()
        self.celsius_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        self.descr_label.pack(side = "left")
        self.celsius_label.pack(side = "left")

        # Нижние виджеты
        self.calc_button = tkinter.Button(self.main_window, text="Преобразовать", command=self.convert)
        self.quit_button = tkinter.Button(self.main_window, text="Выйти", command=self.main_window.destroy)

        self.quit_button.pack(side="bottom")
        self.calc_button.pack(side="bottom")

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        celsius = float(self.temp_entry.get())
        fr = (celsius * 9 / 5) + 32

        self.value.set(str(fr))

if __name__ == '__main__':
    temp_conv = TemperatureConverterGUI()
