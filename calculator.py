from tkinter import *
from tkinter import filedialog
import pyperclip
import json
import csv
import math
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\calculator\\')

root = Tk()
root.title('Calculator')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
x, y = str(x), str(y)
root.geometry(f'320x505+{x}+{y}')
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
        
        self.background = '#1f1e24'
        self.foreground = '#f0ebf0'
        self.foreground2 = '#f757a4'
        self.buttonbackground1 = '#473d47'
        self.buttonbackground2 = '#363336'
        self.buttonforeground = '#f0ebf0'
        self.buttonactivebackground = '#262426'
        self.font = ('Consolas', 12)
        
        self.window = Label(root, text = '', bg = self.background)
        self.window.place(width = 323, height = 508)

        self.logArea = Label(self.window, text = '', bg = self.background)
        self.logArea.place(x = 5, y = 55, width = 295, height = 45)
        self.logAreaMessage = Message(self.logArea, width = 300, textvariable = self.log, bg = self.background, fg = self.foreground, font = self.font)
        self.logAreaMessage.place(x = 7, y = 5)

        self.displayArea = Label(self.window, text = '', bg = self.background)
        self.displayArea.place(x = 5, y = 100, width = 300, height = 50)
        self.displayAreaMessage = Message(self.displayArea, width = 300, textvariable = self.val, bg = self.background, fg = self.foreground2, font = ('Consolas', 22,'bold'))
        self.displayAreaMessage.place(x = -1, y = -5)

        self.button = Label(self.window, text = '', bg = self.background)
        self.button.place(x = -4, y = 153, width = 323, height = 355)

        self.historyButton = Button(self.window, text = '🕒', command = lambda:self.displayHistory())
        self.historyButton.configure(
            background = self.background,
            foreground = self.foreground,
            font = ('Consolas', 20),
            relief = 'flat',
            activebackground = self.buttonactivebackground,
            activeforeground = self.foreground
        )
        self.hover(self.historyButton, self.buttonactivebackground, self.background, self.foreground, self.foreground)
        self.historyButton.place(x = 5, y = 5, width = 50, height = 50)
        


        # button__MC = Button(self.button, text = 'MC', bg = self.background, fg = self.foreground, font = self.font, command = lambda:self.accept('MC'))
        # button__MC.place(x = 5, y = -3, width = 49, height = 25)
        # button__MC['relief'] = 'flat'
        # button__MR = Button(self.button, text = 'MR', bg = self.background, fg = self.foreground, font = self.font, command = lambda:self.accept('MR'))
        # button__MR.place(x = 57, y = -3, width = 49, height = 25)
        # button__MR['relief'] = 'flat'
        # button__MRP = Button(self.button, text = 'MR+', bg = self.background, fg = self.foreground, font = self.font, command = lambda:self.accept('MR+'))
        # button__MRP.place(x = 109, y = -3, width = 49, height = 25)
        # button__MRP['relief'] = 'flat'
        # button__MRN = Button(self.button, text = 'MR-', bg = self.background, fg = self.foreground, font = self.font, command = lambda:self.accept('MR-'))
        # button__MRN.place(x = 162, y = -3, width = 49, height = 25)
        # button__MRN['relief'] = 'flat'
        # button__MS = Button(self.button, text = 'MS', bg = self.background, fg = self.foreground, font = self.font, command = lambda:self.accept('MS'))
        # button__MS.place(x = 215, y = -3, width = 49, height = 25)
        # button__MS['relief'] = 'flat'
        # button__MM = Button(self.button, text = 'M▼', bg = self.background, fg = self.foreground, font = self.font, command = lambda:self.accept('M▼'))
        # button__MM.place(x = 266, y = -3, width = 49, height = 25)
        # button__MM['relief'] = 'flat'
            
        self.button__C = Button(self.button, text = '⌫', command = lambda:self.eraseLastChar())
        self.button__C.place(x = 5, y = 28, width = 75.25, height = 50)
        self.button__Percent = Button(self.button, text = '%', command = lambda:self.getPercent())
        self.button__Percent.place(x = 83.25, y = 28, width = 75.25, height = 50)
        self.button__Fraction = Button(self.button, text = '1/x', command = lambda:self.getFraction())
        self.button__Fraction.place(x = 161.5, y = 28, width = 75.25, height = 50)
        self.button__Remove = Button(self.button, text = 'C', command = lambda:self.reset())
        self.button__Remove.place(x = 239.75, y = 28, width = 75.25, height = 50)

        self.button__PointLeft = Button(self.button, text = '<.', command = lambda:self.movePointLeft())
        self.button__PointLeft.place(x = 5, y = 81, width = 75.25, height = 50)
        self.button__Square = Button(self.button, text = 'x²', command = lambda:self.getSquare())
        self.button__Square.place(x = 83.25, y = 81, width = 75.25, height = 50)
        self.button__SquareRoot = Button(self.button, text = '√x', command = lambda:self.getSquareRoot())
        self.button__SquareRoot.place(x = 161.5, y = 81, width = 75.25, height = 50)
        self.button__Division = Button(self.button, text = '÷', command = lambda:self.accept('/'))
        self.button__Division.place(x = 239.75, y = 81, width = 75.25, height = 50)

        self.button__7 = Button(self.button, text = '7', command = lambda:self.accept(7))
        self.button__7.place(x = 5, y = 134, width = 75.25, height = 50)
        self.button__8 = Button(self.button, text = '8', command = lambda:self.accept(8))
        self.button__8.place(x = 83.25, y = 134, width = 75.25, height = 50)
        self.button__9 = Button(self.button, text = '9', command = lambda:self.accept(9))
        self.button__9.place(x = 161.5, y = 134, width = 75.25, height = 50)
        self.button__Multiplication = Button(self.button, text = '❌', command = lambda:self.accept('*'))
        self.button__Multiplication.place(x = 239.75, y = 134, width = 75.25, height = 50)

        self.button__4 = Button(self.button, text = '4', command = lambda:self.accept(4))
        self.button__4.place(x = 5, y = 187, width = 75.25, height = 50)
        self.button__5 = Button(self.button, text = '5', command = lambda:self.accept(5))
        self.button__5.place(x = 83.25, y = 187, width = 75.25, height = 50)
        self.button__6 = Button(self.button, text = '6', command = lambda:self.accept(6))
        self.button__6.place(x = 161.5, y = 187, width = 75.25, height = 50)
        self.button__Substraction = Button(self.button, text = '-', command = lambda:self.accept('-'))
        self.button__Substraction.place(x = 239.75, y = 187, width = 75.25, height = 50)

        self.button__1 = Button(self.button, text = '1', command = lambda:self.accept(1))
        self.button__1.place(x = 5, y = 240, width = 75.25, height = 50)
        self.button__2 = Button(self.button, text = '2', command = lambda:self.accept(2))
        self.button__2.place(x = 83.25, y = 240, width = 75.25, height = 50)
        self.button__3 = Button(self.button, text = '3', command = lambda:self.accept(3))
        self.button__3.place(x = 161.5, y = 240, width = 75.25, height = 50)
        self.button__Addition = Button(self.button, text = '+', command = lambda:self.accept('+'))
        self.button__Addition.place(x = 239.75, y = 240, width = 75.25, height = 50)

        self.button__PointRight = Button(self.button, text = '.>', command = lambda:self.movePointRight())
        self.button__PointRight.place(x = 5, y = 293, width = 75.25, height = 50)
        self.button__0 = Button(self.button, text = '0', command = lambda:self.accept(0))
        self.button__0.place(x = 83.25, y = 293, width = 75.25, height = 50)
        self.button__Point = Button(self.button, text = '.', command = lambda:self.accept('.'))
        self.button__Point.place(x = 161.5, y = 293, width = 75.25, height = 50)
        self.button__Result = Button(self.button, text = '=', command = lambda:self.math('='))
        self.button__Result.place(x = 239.75, y = 293, width = 75.25, height = 50)
        
        # buttons style
        for i in (self.button__1, self.button__2, self.button__3, self.button__4, self.button__5, self.button__6, self.button__7, self.button__8, self.button__9, self.button__0, self.button__PointRight, self.button__Point):
            i.configure(
                background = self.buttonbackground1,
                foreground = self.buttonforeground,
                font = self.font,
                relief = 'flat',
                activebackground = self.buttonactivebackground,
                activeforeground = self.buttonforeground
            )
            self.hover(i, self.buttonactivebackground, self.buttonbackground1, self.buttonforeground, self.buttonforeground)
        
        
        for i in (self.button__C, self.button__Percent, self.button__Fraction, self.button__Remove, self.button__PointLeft, self.button__Square, self.button__SquareRoot):
            i.configure(
                background = self.buttonbackground2,
                foreground = self.buttonforeground,
                font = self.font,
                relief = 'flat',
                activebackground = self.buttonactivebackground,
                activeforeground = self.buttonforeground
            )
            self.hover(i, self.buttonactivebackground, self.buttonbackground2, self.buttonforeground, self.buttonforeground)
        
        
        for i in (self.button__Substraction, self.button__Addition, self.button__Division):
            i.configure(
                background = self.buttonbackground2,
                foreground = self.buttonforeground,
                font = ('Consolas', 20),
                relief = 'flat',
                activebackground = self.buttonactivebackground,
                activeforeground = self.buttonforeground
            )
            self.hover(i, self.buttonactivebackground, self.buttonbackground2, self.buttonforeground, self.buttonforeground)
            
        
        self.button__Remove.configure(
            background = self.buttonbackground2,
            foreground = self.foreground2,
            font = ('Consolas', 14,'bold'),
            relief = 'flat',
            activebackground = self.buttonactivebackground,
            activeforeground = self.foreground2
            )
        self.hover(self.button__Remove, self.buttonactivebackground, self.buttonbackground2, self.foreground2, self.foreground2)
        
        
        self.button__Result.configure(
                background = self.foreground2,
                foreground = self.buttonbackground1,
                font = ('Consolas', 20,'bold'),
                relief = 'flat',
                activebackground = self.buttonactivebackground,
                activeforeground = self.foreground2
            )
        self.hover(self.button__Result, self.buttonactivebackground, self.foreground2, self.foreground2, self.buttonbackground1)
        
        
        self.button__Multiplication.configure(
            background = self.buttonbackground2,
            foreground = self.buttonforeground,
            font = ('Consolas',8),
            relief = 'flat',
            activebackground = self.buttonactivebackground,
            activeforeground = self.buttonforeground
            )
        self.hover(self.button__Multiplication, self.buttonactivebackground, self.buttonbackground2, self.buttonforeground, self.buttonforeground)

    
    def hover(self, btn, colorOnHover, colorOnLeave, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.config(background = colorOnHover, foreground = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.config(background = colorOnLeave, foreground = colorfgOnLeave))
    # buttons style end
    
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
        self.historyLabel = Label(self.window, text = '', bg = self.background, fg = self.foreground)
        self.historyLog = Message(self.historyLabel, text = '', bg = self.background, fg = self.foreground, font = self.font, width = 200)
        self.historyLabel.place(y = 60, width = 323, height = 450)
        self.historyLog.place(x = 12, y = 0)
        self.historyLog['text'] = ('\n'.join(i for i in self.history))
        self.historyButton['bg'] = '#1f1e24'
        
        # add close history button
        self.button__closeHistory = Button(self.window, text = 'x', command = lambda:self.closeHistory())
        self.button__closeHistory.configure(
            background = self.background,
            foreground = self.foreground2,
            font = self.font,
            relief = 'flat',
            activebackground = self.buttonactivebackground,
            activeforeground = self.foreground2
        )
        self.hover(self.button__closeHistory, self.buttonactivebackground, self.background, self.foreground2, self.foreground2)
        self.button__closeHistory.place(x = 260, y = 5, width = 50, height = 50)

        # copy history
        self.button__copyHistory = Button(self.window, text = '📑\ncopy', command = lambda:self.copyHistory())
        self.button__copyHistory.place(x = 5, y = 5, width = 50, height = 50)

        # save history to .txt file
        self.button__saveToTXT = Button(self.window, text = '💾\ntxt', command = lambda:self.saveToTXT())
        self.button__saveToTXT.place(x = 55, y = 5, width = 50, height = 50)

        # save history to .json file
        self.button__saveToJSON = Button(self.window, text = '💾\njson', command = lambda:self.saveToJSON())
        self.button__saveToJSON.place(x = 105, y = 5, width = 50, height = 50)

        # save history to .csv file
        self.button__saveToCSV = Button(self.window, text = '💾\ncsv', command = lambda:self.saveToCSV())
        self.button__saveToCSV.place(x = 155, y = 5, width = 50, height = 50)

        # clean history
        self.button__cleanHistory = Button(self.window, text = '🧽\nclean', command = lambda:self.cleanHistory())
        self.button__cleanHistory.place(x = 205, y = 5, width = 50, height = 50)

        for i in (self.button__copyHistory, self.button__cleanHistory, self.button__saveToCSV, self.button__saveToJSON, self.button__saveToTXT, self.copyHistory):
            i.configure(
                background = self.background,
                foreground = self.foreground,
                font = self.font,
                relief = 'flat',
                activebackground = self.buttonactivebackground,
                activeforeground = self.foreground
                )
            self.hover(i, self.buttonactivebackground, self.background, self.buttonforeground, self.buttonforeground)
        
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
        self.historyButton = Button(self.window, text = '🕒', command = lambda:self.displayHistory())
        self.historyButton.configure(
            background = self.background,
            foreground = self.foreground,
            font = ('Consolas', 20),
            relief = 'flat',
            activebackground = self.background,
            activeforeground = self.foreground
        )
        self.hover(self.historyButton, self.buttonactivebackground, self.background, self.foreground, self.foreground)
        self.historyButton.place(x = 5, y = 5, width = 50, height = 50)


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