from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('320x505')
root.resizable(False, False)

class Calculator():
    def __init__(self):
        self.val = StringVar()
        self.log = StringVar()
        self.str = ''
        self.res = ''
        self.logVal = ''
        self.his = []

        window = Label(root, text = '', bg = '#241e24')
        window.place(width = 323, height = 508)

        logScreen = Label(window, text = '', bg = '#241e24')
        logScreen.place(x = 18, y = 48, width = 297, height = 30)
        outputLS = Message(logScreen, width = 305, textvariable = self.log, bg = '#241e24', fg = '#363336', font = ('Lucida Console',10,'bold'))
        outputLS.place(y = 8)

        mainScreen = Label(window, text = '', bg = '#241e24')
        mainScreen.place(x = 8, y = 80, width = 307, height = 70)
        outputMS = Message(mainScreen, width = 300, textvariable = self.val, bg = '#241e24', fg = '#f0ebf0', font = ('Lucida Console',28,'bold'))
        outputMS.place(y = 8)
        
        btn = Label(window, text = '', bg = '#241e24')
        btn.place(x = -4, y = 153, width = 323, height = 355)

        btnHis = Button(window, text = '🕒', bg = '#241e24', fg = '#363336', font = ('Lucida Console',20), command = lambda:self.displayHis(window, btn, btnHis, hisLabel, hisLog))
        btnHis.place(x = 20, y = 20, width = 25, height = 25)
        btnHis['relief'] = 'flat'
        
        btnMC = Button(btn, text = 'MC', bg = '#241e24', fg = '#363336', font = ('Lucida Console',12), command = lambda:self.display('MC'))
        btnMC.place(x = 2, y = -3, width = 49, height = 25)
        btnMC['relief'] = 'flat'
        btnMR = Button(btn, text = 'MR', bg = '#241e24', fg = '#363336', font = ('Lucida Console',12), command = lambda:self.display('MR'))
        btnMR.place(x = 57, y = -3, width = 49, height = 25)
        btnMR['relief'] = 'flat'
        btnMRP = Button(btn, text = 'MR+', bg = '#241e24', fg = '#363336', font = ('Lucida Console',12), command = lambda:self.display('MR+'))
        btnMRP.place(x = 109, y = -3, width = 49, height = 25)
        btnMRP['relief'] = 'flat'
        btnMRN = Button(btn, text = 'MR-', bg = '#241e24', fg = '#363336', font = ('Lucida Console',12), command = lambda:self.display('MR-'))
        btnMRN.place(x = 162, y = -3, width = 49, height = 25)
        btnMRN['relief'] = 'flat'
        btnMS = Button(btn, text = 'MS', bg = '#241e24', fg = '#363336', font = ('Lucida Console',12), command = lambda:self.display('MS'))
        btnMS.place(x = 214, y = -3, width = 49, height = 25)
        btnMS['relief'] = 'flat'
        btnMM = Button(btn, text = 'M▼', bg = '#241e24', fg = '#363336', font = ('Lucida Console',12), command = lambda:self.display('M▼'))
        btnMM.place(x = 266, y = -3, width = 49, height = 25)
        btnMM['relief'] = 'flat'

        btnPercent = Button(btn, text = '%', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display('%'))
        btnPercent.place(x = 5, y = 28, width = 75.25, height = 50)
        btnPercent['relief'] = 'flat'
        btnCE = Button(btn, text = 'CE', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display('CE'))
        btnCE.place(x = 83.25, y = 28, width = 75.25, height = 50)
        btnCE['relief'] = 'flat'
        btnC = Button(btn, text = 'C', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.reset())
        btnC.place(x = 161.5, y = 28, width = 75.25, height = 50)
        btnC['relief'] = 'flat'
        btnDel = Button(btn, text = '<', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display('<'))
        btnDel.place(x = 239.75, y = 28, width = 75.25, height = 50)
        btnDel['relief'] = 'flat'

        btnFr = Button(btn, text = '1/x', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display('1/x'))
        btnFr.place(x = 5, y = 81, width = 75.25, height = 50)
        btnFr['relief'] = 'flat'
        btnSq = Button(btn, text = 'x2', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display('*2'))
        btnSq.place(x = 83.25, y = 81, width = 75.25, height = 50)
        btnSq['relief'] = 'flat'
        btnSr = Button(btn, text = '√', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display('√'))
        btnSr.place(x = 161.5, y = 81, width = 75.25, height = 50)
        btnSr['relief'] = 'flat'
        btnDiv = Button(btn, text = '÷', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',18), command = lambda:self.display('/'))
        btnDiv.place(x = 239.75, y = 81, width = 75.25, height = 50)
        btnDiv['relief'] = 'flat'

        btn7 = Button(btn, text = '7', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(7))
        btn7.place(x = 5, y = 134, width = 75.25, height = 50)
        btn7['relief'] = 'flat'
        btn8 = Button(btn, text = '8', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(8))
        btn8.place(x = 83.25, y = 134, width = 75.25, height = 50)
        btn8['relief'] = 'flat'
        btn9 = Button(btn, text = '9', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(9))
        btn9.place(x = 161.5, y = 134, width = 75.25, height = 50)
        btn9['relief'] = 'flat'
        btnMul = Button(btn, text = 'x', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',18), command = lambda:self.display('*'))
        btnMul.place(x = 239.75, y = 134, width = 75.25, height = 50)
        btnMul['relief'] = 'flat'

        btn4 = Button(btn, text = '4', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(4))
        btn4.place(x = 5, y = 187, width = 75.25, height = 50)
        btn4['relief'] = 'flat'
        btn5 = Button(btn, text = '5', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(5))
        btn5.place(x = 83.25, y = 187, width = 75.25, height = 50)
        btn5['relief'] = 'flat'
        btn6 = Button(btn, text = '6', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(6))
        btn6.place(x = 161.5, y = 187, width = 75.25, height = 50)
        btn6['relief'] = 'flat'
        btnSub = Button(btn, text = '-', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',18), command = lambda:self.display('-'))
        btnSub.place(x = 239.75, y = 187, width = 75.25, height = 50)
        btnSub['relief'] = 'flat'

        btn1 = Button(btn, text = '1', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(1))
        btn1.place(x = 5, y = 240, width = 75.25, height = 50)
        btn1['relief'] = 'flat'
        btn2 = Button(btn, text = '2', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(2))
        btn2.place(x = 83.25, y = 240, width = 75.25, height = 50)
        btn2['relief'] = 'flat'
        btn3 = Button(btn, text = '3', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(3))
        btn3.place(x = 161.5, y = 240, width = 75.25, height = 50)
        btn3['relief'] = 'flat'
        btnAdd = Button(btn, text = '+', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console',18), command = lambda:self.display('+'))
        btnAdd.place(x = 239.75, y = 240, width = 75.25, height = 50)
        btnAdd['relief'] = 'flat'

        btnNeg = Button(btn, text = '+/-', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display('-'))
        btnNeg.place(x = 5, y = 293, width = 75.25, height = 50)
        btnNeg['relief'] = 'flat'
        btn0 = Button(btn, text = '0', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display(0))
        btn0.place(x = 83.25, y = 293, width = 75.25, height = 50)
        btn0['relief'] = 'flat'
        btnSep = Button(btn, text = '.', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console',12), command = lambda:self.display('.'))
        btnSep.place(x = 161.5, y = 293, width = 75.25, height = 50)
        btnSep['relief'] = 'flat'
        btnResult = Button(btn, text = '=', bg = '#f757a4', fg = '#362f36', font = ('Lucida Console',18), command = lambda:self.math('='))
        btnResult.place(x = 239.75, y = 293, width = 75.25, height = 50)
        btnResult['relief'] = 'flat'

        hisLabel = Label(btn, text = '', bg = '#241e24', fg = '#f0ebf0')
        hisLog = Message(hisLabel, text = '', bg = '#241e24', fg = '#f0ebf0', font = ('Lucida Console',12,'bold'), width = 200)
        
    def display(self, i):
            self.str += str(i)
            self.val.set(self.str)
    
    def displayHis(self, window, btn, btnHis, hisLabel, hisLog):
        hisLabel.place(width = 323, height = 355)
        hisLog.place(x = 10)
        hisLog['text'] = ('\n\n'.join(i for i in self.his))
        window['bg'] = '#241e24'
        btnHis['bg'] = '#241e24'
    
    def math(self, i):
        self.logVal += self.str
        
        self.res = eval(self.str)
        self.val.set(str(self.res))
        self.str = (str(self.res))
        
        self.logVal = f'{self.logVal}{i}{self.res}'
        self.his.insert(0, self.logVal)
        self.logVal = ''
        self.log.set(self.his[0])
        
    def reset(self):
        self.str = ''
        self.val.set(self.str)
        self.log.set(self.str)     

calculator = Calculator()
root.mainloop()