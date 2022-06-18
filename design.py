from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('323x508')


window = Label(master = root, text = '', bg = '#241e24')
window.place(width = 323, height = 508)


btnPercent = Button(master = window, text = '%', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnPercent.place(x = 5, y = 185, width = 75.25, height = 50)
btnPercent['relief'] = 'flat'
btnCE = Button(master = window, text = 'CE', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnCE.place(x = 83.25, y = 185, width = 75.25, height = 50)
btnCE['relief'] = 'flat'
btnC = Button(master = window, text = 'C', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnC.place(x = 161.5, y = 185, width = 75.25, height = 50)
btnC['relief'] = 'flat'
btnDel = Button(master = window, text = '<', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnDel.place(x = 239.75, y = 185, width = 75.25, height = 50)
btnDel['relief'] = 'flat'

btnFr = Button(master = window, text = '1/x', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnFr.place(x = 5, y = 238, width = 75.25, height = 50)
btnFr['relief'] = 'flat'
btnSq = Button(master = window, text = 'x2', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnSq.place(x = 83.25, y = 238, width = 75.25, height = 50)
btnSq['relief'] = 'flat'
btnSr = Button(master = window, text = '√', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnSr.place(x = 161.5, y = 238, width = 75.25, height = 50)
btnSr['relief'] = 'flat'
btnDiv = Button(master = window, text = '÷', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnDiv.place(x = 239.75, y = 238, width = 75.25, height = 50)
btnDiv['relief'] = 'flat'

btn7 = Button(master = window, text = '7', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn7.place(x = 5, y = 291, width = 75.25, height = 50)
btn8 = Button(master = window, text = '8', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn8.place(x = 83.25, y = 291, width = 75.25, height = 50)
btn9 = Button(master = window, text = '9', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn9.place(x = 161.5, y = 291, width = 75.25, height = 50)
btnMul = Button(master = window, text = '×', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnMul.place(x = 239.75, y = 291, width = 75.25, height = 50)

btn4 = Button(master = window, text = '4', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn4.place(x = 5, y = 344, width = 75.25, height = 50)
btn5 = Button(master = window, text = '5', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn5.place(x = 83.25, y = 344, width = 75.25, height = 50)
btn6 = Button(master = window, text = '6', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn6.place(x = 161.5, y = 344, width = 75.25, height = 50)
btnSub = Button(master = window, text = '-', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnSub.place(x = 239.75, y = 344, width = 75.25, height = 50)

btn1 = Button(master = window, text = '1', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn1.place(x = 5, y = 397, width = 75.25, height = 50)
btn2 = Button(master = window, text = '2', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn2.place(x = 83.25, y = 397, width = 75.25, height = 50)
btn3 = Button(master = window, text = '3', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn3.place(x = 161.5, y = 397, width = 75.25, height = 50)
btnAdd = Button(master = window, text = '+', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnAdd.place(x = 239.75, y = 397, width = 75.25, height = 50)

btnNeg = Button(master = window, text = '+/-', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnNeg.place(x = 5, y = 450, width = 75.25, height = 50)
btn0 = Button(master = window, text = '0', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn0.place(x = 83.25, y = 450, width = 75.25, height = 50)
btnSep = Button(master = window, text = '.', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnSep.place(x = 161.5, y = 450, width = 75.25, height = 50)
btnResult = Button(master = window, text = '=', bg = '#f757a4', fg = '#362f36', font = ('Lucida Console', 12))
btnResult.place(x = 239.75, y = 450, width = 75.25, height = 50)

window.mainloop()