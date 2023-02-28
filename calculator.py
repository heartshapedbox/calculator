from tkinter import *
from tkinter import filedialog
from tktooltip import ToolTip
import customtkinter
import pyperclip
import json
import csv
import math
import os
os.chdir('C:\\Users\\Dima\\Documents\\GitHub\\calculator\\')
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')


root = customtkinter.CTk()
root.title('Calculator')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
x, y = str(x), str(y)
root.geometry(f'320x490+{x}+{y}')
# root.attributes('-alpha', 0.95)
root.resizable(False, False)
root.iconbitmap('assets\\logo.ico')


class Calculator():
    def __init__(self):
        self.val = StringVar()
        self.log = StringVar()
        self.str = ''
        self.res = ''
        self.logVal = ''
        self.history = []

        self.accent_color_1 = '#1f1e24'
        self.accent_color_2 = '#f0ebf0'
        self.accent_color_3 = '#f757a4'
        self.accent_color_4 = '#473d47'
        self.accent_color_5 = '#363336'
        self.accent_color_6 = '#f0ebf0'
        self.accent_color_7 = '#262426'
        self.font = ('Consolas', 18)

        self.window = Label(
            root, text='', bg=self.accent_color_1, width=323, height=508)
        self.window.pack()

        self.logArea = Label(self.window, text='',
                             bg=self.accent_color_1, width=295, height=45)
        self.logArea.place(x=5, y=60)
        self.logAreaMessage = Message(self.logArea, width=600, textvariable=self.log,
                                      bg=self.accent_color_1, fg=self.accent_color_4, font=('Consolas', 20))
        self.logAreaMessage.place(x=7, y=55)

        self.displayArea = Label(self.window, text='',
                                 bg=self.accent_color_1, width=600, height=50)
        self.displayArea.place(x=5, y=170)
        self.displayAreaMessage = Message(self.displayArea, width=600, textvariable=self.val,
                                          bg=self.accent_color_1, fg=self.accent_color_3, font=('Consolas', 36, 'bold'))
        self.displayAreaMessage.place(x=-1, y=10)

        self.button = Label(self.window, text='',
                            bg=self.accent_color_1, width=323, height=355)
        self.button.place(x=-4, y=245)
        self.button_Remove = customtkinter.CTkButton(self.button, text='⌫', font=(
            'Consolas', 14), width=75.25, height=50, command=lambda: self.eraseLastChar())
        self.button_Remove.place(x=5.5, y=28)
        self.button_Percent = customtkinter.CTkButton(
            self.button, text='%', font=self.font, width=75.25, height=50, command=lambda: self.getPercent())
        self.button_Percent.place(x=83.5, y=28)
        self.button_Fraction = customtkinter.CTkButton(
            self.button, text='1/x', font=self.font, width=75.25, height=50, command=lambda: self.getFraction())
        self.button_Fraction.place(x=162.4, y=28)
        self.button_C = customtkinter.CTkButton(self.button, text='C', font=(
            'Consolas', 18, 'bold'), width=75.25, height=50, command=lambda: self.reset())
        self.button_C.place(x=240, y=28)

        self.button_PointLeft = customtkinter.CTkButton(
            self.button, text='<.', font=self.font, width=75.25, height=50, command=lambda: self.movePointLeft())
        self.button_PointLeft.place(x=5.5, y=81)
        self.button_Square = customtkinter.CTkButton(
            self.button, text='x²', font=self.font, width=75.25, height=50, command=lambda: self.getSquare())
        self.button_Square.place(x=83.5, y=81)
        self.button_SquareRoot = customtkinter.CTkButton(
            self.button, text='√x', font=self.font, width=75.25, height=50, command=lambda: self.getSquareRoot())
        self.button_SquareRoot.place(x=162.4, y=81)
        self.button_Division = customtkinter.CTkButton(self.button, text='÷', font=(
            'Consolas', 20), width=75.25, height=50, command=lambda: self.accept('/'))
        self.button_Division.place(x=240, y=81)

        self.button_7 = customtkinter.CTkButton(
            self.button, text='7',  font=self.font, width=75.25, height=50, command=lambda: self.accept(7))
        self.button_7.place(x=5.5, y=134)
        self.button_8 = customtkinter.CTkButton(
            self.button, text='8',  font=self.font, width=75.25, height=50, command=lambda: self.accept(8))
        self.button_8.place(x=83.5, y=134)
        self.button_9 = customtkinter.CTkButton(
            self.button, text='9',  font=self.font, width=75.25, height=50, command=lambda: self.accept(9))
        self.button_9.place(x=162.4, y=134)
        self.button_Multiplication = customtkinter.CTkButton(self.button, text='❌', font=(
            'Consolas', 8), width=75.25, height=50, command=lambda: self.accept('*'))
        self.button_Multiplication.place(x=240, y=134)

        self.button_4 = customtkinter.CTkButton(
            self.button, text='4',  font=self.font, width=75.25, height=50, command=lambda: self.accept(4))
        self.button_4.place(x=5.5, y=187)
        self.button_5 = customtkinter.CTkButton(
            self.button, text='5',  font=self.font, width=75.25, height=50, command=lambda: self.accept(5))
        self.button_5.place(x=83.5, y=187)
        self.button_6 = customtkinter.CTkButton(
            self.button, text='6',  font=self.font, width=75.25, height=50, command=lambda: self.accept(6))
        self.button_6.place(x=162.4, y=187)
        self.button_Substraction = customtkinter.CTkButton(self.button, text='-', font=(
            'Consolas', 20), width=75.25, height=50, command=lambda: self.accept('-'))
        self.button_Substraction.place(x=240, y=187)

        self.button_1 = customtkinter.CTkButton(
            self.button, text='1', font=self.font, width=75.25, height=50, command=lambda: self.accept(1))
        self.button_1.place(x=5.5, y=240)
        self.button_2 = customtkinter.CTkButton(
            self.button, text='2', font=self.font, width=75.25, height=50, command=lambda: self.accept(2))
        self.button_2.place(x=83.5, y=240)
        self.button_3 = customtkinter.CTkButton(
            self.button, text='3', font=self.font, width=75.25, height=50, command=lambda: self.accept(3))
        self.button_3.place(x=162.4, y=240)
        self.button_Addition = customtkinter.CTkButton(self.button, text='+', font=(
            'Consolas', 20), width=75.25, height=50, command=lambda: self.accept('+'))
        self.button_Addition.place(x=240, y=240)

        self.button_PointRight = customtkinter.CTkButton(
            self.button, text='.>',  font=self.font, width=75.25, height=50, command=lambda: self.movePointRight())
        self.button_PointRight.place(x=5.5, y=293)
        self.button_0 = customtkinter.CTkButton(
            self.button, text='0',  font=self.font, width=75.25, height=50, command=lambda: self.accept(0))
        self.button_0.place(x=83.5, y=293)
        self.button_Point = customtkinter.CTkButton(
            self.button, text='.',  font=self.font, width=75.25, height=50, command=lambda: self.accept('.'))
        self.button_Point.place(x=162.4, y=293)
        self.button_Result = customtkinter.CTkButton(self.button, text='=', font=(
            'Consolas', 20, 'bold'), width=75.25, height=50, command=lambda: self.math('='))
        self.button_Result.place(x=240, y=293)

        self.historyButton = customtkinter.CTkButton(self.window, text='🕒', font=(
            'Consolas', 20), width=50, height=50, command=self.displayHistory)
        self.historyButton.configure(
            bg_color=self.accent_color_1,
            fg_color=self.accent_color_1,
            text_color=self.accent_color_3,
            hover_color=self.accent_color_7,
            corner_radius=8
        )
        self.historyButton.place(x=5, y=5)
        self.hover(self.historyButton, self.accent_color_4,
                   self.accent_color_3)
        self.tip_history = ToolTip(self.historyButton, msg='History', parent_kwargs={
                                   "bg": self.accent_color_4, "padx": 1, "pady": 1}, fg=self.accent_color_3, bg=self.accent_color_7, pady=5, delay=1)

        # buttons style
        for i in (self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7, self.button_8, self.button_9, self.button_0, self.button_PointRight, self.button_Point):
            i.configure(
                bg_color=self.accent_color_1,
                fg_color=self.accent_color_4,
                text_color=self.accent_color_6,
                hover_color=self.accent_color_7,
                corner_radius=5
            )
            self.hover(i, self.accent_color_4, self.accent_color_2)

        for i in (self.button_Remove, self.button_Percent, self.button_Fraction, self.button_PointLeft, self.button_Square, self.button_SquareRoot):
            i.configure(
                bg_color=self.accent_color_1,
                fg_color=self.accent_color_5,
                text_color=self.accent_color_6,
                hover_color=self.accent_color_7,
                corner_radius=5
            )
            self.hover(i, self.accent_color_4, self.accent_color_2)

        for i in (self.button_Substraction, self.button_Addition, self.button_Division):
            i.configure(
                bg_color=self.accent_color_1,
                fg_color=self.accent_color_5,
                text_color=self.accent_color_6,
                hover_color=self.accent_color_7,
                corner_radius=5
            )
            self.hover(i, self.accent_color_4, self.accent_color_2)

        self.button_C.configure(
            bg_color=self.accent_color_1,
            fg_color=self.accent_color_5,
            text_color=self.accent_color_3,
            hover_color=self.accent_color_7,
            corner_radius=5
        )
        self.hover(self.button_C, self.accent_color_4, self.accent_color_3)

        self.button_Result.configure(
            bg_color=self.accent_color_1,
            fg_color=self.accent_color_3,
            text_color=self.accent_color_4,
            hover_color=self.accent_color_7,
            corner_radius=5
        )
        self.hover(self.button_Result, self.accent_color_4,
                   self.accent_color_4)

        self.button_Multiplication.configure(
            bg_color=self.accent_color_1,
            fg_color=self.accent_color_5,
            text_color=self.accent_color_6,
            hover_color=self.accent_color_7,
            corner_radius=5
        )
        self.hover(self.button_Multiplication,
                   self.accent_color_4, self.accent_color_2)
    # buttons style end

    def hover(self, btn, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", btn.configure(text_color=colorfgOnHover))
        btn.bind("<Leave>", btn.configure(text_color=colorfgOnLeave))

    def accept(self, i):
        if self.str == '0' and i == 0:
            self.reset()
        elif len(self.str) > 18:
            self.reset()
        else:
            self.display(i)

    def display(self, i):
        self.str += str(i)
        self.val.set(self.str)

    def displayHistory(self):
        # add history area
        self.historyLabel = Label(self.window, text='', width=323,
                                  height=450, bg=self.accent_color_1, fg=self.accent_color_2)
        self.historyLog = Message(self.historyLabel, text='', bg=self.accent_color_1,
                                  fg=self.accent_color_4, font=('Consolas', 20), width=500)
        self.historyLabel.place(y=100)
        self.historyLog.place(x=12, y=16)
        self.historyLog['text'] = ('\n'.join(i for i in self.history))
        self.historyButton['bg'] = self.accent_color_1
        self.tip_history.destroy()

        # add close history button
        self.button_CloseHistory = customtkinter.CTkButton(
            self.window, text='x', font=self.font, width=50, height=50, command=self.closeHistory)
        self.button_CloseHistory.configure(
            bg_color=self.accent_color_1,
            fg_color=self.accent_color_1,
            text_color=self.accent_color_3,
            hover_color=self.accent_color_7,
            corner_radius=8
        )
        self.hover(self.button_CloseHistory,
                   self.accent_color_4, self.accent_color_3)
        self.button_CloseHistory.place(x=260, y=5)

        # copy history
        self.button_CopyHistory = customtkinter.CTkButton(self.window, text='📑\ncopy', font=(
            'Consolas', 12), width=50, height=50, command=self.copyHistory)
        self.button_CopyHistory.place(x=5, y=5)

        # save history to .txt file
        self.button_saveToTXT = customtkinter.CTkButton(self.window, text='💾\ntxt', font=(
            'Consolas', 12), width=50, height=50, command=self.saveToTXT)
        self.button_saveToTXT.place(x=55, y=5)

        # save history to .json file
        self.button_saveToJSON = customtkinter.CTkButton(self.window, text='💾\njson', font=(
            'Consolas', 12), width=50, height=50, command=self.saveToJSON)
        self.button_saveToJSON.place(x=105, y=5)

        # save history to .csv file
        self.button_saveToCSV = customtkinter.CTkButton(self.window, text='💾\ncsv', font=(
            'Consolas', 12), width=50, height=50, command=self.saveToCSV)
        self.button_saveToCSV.place(x=155, y=5)

        # clean history
        self.button_CleanHistory = customtkinter.CTkButton(self.window, text='🧽\nclean', font=(
            'Consolas', 12), width=50, height=50, command=self.cleanHistory)
        self.button_CleanHistory.place(x=205, y=5)

        for i in (self.button_CopyHistory, self.button_CleanHistory, self.button_saveToCSV, self.button_saveToJSON, self.button_saveToTXT):
            i.configure(
                bg_color=self.accent_color_1,
                fg_color=self.accent_color_1,
                text_color=self.accent_color_2,
                hover_color=self.accent_color_7,
                corner_radius=8
            )
            self.hover(i, self.accent_color_4, self.accent_color_2)

        self.tip_close_history = ToolTip(self.button_CloseHistory, msg='Close history', parent_kwargs={
                                         "bg": self.accent_color_4, "padx": 1, "pady": 1}, fg=self.accent_color_3, bg=self.accent_color_7, pady=5, delay=1)
        self.tip_copy_history = ToolTip(self.button_CopyHistory, msg='Copy history', parent_kwargs={
                                        "bg": self.accent_color_4, "padx": 1, "pady": 1}, fg=self.accent_color_3, bg=self.accent_color_7, pady=5, delay=1)
        self.tip_copy_history_txt = ToolTip(self.button_saveToTXT, msg='Save history to .txt file', parent_kwargs={
                                            "bg": self.accent_color_4, "padx": 1, "pady": 1}, fg=self.accent_color_3, bg=self.accent_color_7, pady=5, delay=1)
        self.tip_copy_history_json = ToolTip(self.button_saveToJSON, msg='Save history to .json file', parent_kwargs={
                                             "bg": self.accent_color_4, "padx": 1, "pady": 1}, fg=self.accent_color_3, bg=self.accent_color_7, pady=5, delay=1)
        self.tip_copy_history_csv = ToolTip(self.button_saveToCSV, msg='Save history to .csv file', parent_kwargs={
                                            "bg": self.accent_color_4, "padx": 1, "pady": 1}, fg=self.accent_color_3, bg=self.accent_color_7, pady=5, delay=1)
        self.tip_clean_history = ToolTip(self.button_CleanHistory, msg='Remove history', parent_kwargs={
                                         "bg": self.accent_color_4, "padx": 1, "pady": 1}, fg=self.accent_color_3, bg=self.accent_color_7, pady=5, delay=1)

        # remove history button
        self.historyButton.destroy()
        self.tip_history.destroy()

    def closeHistory(self):
        for i in (self.historyLabel, self.historyLog, self.button_CloseHistory, self.button_CleanHistory, self.button_CopyHistory, self.button_saveToCSV, self.button_saveToTXT, self.button_saveToJSON, self.tip_clean_history, self.tip_close_history, self.tip_copy_history_csv, self.tip_copy_history_json, self.tip_copy_history_txt):
            i.destroy()
        self.historyButton = customtkinter.CTkButton(self.window, text='🕒', font=(
            'Consolas', 16), width=50, height=50, command=self.displayHistory)
        self.historyButton.configure(
            bg_color=self.accent_color_1,
            fg_color=self.accent_color_1,
            text_color=self.accent_color_3,
            hover_color=self.accent_color_7,
            corner_radius=5
        )
        self.hover(self.historyButton, self.accent_color_4,
                   self.accent_color_3)
        self.historyButton.place(x=5, y=5)
        self.tip_history = ToolTip(self.historyButton, msg='History', parent_kwargs={
                                   "bg": self.accent_color_4, "padx": 1, "pady": 1}, fg=self.accent_color_3, bg=self.accent_color_7, pady=5, delay=1)

    def cleanHistory(self):
        self.historyLog['text'] = ""
        self.history = []

    def copyHistory(self):
        pyperclip.copy(self.historyLog['text'])

    def saveToCSV(self):
        filename = filedialog.asksaveasfilename(
            initialdir="/", title="Save as", initialfile='calculator_log', filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        with open(f'{filename}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for i in self.history:
                writer.writerow([i])

    def saveToTXT(self):
        filename = filedialog.asksaveasfilename(
            initialdir="/", title="Save as", initialfile='calculator_log', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        with open(f'{filename}.txt', 'w', newline='') as file:
            string = '\n'.join(str(i) for i in self.history)
            file.write(string)

    def saveToJSON(self):
        list = []
        for i in range(0, len(self.history)):
            list.append(
                {
                    f'{i + 1}': self.history[i]
                }
            )
        filename = filedialog.asksaveasfilename(
            initialdir="/", title="Save as", initialfile='calculator_log', filetypes=(("json files", "*.json"), ("all files", "*.*")))
        with open(f'{filename}.json', 'w', encoding='utf-8') as file:
            json.dump(list, file, indent=4, ensure_ascii=False)

    def math(self, i):
        try:
            self.logVal += self.str
            self.res = round(eval(self.str), 5)
            self.val.set(str(self.res))
            self.str = (str(self.res))
            self.logVal = f'{self.logVal} {i} {self.res}'
            self.history.insert(0, self.logVal)
            self.logVal = ''
            self.log.set(self.history[0])
        except SyntaxError:
            self.reset()
            self.logVal = ''

    def reset(self):
        self.str = ''
        self.val.set('0')
        self.log.set('0')

    def eraseLastChar(self):
        slicer = slice(0, -1)
        sliced = self.val.get()[slicer]
        self.val.set(sliced)
        self.str = self.val.get()
        if len(self.str) == 0:
            self.val.set('0')
            self.log.set('0')

    def movePointRight(self):
        if self.val.get() != '0' and len(self.str) < 18:
            try:
                moveRight = round(int(self.val.get()) * 10, 10)
                self.str = (str(moveRight))
                self.val.set(self.str)
            except ValueError:
                try:
                    moveRight = round(float(self.val.get()) * 10, 10)
                    self.str = (str(moveRight))
                    self.val.set(self.str)
                except ValueError:
                    self.reset()
        else:
            self.reset()

    def movePointLeft(self):
        if self.val.get() != '0' and len(self.str) < 18:
            try:
                moveLeft = round(int(self.val.get()) / 10, 10)
                self.str = (str(moveLeft))
                self.val.set(self.str)
            except ValueError:
                try:
                    moveLeft = round(float(self.val.get()) / 10, 10)
                    self.str = (str(moveLeft))
                    self.val.set(self.str)
                except ValueError:
                    self.reset()
        else:
            self.reset()

    def getSquareRoot(self):
        if self.val.get() != '0':
            try:
                self.logVal += self.str
                squareRoot = round(math.sqrt(int(self.val.get())), 5)
                self.str = (str(squareRoot))
                self.val.set(self.str)
                self.logVal = f'√({self.logVal}) = {self.str}'
                self.history.insert(0, self.logVal)
                self.logVal = ''
                self.log.set(self.history[0])
            except ValueError:
                try:
                    squareRoot = round(math.sqrt(float(self.val.get())), 5)
                    self.str = (str(squareRoot))
                    self.val.set(self.str)
                    self.logVal = f'√({self.logVal}) = {self.str}'
                    self.history.insert(0, self.logVal)
                    self.logVal = ''
                    self.log.set(self.history[0])
                except ValueError:
                    pass

    def getSquare(self):
        if self.val.get() != '0':
            try:
                self.logVal += self.str
                square = round(math.pow(int(self.val.get()), 2), 5)
                self.str = (str(square))
                self.val.set(self.str)
                self.logVal = f'sqr({self.logVal}) = {self.str}'
                self.history.insert(0, self.logVal)
                self.logVal = ''
                self.log.set(self.history[0])
            except ValueError:
                try:
                    square = round(math.pow(float(self.val.get()), 2), 5)
                    self.str = (str(square))
                    self.val.set(self.str)
                    self.logVal = f'sqr({self.logVal}) = {self.str}'
                    self.history.insert(0, self.logVal)
                    self.logVal = ''
                    self.log.set(self.history[0])
                except ValueError:
                    pass

    def getFraction(self):
        if self.val.get() != '0':
            try:
                self.logVal += self.str
                fraction = round(1 / int(self.val.get()), 5)
                self.str = (str(fraction))
                self.val.set(self.str)
                self.logVal = f'1/({self.logVal}) = {self.str}'
                self.history.insert(0, self.logVal)
                self.logVal = ''
                self.log.set(self.history[0])
            except ValueError:
                try:
                    fraction = round(1 / float(self.val.get()), 5)
                    self.str = (str(fraction))
                    self.val.set(self.str)
                    self.logVal = f'1/({self.logVal}) = {self.str}'
                    self.history.insert(0, self.logVal)
                    self.logVal = ''
                    self.log.set(self.history[0])
                except ValueError:
                    pass

    def getPercent(self):
        input = self.val.get()
        operators_list = ['+', '-', '*', '/']
        taken_operators = []
        output, expression_result, percent = '', '', ''
        for i in range(len(input), 1, -1):
            if input[i - 1] in operators_list:
                taken_operators.append(input[i - 1])
                expression = input.split(taken_operators[0])[0]
                multiplier = input.split(taken_operators[0])[-1]
                expression_result = round(eval(expression), 5)
                percent = round(
                    eval(f'{expression_result} * {multiplier} / 100'), 5)
                output = f'{expression_result}{taken_operators[0]}{percent}'
                self.str = output
                self.val.set(self.str)


if __name__ == '__main__':
    calculator = Calculator().reset()

root.mainloop()
