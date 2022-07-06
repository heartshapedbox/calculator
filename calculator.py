from tkinter import *
from tkinter import filedialog
import pyperclip
import json
import csv
import math

root = Tk()
root.title('Calculator')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
root.geometry('320x505+' + str(x) + '+' + str(y))
# root.attributes('-alpha', 0.95)
root.resizable(False, False)

class Calculator():
    def __init__(self):
        self.val = StringVar()
        self.log = StringVar()
        self.str = ''
        self.res = ''
        self.logVal = ''
        self.history = []
        self.window = Label(root, text = '', bg = '#1f1e24')
        self.window.place(width = 323, height = 508)

        self.logArea = Label(self.window, text = '', bg = '#1f1e24')
        self.logArea.place(x = 5, y = 55, width = 295, height = 45)
        self.logAreaMessage = Message(self.logArea, width = 300, textvariable = self.log, bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12))
        self.logAreaMessage.place(x = 7, y = 5)

        self.displayArea = Label(self.window, text = '', bg = '#1f1e24')
        self.displayArea.place(x = 5, y = 100, width = 300, height = 50)
        self.displayAreaMessage = Message(self.displayArea, width = 300, textvariable = self.val, bg = '#1f1e24', fg = '#f757a4', font = ('Consolas',22,'bold'))
        self.displayAreaMessage.place(x = -1, y = -5)

        self.button = Label(self.window, text = '', bg = '#1f1e24')
        self.button.place(x = -4, y = 153, width = 323, height = 355)

        self.historyButton = Button(self.window, text = '🕒', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.displayHistory())
        self.historyButton.place(x = 5, y = 5, width = 50, height = 50)
        self.historyButton['relief'] = 'flat'


        button__MC = Button(self.button, text = 'MC', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept('MC'))
        button__MC.place(x = 5, y = -3, width = 49, height = 25)
        button__MC['relief'] = 'flat'
        button__MR = Button(self.button, text = 'MR', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept('MR'))
        button__MR.place(x = 57, y = -3, width = 49, height = 25)
        button__MR['relief'] = 'flat'
        button__MRP = Button(self.button, text = 'MR+', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept('MR+'))
        button__MRP.place(x = 109, y = -3, width = 49, height = 25)
        button__MRP['relief'] = 'flat'
        button__MRN = Button(self.button, text = 'MR-', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept('MR-'))
        button__MRN.place(x = 162, y = -3, width = 49, height = 25)
        button__MRN['relief'] = 'flat'
        button__MS = Button(self.button, text = 'MS', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept('MS'))
        button__MS.place(x = 215, y = -3, width = 49, height = 25)
        button__MS['relief'] = 'flat'
        button__MM = Button(self.button, text = 'M▼', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept('M▼'))
        button__MM.place(x = 266, y = -3, width = 49, height = 25)
        button__MM['relief'] = 'flat'

        button__C = Button(self.button, text = '⌫', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.eraseLastChar())
        button__C.place(x = 5, y = 28, width = 75.25, height = 50)
        button__C['relief'] = 'flat'
        button__Percent = Button(self.button, text = '%', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.getPercent())
        button__Percent.place(x = 83.25, y = 28, width = 75.25, height = 50)
        button__Percent['relief'] = 'flat'
        button__Fraction = Button(self.button, text = '1/x', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.getFraction())
        button__Fraction.place(x = 161.5, y = 28, width = 75.25, height = 50)
        button__Fraction['relief'] = 'flat'
        button__Remove = Button(self.button, text = 'C', bg = '#363336', fg = '#f757a4', font = ('Consolas',14,'bold'), command = lambda:self.reset())
        button__Remove.place(x = 239.75, y = 28, width = 75.25, height = 50)
        button__Remove['relief'] = 'flat'

        button__PointLeft = Button(self.button, text = '<.', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.movePointLeft())
        button__PointLeft.place(x = 5, y = 81, width = 75.25, height = 50)
        button__PointLeft['relief'] = 'flat'
        button__Square = Button(self.button, text = 'x²', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.getSquare())
        button__Square.place(x = 83.25, y = 81, width = 75.25, height = 50)
        button__Square['relief'] = 'flat'
        button__SquareRoot = Button(self.button, text = '√x', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.getSquareRoot())
        button__SquareRoot.place(x = 161.5, y = 81, width = 75.25, height = 50)
        button__SquareRoot['relief'] = 'flat'
        button__Division = Button(self.button, text = '÷', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.accept('/'))
        button__Division.place(x = 239.75, y = 81, width = 75.25, height = 50)
        button__Division['relief'] = 'flat'

        button__7 = Button(self.button, text = '7', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(7))
        button__7.place(x = 5, y = 134, width = 75.25, height = 50)
        button__7['relief'] = 'flat'
        button__8 = Button(self.button, text = '8', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(8))
        button__8.place(x = 83.25, y = 134, width = 75.25, height = 50)
        button__8['relief'] = 'flat'
        button__9 = Button(self.button, text = '9', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(9))
        button__9.place(x = 161.5, y = 134, width = 75.25, height = 50)
        button__9['relief'] = 'flat'
        button__Multiplication = Button(self.button, text = '❌', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',8), command = lambda:self.accept('*'))
        button__Multiplication.place(x = 239.75, y = 134, width = 75.25, height = 50)
        button__Multiplication['relief'] = 'flat'

        button__4 = Button(self.button, text = '4', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(4))
        button__4.place(x = 5, y = 187, width = 75.25, height = 50)
        button__4['relief'] = 'flat'
        button__5 = Button(self.button, text = '5', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(5))
        button__5.place(x = 83.25, y = 187, width = 75.25, height = 50)
        button__5['relief'] = 'flat'
        button__6 = Button(self.button, text = '6', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(6))
        button__6.place(x = 161.5, y = 187, width = 75.25, height = 50)
        button__6['relief'] = 'flat'
        button__Substraction = Button(self.button, text = '-', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.accept('-'))
        button__Substraction.place(x = 239.75, y = 187, width = 75.25, height = 50)
        button__Substraction['relief'] = 'flat'

        button__1 = Button(self.button, text = '1', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(1))
        button__1.place(x = 5, y = 240, width = 75.25, height = 50)
        button__1['relief'] = 'flat'
        button__2 = Button(self.button, text = '2', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(2))
        button__2.place(x = 83.25, y = 240, width = 75.25, height = 50)
        button__2['relief'] = 'flat'
        button__3 = Button(self.button, text = '3', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(3))
        button__3.place(x = 161.5, y = 240, width = 75.25, height = 50)
        button__3['relief'] = 'flat'
        button__Addition = Button(self.button, text = '+', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.accept('+'))
        button__Addition.place(x = 239.75, y = 240, width = 75.25, height = 50)
        button__Addition['relief'] = 'flat'

        button__PointRight = Button(self.button, text = '.>', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.movePointRight())
        button__PointRight.place(x = 5, y = 293, width = 75.25, height = 50)
        button__PointRight['relief'] = 'flat'
        button__0 = Button(self.button, text = '0', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept(0))
        button__0.place(x = 83.25, y = 293, width = 75.25, height = 50)
        button__0['relief'] = 'flat'
        button__Point = Button(self.button, text = '.', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.accept('.'))
        button__Point.place(x = 161.5, y = 293, width = 75.25, height = 50)
        button__Point['relief'] = 'flat'
        button__Result = Button(self.button, text = '=', bg = '#f757a4', fg = '#473d47', font = ('Consolas',20,'bold'), command = lambda:self.math('='))
        button__Result.place(x = 239.75, y = 293, width = 75.25, height = 50)
        button__Result['relief'] = 'flat'
    
    
    def accept(self,i):
        if self.str == '0' and i == 0:
            self.reset()
        elif len(self.str) > 16:
            self.reset()
        else:
            self.display(i)
            

    def display(self, i):
            self.str += str(i)
            self.val.set(self.str)


    def displayHistory(self):
        # add history area
        self.historyLabel = Label(self.window, text = '', bg = '#1f1e24', fg = '#f0ebf0')
        self.historyLog = Message(self.historyLabel, text = '', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), width = 200)
        self.historyLabel.place(y = 60, width = 323, height = 450)
        self.historyLog.place(x = 12, y = 0)
        self.historyLog['text'] = ('\n'.join(i for i in self.history))
        self.historyButton['bg'] = '#1f1e24'

        # add close history button
        self.button__closeHistory = Button(self.window, text = 'x', bg = '#1f1e24', fg = '#f757a4', font = ('Consolas',12), command = lambda:self.closeHistory())
        self.button__closeHistory.place(x = 260, y = 5, width = 50, height = 50)
        self.button__closeHistory['relief'] = 'flat'

        # copy history
        self.button__copyHistory = Button(self.window, text = '📑\ncopy', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.copyHistory())
        self.button__copyHistory.place(x = 5, y = 5, width = 50, height = 50)
        self.button__copyHistory['relief'] = 'flat'

        # save history to .txt file
        self.button__saveToTXT = Button(self.window, text = '💾\ntxt', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.saveToTXT())
        self.button__saveToTXT.place(x = 55, y = 5, width = 50, height = 50)
        self.button__saveToTXT['relief'] = 'flat'

        # save history to .json file
        self.button__saveToJSON = Button(self.window, text = '💾\njson', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.saveToJSON())
        self.button__saveToJSON.place(x = 105, y = 5, width = 50, height = 50)
        self.button__saveToJSON['relief'] = 'flat'

        # save history to .csv file
        self.button__saveToCSV = Button(self.window, text = '💾\ncsv', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.saveToCSV())
        self.button__saveToCSV.place(x = 155, y = 5, width = 50, height = 50)
        self.button__saveToCSV['relief'] = 'flat'

        # clean history
        self.button__cleanHistory = Button(self.window, text = '🧽\nclean', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.cleanHistory())
        self.button__cleanHistory.place(x = 205, y = 5, width = 50, height = 50)
        self.button__cleanHistory['relief'] = 'flat'

        # remove history button
        self.historyButton.destroy()


    def closeHistory(self):
        self.historyLabel.destroy()
        self.historyLog.destroy()
        self.button__closeHistory.destroy()
        self.button__cleanHistory.destroy()
        self.button__copyHistory.destroy()
        self.button__saveToCSV.destroy()
        self.button__saveToTXT.destroy()
        self.button__saveToJSON.destroy()
        self.historyButton = Button(self.window, text = '🕒', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.displayHistory())
        self.historyButton.place(x = 5, y = 5, width = 50, height = 50)
        self.historyButton['relief'] = 'flat'


    def cleanHistory(self):
        self.historyLog['text'] = ""
        self.history = []


    def copyHistory(self):
        pyperclip.copy(self.historyLog['text'])


    def saveToCSV(self):
        filename =  filedialog.asksaveasfilename(initialdir = "/", title = "Save as", initialfile = 'calculator_log', filetypes = (("csv files","*.csv"),("all files","*.*")))
        with open(f'{filename}.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            for i in self.history:
                writer.writerow([i])


    def saveToTXT(self):
        filename =  filedialog.asksaveasfilename(initialdir = "/", title = "Save as", initialfile = 'calculator_log', filetypes = (("txt files","*.txt"),("all files","*.*")))
        with open(f'{filename}.txt', 'w', newline = '') as file:
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
        filename =  filedialog.asksaveasfilename(initialdir = "/", title = "Save as", initialfile = 'calculator_log', filetypes = (("json files","*.json"),("all files","*.*")))
        with open(f'{filename}.json', 'w', encoding = 'utf-8') as file:
            json.dump(list, file, indent = 4, ensure_ascii = False)


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
        if self.val.get() != '0' and len(self.str) < 16:
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
        if self.val.get() != '0' and len(self.str) < 16:
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
                square = round(math.pow(int(self.val.get()),2), 5)
                self.str = (str(square))
                self.val.set(self.str)
                self.logVal = f'sqr({self.logVal}) = {self.str}'
                self.history.insert(0, self.logVal)
                self.logVal = ''
                self.log.set(self.history[0])
            except ValueError:
                try:
                    square = round(math.pow(float(self.val.get()),2), 5)
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
        operators_list = ['+','-','*','/']
        taken_operators = []
        output, expression_result, percent = '', '', ''
        for i in range(len(input), 1, -1):
            if input[i - 1] in operators_list:
                taken_operators.append(input[i - 1])
                expression = input.split(taken_operators[0])[0]
                multiplier = input.split(taken_operators[0])[-1]
                expression_result = round(eval(expression), 5)
                percent = round(eval(f'{expression_result} * {multiplier} / 100'), 5)
                output = f'{expression_result}{taken_operators[0]}{percent}'
                self.str = output
                self.val.set(self.str)

if __name__ == '__main__':
    calculator = Calculator().reset()

root.mainloop()