#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    import tkFileDialog
    import tkSimpleDialog
    import tkColorChooser  #askcolor()
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    import tkinter.filedialog as tkFileDialog
    import tkinter.simpledialog as tkSimpleDialog    #askstring()
    import tkinter.colorchooser as tkColorChooser  #askcolor()
import win32com.client as wincl
class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('386x230')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text1Var = StringVar(value='打开文本文档')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.021, rely=0.035, relwidth=0.79, relheight=0.109)

        self.Command1Var = StringVar(value='打开')
        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.top, text='打开', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.829, rely=0.035, relwidth=0.148, relheight=0.109)

        self.Text2Font = Font(font=('宋体',9))
        self.Text2 = Text(self.top, font=self.Text2Font)
        self.Text2.place(relx=0.021, rely=0.209, relwidth=0.956, relheight=0.63)
        self.Text2.insert('1.0','')

        self.Command2Var = StringVar(value='TEXT转语音')
        self.style.configure('TCommand2.TButton', font=('宋体',9))
        self.Command2 = Button(self.top, text='TEXT转语音', textvariable=self.Command2Var, command=self.Command2_Cmd, style='TCommand2.TButton')
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda : self.Command2Var.get()
        self.Command2.place(relx=0.249, rely=0.87, relwidth=0.541, relheight=0.109)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!   
        txt = self.Text2.get('1.0','end')
        text2Speech(str(txt))
def text2Speech(text): 
	speak = wincl.Dispatch("SAPI.SpVoice") 
	speak.Speak(text)
if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

