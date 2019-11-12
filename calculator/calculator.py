from tkinter import *

calc = Tk()
calc.title('calculator')
operator = ''

def clear():
    global operator
    operator=''
    txt_input.set("")
    display.insert(0,'START CALCULATING...')

def button_press(number_or_operator):
    global operator
    operator = operator+str(number_or_operator)
    txt_input.set(operator)

def equal():
    global operator
    result = float(eval(operator))
    txt_input.set(result)
    operator=''


txt_input =StringVar(value='START CALCULATING...')

#-----------------DISPLAY-----------------------------------
display = Entry(calc,font =('arial',30),fg='white',bg='green'
                ,justify='right',bd='50',textvariable=txt_input)
display.grid(columnspan=4)

#------------------row 1--------------------------------------

button7 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='7',command=lambda:button_press(7)).grid(row=1,column=0)
button8 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='8',command=lambda:button_press(8)).grid(row=1,column=1)
button9 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='9',command=lambda:button_press(9)).grid(row=1,column=2)
button_clear = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='green',
                 font=('arial',30,'bold'),text='C',command=clear).grid(row=1,column=3)

#------------------row 2--------------------------------------

button4 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='4',command=lambda:button_press(4)).grid(row=2,column=0)
button5 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='5',command=lambda:button_press(5)).grid(row=2,column=1)
button6 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='6',command=lambda:button_press(6)).grid(row=2,column=2)
button_plus = Button(calc,padx =34,pady =12,bd=8,fg='black',bg='orange',
                 font=('arial',30,'bold'),text='+',command=lambda:button_press('+')).grid(row=2,column=3)

#------------------row 3--------------------------------------

button1 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='1',command=lambda:button_press(1)).grid(row=3,column=0)
button2 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='2',command=lambda:button_press(2)).grid(row=3,column=1)
button3 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='3',command=lambda:button_press(3)).grid(row=3,column=2)
button_minus = Button(calc,padx =38,pady =12,bd=8,fg='black',bg='orange',
                 font=('arial',30,'bold'),text='-',command=lambda:button_press('-')).grid(row=3,column=3)

#------------------row 4--------------------------------------

button_0 = Button(calc,padx =30,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='0',command=lambda:button_press(0)).grid(row=4,column=0)
button_dot = Button(calc,padx =36,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='.',command=lambda:button_press('.')).grid(row=4,column=1)
button_divide = Button(calc,padx =36,pady =12,bd=8,fg='black',bg='orange',
                 font=('arial',30,'bold'),text='/',command=lambda:button_press('/')).grid(row=4,column=2)
button_mult = Button(calc,padx =38,pady =12,bd=8,fg='black',bg='orange',
                 font=('arial',30,'bold'),text='*',command=lambda:button_press('*')).grid(row=4,column=3)

#------------------row 5--------------------------------------

button_equal = Button(calc,padx =95,pady =12,bd=8,fg='black',bg='green',
                 font=('arial',30,'bold'),text='=',command=equal).grid(row=5,column=0,columnspan=2)
button_open = Button(calc,padx =35,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text='(',command=lambda:button_press('(')).grid(row=5,column=2)
button_close = Button(calc,padx =38,pady =12,bd=8,fg='black',bg='white',
                 font=('arial',30,'bold'),text=')',command=lambda:button_press(')')).grid(row=5,column=3)

calc.mainloop()