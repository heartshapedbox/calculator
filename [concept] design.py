from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('323x508')
root.resizable(False, False)


window = Label(root, text = '', bg = '#241e24')
window.place(width = 323, height = 508)


# log area
logScreen = Label(root, text = '', bg = '#241e24')
logScreen.place(x = 8, y = 28, width = 307, height = 50)
outputLS = Message(logScreen, width = 307, text = 0, bg = '#241e24', fg = '#363336', font = ('Lucida Console', 12, 'bold'))
outputLS.place(y = 12)


#  display area
mainScreen = Label(root, text = '', bg = '#241e24')
mainScreen.place(x = 8, y = 80, width = 307, height = 70)
outputMS = Message(mainScreen, width = 300, text = 0, bg = '#241e24', fg = '#f0ebf0', font = ('Lucida Console', 28, 'bold'))
outputMS.place(y = 8)


# buttons design
btnMC = Button(window, text = 'MC', bg = '#241e24', fg = '#363336', font = ('Lucida Console', 12))
btnMC.place(x = 5, y = 158, width = 49, height = 20)
btnMC['relief'] = 'flat'
btnMR = Button(window, text = 'MR', bg = '#241e24', fg = '#363336', font = ('Lucida Console', 12))
btnMR.place(x = 57, y = 158, width = 49, height = 20)
btnMR['relief'] = 'flat'
btnMRP = Button(window, text = 'MR+', bg = '#241e24', fg = '#363336', font = ('Lucida Console', 12))
btnMRP.place(x = 109, y = 158, width = 49, height = 20)
btnMRP['relief'] = 'flat'
btnMRN = Button(window, text = 'MR-', bg = '#241e24', fg = '#363336', font = ('Lucida Console', 12))
btnMRN.place(x = 162, y = 158, width = 49, height = 20)
btnMRN['relief'] = 'flat'
btnMS = Button(window, text = 'MS', bg = '#241e24', fg = '#363336', font = ('Lucida Console', 12))
btnMS.place(x = 214, y = 158, width = 49, height = 20)
btnMS['relief'] = 'flat'
btnMM = Button(window, text = 'M▼', bg = '#241e24', fg = '#363336', font = ('Lucida Console', 12))
btnMM.place(x = 266, y = 158, width = 49, height = 20)
btnMM['relief'] = 'flat'

btnPercent = Button(window, text = '%', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnPercent.place(x = 5, y = 185, width = 75.25, height = 50)
btnPercent['relief'] = 'flat'
btnCE = Button(window, text = 'CE', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnCE.place(x = 83.25, y = 185, width = 75.25, height = 50)
btnCE['relief'] = 'flat'
btnC = Button(window, text = 'C', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnC.place(x = 161.5, y = 185, width = 75.25, height = 50)
btnC['relief'] = 'flat'
btnDel = Button(window, text = '<', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnDel.place(x = 239.75, y = 185, width = 75.25, height = 50)
btnDel['relief'] = 'flat'

btnFr = Button(window, text = '1/x', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnFr.place(x = 5, y = 238, width = 75.25, height = 50)
btnFr['relief'] = 'flat'
btnSq = Button(window, text = 'x2', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnSq.place(x = 83.25, y = 238, width = 75.25, height = 50)
btnSq['relief'] = 'flat'
btnSr = Button(window, text = '√', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnSr.place(x = 161.5, y = 238, width = 75.25, height = 50)
btnSr['relief'] = 'flat'
btnDiv = Button(window, text = '÷', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 18))
btnDiv.place(x = 239.75, y = 238, width = 75.25, height = 50)
btnDiv['relief'] = 'flat'

btn7 = Button(window, text = '7', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn7.place(x = 5, y = 291, width = 75.25, height = 50)
btn7['relief'] = 'flat'
btn8 = Button(window, text = '8', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn8.place(x = 83.25, y = 291, width = 75.25, height = 50)
btn8['relief'] = 'flat'
btn9 = Button(window, text = '9', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn9.place(x = 161.5, y = 291, width = 75.25, height = 50)
btn9['relief'] = 'flat'
btnMul = Button(window, text = 'x', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 18))
btnMul.place(x = 239.75, y = 291, width = 75.25, height = 50)
btnMul['relief'] = 'flat'

btn4 = Button(window, text = '4', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn4.place(x = 5, y = 344, width = 75.25, height = 50)
btn4['relief'] = 'flat'
btn5 = Button(window, text = '5', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn5.place(x = 83.25, y = 344, width = 75.25, height = 50)
btn5['relief'] = 'flat'
btn6 = Button(window, text = '6', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn6.place(x = 161.5, y = 344, width = 75.25, height = 50)
btn6['relief'] = 'flat'
btnSub = Button(window, text = '-', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 18))
btnSub.place(x = 239.75, y = 344, width = 75.25, height = 50)
btnSub['relief'] = 'flat'

btn1 = Button(window, text = '1', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn1.place(x = 5, y = 397, width = 75.25, height = 50)
btn1['relief'] = 'flat'
btn2 = Button(window, text = '2', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn2.place(x = 83.25, y = 397, width = 75.25, height = 50)
btn2['relief'] = 'flat'
btn3 = Button(window, text = '3', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn3.place(x = 161.5, y = 397, width = 75.25, height = 50)
btn3['relief'] = 'flat'
btnAdd = Button(window, text = '+', bg = '#363336', fg = '#f0ebf0', font = ('Lucida Console', 18))
btnAdd.place(x = 239.75, y = 397, width = 75.25, height = 50)
btnAdd['relief'] = 'flat'

btnNeg = Button(window, text = '+/-', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnNeg.place(x = 5, y = 450, width = 75.25, height = 50)
btnNeg['relief'] = 'flat'
btn0 = Button(window, text = '0', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btn0.place(x = 83.25, y = 450, width = 75.25, height = 50)
btn0['relief'] = 'flat'
btnSep = Button(window, text = '.', bg = '#362f36', fg = '#f0ebf0', font = ('Lucida Console', 12))
btnSep.place(x = 161.5, y = 450, width = 75.25, height = 50)
btnSep['relief'] = 'flat'
btnResult = Button(window, text = '=', bg = '#f757a4', fg = '#362f36', font = ('Lucida Console', 18))
btnResult.place(x = 239.75, y = 450, width = 75.25, height = 50)
btnResult['relief'] = 'flat'

root.mainloop()