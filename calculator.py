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
        self.logArea.place(x = 5, y = 48, width = 297, height = 30)
        self.logAreaMessage = Message(self.logArea, width = 305, textvariable = self.log, bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12))
        self.logAreaMessage.place(y = 8)

        self.displayArea = Label(self.window, text = '', bg = '#1f1e24')
        self.displayArea.place(y = 80, width = 307, height = 70)
        self.displayAreaMessage = Message(self.displayArea, width = 300, textvariable = self.val, bg = '#1f1e24', fg = '#f757a4', font = ('Consolas',26,'bold'))
        self.displayAreaMessage.place(x = -6, y = 8)

        self.btn = Label(self.window, text = '', bg = '#1f1e24')
        self.btn.place(x = -4, y = 153, width = 323, height = 355)

        self.historyBtn = Button(self.window, text = '🕒', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.displayHistory())
        self.historyBtn.place(x = 5, y = 5, width = 35, height = 35)
        self.historyBtn['relief'] = 'flat'


        btnMC = Button(self.btn, text = 'MC', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display('MC'))
        btnMC.place(x = 2, y = -3, width = 49, height = 25)
        btnMC['relief'] = 'flat'
        btnMR = Button(self.btn, text = 'MR', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display('MR'))
        btnMR.place(x = 57, y = -3, width = 49, height = 25)
        btnMR['relief'] = 'flat'
        btnMRP = Button(self.btn, text = 'MR+', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display('MR+'))
        btnMRP.place(x = 109, y = -3, width = 49, height = 25)
        btnMRP['relief'] = 'flat'
        btnMRN = Button(self.btn, text = 'MR-', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display('MR-'))
        btnMRN.place(x = 162, y = -3, width = 49, height = 25)
        btnMRN['relief'] = 'flat'
        btnMS = Button(self.btn, text = 'MS', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display('MS'))
        btnMS.place(x = 212, y = -3, width = 49, height = 25)
        btnMS['relief'] = 'flat'
        btnMM = Button(self.btn, text = 'M▼', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display('M▼'))
        btnMM.place(x = 266, y = -3, width = 49, height = 25)
        btnMM['relief'] = 'flat'

        btnPercent = Button(self.btn, text = 'C', bg = '#363336', fg = '#f757a4', font = ('Consolas',16), command = lambda:self.reset())
        btnPercent.place(x = 5, y = 28, width = 75.25, height = 50)
        btnPercent['relief'] = 'flat'
        btnCE = Button(self.btn, text = '%', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display('%'))
        btnCE.place(x = 83.25, y = 28, width = 75.25, height = 50)
        btnCE['relief'] = 'flat'
        btnC = Button(self.btn, text = '1/x', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.getFraction())
        btnC.place(x = 161.5, y = 28, width = 75.25, height = 50)
        btnC['relief'] = 'flat'
        btnDel = Button(self.btn, text = '⌫', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.eraseLastChar())
        btnDel.place(x = 239.75, y = 28, width = 75.25, height = 50)
        btnDel['relief'] = 'flat'

        btnFr = Button(self.btn, text = '<.', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.movePointLeft())
        btnFr.place(x = 5, y = 81, width = 75.25, height = 50)
        btnFr['relief'] = 'flat'
        btnSq = Button(self.btn, text = 'x²', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.getSquare())
        btnSq.place(x = 83.25, y = 81, width = 75.25, height = 50)
        btnSq['relief'] = 'flat'
        btnSr = Button(self.btn, text = '√x', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.getSquareRoot())
        btnSr.place(x = 161.5, y = 81, width = 75.25, height = 50)
        btnSr['relief'] = 'flat'
        btnDiv = Button(self.btn, text = '÷', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.display('/'))
        btnDiv.place(x = 239.75, y = 81, width = 75.25, height = 50)
        btnDiv['relief'] = 'flat'

        btn7 = Button(self.btn, text = '7', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(7))
        btn7.place(x = 5, y = 134, width = 75.25, height = 50)
        btn7['relief'] = 'flat'
        btn8 = Button(self.btn, text = '8', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(8))
        btn8.place(x = 83.25, y = 134, width = 75.25, height = 50)
        btn8['relief'] = 'flat'
        btn9 = Button(self.btn, text = '9', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(9))
        btn9.place(x = 161.5, y = 134, width = 75.25, height = 50)
        btn9['relief'] = 'flat'
        btnMul = Button(self.btn, text = '❌', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',8), command = lambda:self.display('*'))
        btnMul.place(x = 239.75, y = 134, width = 75.25, height = 50)
        btnMul['relief'] = 'flat'

        btn4 = Button(self.btn, text = '4', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(4))
        btn4.place(x = 5, y = 187, width = 75.25, height = 50)
        btn4['relief'] = 'flat'
        btn5 = Button(self.btn, text = '5', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(5))
        btn5.place(x = 83.25, y = 187, width = 75.25, height = 50)
        btn5['relief'] = 'flat'
        btn6 = Button(self.btn, text = '6', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(6))
        btn6.place(x = 161.5, y = 187, width = 75.25, height = 50)
        btn6['relief'] = 'flat'
        btnSub = Button(self.btn, text = '-', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.display('-'))
        btnSub.place(x = 239.75, y = 187, width = 75.25, height = 50)
        btnSub['relief'] = 'flat'

        btn1 = Button(self.btn, text = '1', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(1))
        btn1.place(x = 5, y = 240, width = 75.25, height = 50)
        btn1['relief'] = 'flat'
        btn2 = Button(self.btn, text = '2', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(2))
        btn2.place(x = 83.25, y = 240, width = 75.25, height = 50)
        btn2['relief'] = 'flat'
        btn3 = Button(self.btn, text = '3', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(3))
        btn3.place(x = 161.5, y = 240, width = 75.25, height = 50)
        btn3['relief'] = 'flat'
        btnAdd = Button(self.btn, text = '+', bg = '#363336', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.display('+'))
        btnAdd.place(x = 239.75, y = 240, width = 75.25, height = 50)
        btnAdd['relief'] = 'flat'

        btnNeg = Button(self.btn, text = '.>', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.movePointRight())
        btnNeg.place(x = 5, y = 293, width = 75.25, height = 50)
        btnNeg['relief'] = 'flat'
        btn0 = Button(self.btn, text = '0', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display(0))
        btn0.place(x = 83.25, y = 293, width = 75.25, height = 50)
        btn0['relief'] = 'flat'
        btnSep = Button(self.btn, text = '.', bg = '#473d47', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.display('.'))
        btnSep.place(x = 161.5, y = 293, width = 75.25, height = 50)
        btnSep['relief'] = 'flat'
        btnResult = Button(self.btn, text = '=', bg = '#f757a4', fg = '#473d47', font = ('Consolas',20), command = lambda:self.math('='))
        btnResult.place(x = 239.75, y = 293, width = 75.25, height = 50)
        btnResult['relief'] = 'flat'


    def display(self, i):
        if len(self.str) < 13 and self.str != "00":
            self.str += str(i)
            self.val.set(self.str)
        else:
            self.reset()
            


    def displayHistory(self):
        # add history area
        self.historyLabel = Label(self.window, text = '', bg = '#1f1e24', fg = '#f0ebf0')
        self.historyLog = Message(self.historyLabel, text = '', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), width = 200)
        self.historyLabel.place(y = 60, width = 323, height = 450)
        self.historyLog.place(x = 5, y = -4)
        self.historyLog['text'] = ('\n'.join(i for i in self.history))
        self.historyBtn['bg'] = '#1f1e24'

        # add close history button
        self.closeHistoryBtn = Button(self.window, text = 'x', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.closeHistory())
        self.closeHistoryBtn.place(x = 277, y = 5, width = 35, height = 35)
        self.closeHistoryBtn['relief'] = 'flat'

        # copy history
        self.copyHistoryBtn = Button(self.window, text = '📑\ncopy', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.copyHistory())
        self.copyHistoryBtn.place(x = 5, y = 5, width = 50, height = 50)
        self.copyHistoryBtn['relief'] = 'flat'

        # save history to .txt file
        self.saveHistoryToTXTBtn = Button(self.window, text = '💾\ntxt', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.saveToTXT())
        self.saveHistoryToTXTBtn.place(x = 55, y = 5, width = 50, height = 50)
        self.saveHistoryToTXTBtn['relief'] = 'flat'

        # save history to .json file
        self.saveHistoryToJSONBtn = Button(self.window, text = '💾\njson', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.saveToJSON())
        self.saveHistoryToJSONBtn.place(x = 105, y = 5, width = 50, height = 50)
        self.saveHistoryToJSONBtn['relief'] = 'flat'

        # save history to .csv file
        self.saveHistoryToCSVBtn = Button(self.window, text = '💾\ncsv', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.saveToCSV())
        self.saveHistoryToCSVBtn.place(x = 155, y = 5, width = 50, height = 50)
        self.saveHistoryToCSVBtn['relief'] = 'flat'

        # clean history
        self.cleanHistoryBtn = Button(self.window, text = '🧽\nclean', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',12), command = lambda:self.cleanHistory())
        self.cleanHistoryBtn.place(x = 205, y = 5, width = 50, height = 50)
        self.cleanHistoryBtn['relief'] = 'flat'

        # remove history button
        self.historyBtn.destroy()


    def closeHistory(self):
        self.historyLabel.destroy()
        self.historyLog.destroy()
        self.closeHistoryBtn.destroy()
        self.cleanHistoryBtn.destroy()
        self.copyHistoryBtn.destroy()
        self.saveHistoryToCSVBtn.destroy()
        self.saveHistoryToTXTBtn.destroy()
        self.saveHistoryToJSONBtn.destroy()
        self.historyBtn = Button(self.window, text = '🕒', bg = '#1f1e24', fg = '#f0ebf0', font = ('Consolas',20), command = lambda:self.displayHistory())
        self.historyBtn.place(x = 5, y = 5, width = 35, height = 35)
        self.historyBtn['relief'] = 'flat'


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
        self.logVal += self.str
        self.res = round(eval(self.str), 5)
        self.val.set(str(self.res))
        self.str = (str(self.res))
        self.logVal = f'{self.logVal} {i} {self.res}'
        self.history.insert(0, self.logVal)
        self.logVal = ''
        self.log.set(self.history[0])


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
        if self.val.get() != '0':
            try:
                moveRight = round(int(self.val.get()) * 10, 4)
                self.str = (str(moveRight))
                self.val.set(self.str)
            except ValueError:
                try:
                    moveRight = round(float(self.val.get()) * 10, 4)
                    self.str = (str(moveRight))
                    self.val.set(self.str)
                except ValueError:
                    pass
    
    
    def movePointLeft(self):
        if self.val.get() != '0':
            try:
                moveLeft = round(int(self.val.get()) / 10, 4)
                self.str = (str(moveLeft))
                self.val.set(self.str)
            except ValueError:
                try:
                    moveLeft = round(float(self.val.get()) / 10, 4)
                    self.str = (str(moveLeft))
                    self.val.set(self.str)
                except ValueError:
                    pass

    
    def getSquareRoot(self):
        if self.val.get() != '0':
            try:
                self.logVal += self.str
                squareRoot = round(math.sqrt(int(self.val.get())), 4)
                self.str = (str(squareRoot))
                self.val.set(self.str)
                self.logVal = f'√({self.logVal}) = {self.str}'
                self.history.insert(0, self.logVal)
                self.logVal = ''
                self.log.set(self.history[0])
            except ValueError:
                try:
                    squareRoot = round(math.sqrt(float(self.val.get())), 4)
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
                square = round(math.pow(int(self.val.get()),2), 4)
                self.str = (str(square))
                self.val.set(self.str)
                self.logVal = f'sqr({self.logVal}) = {self.str}'
                self.history.insert(0, self.logVal)
                self.logVal = ''
                self.log.set(self.history[0])
            except ValueError:
                try:
                    square = round(math.pow(float(self.val.get()),2), 4)
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
                fraction = round(1 / int(self.val.get()), 4)
                self.str = (str(fraction))
                self.val.set(self.str)
                self.logVal = f'1/({self.logVal}) = {self.str}'
                self.history.insert(0, self.logVal)
                self.logVal = ''
                self.log.set(self.history[0])
            except ValueError:
                try:
                    fraction = round(1 / float(self.val.get()), 4)
                    self.str = (str(fraction))
                    self.val.set(self.str)
                    self.logVal = f'1/({self.logVal}) = {self.str}'
                    self.history.insert(0, self.logVal)
                    self.logVal = ''
                    self.log.set(self.history[0])
                except ValueError:
                    pass
        


calculator = Calculator().reset()
root.mainloop()