import tkinter
import tkinter.messagebox

class GPAgui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("GPA counter")

        self.grade_1 = tkinter.Frame()
        self.grade_2 = tkinter.Frame()
        self.grade_3 = tkinter.Frame()
        self.average_grade = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        # Оценка №1
        self.label_1 = tkinter.Label(self.grade_1, text="Ввести экзаменационную оценку №1:")
        self.entry_1 = tkinter.Entry(self.grade_1, width=10)
        self.label_1.pack(side="left")
        self.entry_1.pack(side="left")

        # Оценка №2
        self.label_2 = tkinter.Label(self.grade_2, text="Ввести экзаменационную оценку №2:")
        self.entry_2 = tkinter.Entry(self.grade_2, width=10)
        self.label_2.pack(side="left")
        self.entry_2.pack(side="left")

        # Оценка №3
        self.label_3 = tkinter.Label(self.grade_3, text="Ввести экзаменационную оценку №3:")
        self.entry_3 = tkinter.Entry(self.grade_3, width=10)
        self.label_3.pack(side="left")
        self.entry_3.pack(side="left")

        # Средний балл
        self.average_value = tkinter.Label(self.average_grade, text="Средний балл")
        self.value = tkinter.StringVar()
        self.avg = tkinter.Label(self.average_grade, textvariable=self.value)

        self.average_value.pack(side="left")
        self.avg.pack(side="left")

        # Усреднить и выйти КНОПКИ!!!
        self.counter_button = tkinter.Button(self.main_window, text="Усреднить", command=self.AVG_counter_function)
        self.quit_button = tkinter.Button(self.main_window, text="Выйти", command=self.main_window.destroy)

        self.quit_button.pack(side="bottom")
        self.counter_button.pack(side="bottom")

        self.grade_1.pack()
        self.grade_2.pack()
        self.grade_3.pack()
        self.average_grade.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def AVG_counter_function(self):
        grade1 = float(self.entry_1.get())
        grade2 = float(self.entry_2.get())
        grade3 = float(self.entry_3.get())
        total = (grade1 + grade2 + grade3) / 3
        self.value.set(str(total))

if __name__ == '__main__':
    counter_GPA = GPAgui()