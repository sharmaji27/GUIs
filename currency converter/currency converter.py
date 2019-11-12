from tkinter import *
from tkinter import ttk

win =Tk()
win.title('currency converter')
win.configure(bg='#462066')

def clear():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)

def convert():
    if(indicator.get()=='AMERICA'):
        val = (amount.get()*0.014)
        e3.insert(0,str(val))
    elif (indicator.get() == 'DUBAI'):
        val = (amount.get() * 0.052)
        e3.insert(0, str(val))
    elif (indicator.get() == 'CHINA'):
        val = (amount.get() * 0.094)
        e3.insert(0, str(val))
    elif (indicator.get() == 'RUSSIA'):
        val = (amount.get() * 0.93)
        e3.insert(0, str(val))
    elif (indicator.get() == 'GERMANY'):
        val = (amount.get() * 0.012)
        e3.insert(0, str(val))
    elif (indicator.get() == 'THAILAND'):
        val = (amount.get() * 0.45)
        e3.insert(0, str(val))

amount = IntVar()

indicator = StringVar(value='\tchoose a country')
Label(text='CURRENCY CONVERTER!!!',font=('arial',30,'bold'),bg='#462066',fg='#FFB85F').grid(row=0,column=1)

Label(text='amount in INR',font=('arial',30,'bold'),bg='#462066',fg='#FFB85F').grid(row=1,sticky=W)
e1= Entry(width=30,font=('arial',30,'bold'),textvariable=amount)
e1.grid(row=1,column=1)

Label(text='choose country',font=('arial',30,'bold'),bg='#462066',fg='#FFB85F').grid(row=2,sticky=W)
e2= ttk.Combobox(width=29,font=('arial',30,'bold'),textvariable=indicator)
e2['values']=('AMERICA','DUBAI','RUSSIA','CHINA','GERMANY','THAILAND')
e2.grid(row=2,column=1)

Label(text='in selected currency',font=('arial',30,'bold'),bg='#462066',fg='#FFB85F').grid(row=3,sticky=W)
e3= Entry(width=30,font=('arial',30,'bold'))
e3.grid(row=3,column=1)

clear()

Button(text='CONVERT',font=('arial',30,'bold'),width=15,bg='green',fg='yellow',command=convert).grid(row=4,column=1,sticky=W)
Button(text='CLEAR',font=('arial',30,'bold'),width=15,bg='green',fg='yellow',command=clear).grid(row=4,column=1,sticky=E)

win.mainloop()