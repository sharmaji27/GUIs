from tkinter import *

win=Tk()
win.title('area')
win.configure(bg='yellow')
l=IntVar()
h=IntVar()

def calculate():
    l1=l.get()
    h1=h.get()
    area=l1*h1
    e3.insert(0,str(area))

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)



Label(text='Area of a rectangle',pady=20,font=('arial',30,'bold'),fg='black',bg='yellow').grid(row=0,column=1)

Label(text='LENGTH',padx=130,font=('arial',30,'bold'),bg='black',fg='white').grid(row=1,sticky=W)
e1= Entry(width=30,font=('arial',30,'bold'),textvariable=l)
e1.grid(row=1,column=1)

Label(text='HEIGHT',padx=137,font=('arial',30,'bold'),bg='black',fg='white').grid(row=2,sticky=W)
e2= Entry(width=30,font=('arial',30,'bold'),textvariable=h)
e2.grid(row=2,column=1)

Label(text='CALCULATED AREA',padx=17,font=('arial',30,'bold'),bg='black',fg='white').grid(row=3,sticky=W)
e3= Entry(width=30,font=('arial',30,'bold'))
e3.grid(row=3,column=1)

clear()

Button(text='calculate',font=('arial',30,'bold'),width=15,command=calculate,bg='green',fg='yellow').grid(row=4,column=1,sticky=W)
Button(text='clear',font=('arial',30,'bold'),width=15,command=clear,bg='green',fg='yellow').grid(row=4,column=1,sticky=E)

win.mainloop()