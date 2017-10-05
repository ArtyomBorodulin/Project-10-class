from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def padenie():
 def calc5():
    if int(intvar.get()) == 0:
        if len(str(e1.get())) == 0 or len(str(e4.get())) == 0:
            messagebox.showerror('Уклон реки Error','Введено недостаточное количество данных')
        else:
         e5.delete(0,END)
         a = float(e1.get())
         b = float(e4.get())
         b = b/1000;d = (b/a)*10000
         e5.insert(END,round(d,2))
    else:
        if len(str(e1.get())) == 0 or len(str(e2.get())) == 0 or len(str(e3.get())) == 0:
            messagebox.showerror('Уклон реки Error','Введено недостаточное количество данных')
        else:
         e5.delete(0,END)
         a = float(e1.get())
         b = float(e2.get())
         c = float(e3.get())
         b = abs(c-b)/1000;d = (b/a)*10000
         e5.insert(END,round(d,2))
#Обложка
 window = Tk()
 window.geometry('1150x550')
 window.title('Уклон реки')
 intvar = IntVar()

#Раздел функций
 def print1():
    t2.config(state = NORMAL);t3.config(state = NORMAL);e2.config(state = NORMAL);e3.config(state = NORMAL);t4.config(state = DISABLED);e4.config(state = DISABLED)
    if int(intvar.get()) == 0:
     e2.config(state = DISABLED);e3.config(state = DISABLED);t2.config(state = DISABLED);t3.config(state = DISABLED);t4.config(state = NORMAL);e4.config(state = NORMAL)
#Процедура вывода текста
 e1 = ttk.Entry(window,width = 10);e1.grid(row = 0,column = 1)
 t2 = ttk.Label(window,text = 'Введите высоту над уровнем моря у истока реки',font = 'times 12',state = DISABLED);t2.grid(row = 1,column = 0,sticky = 'W')
 t3 = ttk.Label(window,text = 'Введите высоту над уровнем моря у устья реки',font = 'times 12',state = DISABLED);t3.grid(row = 2,column = 0,sticky = 'W')
 e2 = ttk.Entry(window,width = 10,state = DISABLED);e2.grid(row = 1,column = 1,sticky = 'W')
 e3 = ttk.Entry(window,width = 10,state = DISABLED);e3.grid(row = 2,column  = 1,sticky = 'W')
 check_button = Checkbutton(window,variable = intvar,command = print1,text = 'В условии дана высота над уровнем моря у истока и устья',font = 'times 12',onvalue=1, offvalue=0);check_button.place(x = 0,y = 150)
 t4 = ttk.Label(window,text = 'Введите падение реки (м)',font = 'times 12');t4.grid(row = 3,column = 0,sticky = 'W')
 e4 = ttk.Entry(window,width = 10);e4.grid(row = 3,column = 1)
 b = ttk.Button(window,text = 'Вычислить',width = 15,command = calc5);b.grid(row = 5,column = 0,sticky = 'W')
 t5 = ttk.Label(window,text = 'Уклон реки (в промилле)',font = 'times 12');t5.grid(row = 4,column = 0,sticky = 'W')
 e5 = ttk.Entry(window,width = 10);e5.grid(row = 4,column = 1)
 #текст
 t1 = ttk.Label(window,text = 'Введите длину реки (км)',font = 'times 12');t1.grid(row = 0,column = 0,sticky = 'W')
 window.mainloop()

root = Tk()
root.geometry('500x550')
root.title('1 вкладка')
function7 = ttk.Button(root,text = 'Падение реки',width = 40,command = padenie);function7.grid(row = 6,column = 0,pady = 5,sticky = 'W')
root.mainloop()
