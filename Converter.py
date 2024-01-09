import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Converter")

        # Верхние виджеты
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text = "Введите расстояние в км:")
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        # Нижние виджеты
        self.calc_button = tkinter.Button(self.main_window, text="Преобразовать", command=self.convert)
        self.quit_button = tkinter.Button(self.main_window, text="Выйти", command=self.main_window.destroy)

        self.quit_button.pack(side="bottom")
        self.calc_button.pack(side="bottom")


        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        tkinter.messagebox.showinfo("Результаты", str(kilo) + " километров эквивалетно " + str(miles) + " милям")

if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()