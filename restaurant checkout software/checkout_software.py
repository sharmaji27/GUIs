#remove your pushbullet api before uploading
from tkinter import *
from tkinter import ttk
from pushbullet import PushBullet
# pb = PushBullet('your pushbullet api here')

customer_info =open('info.txt','a')

win =Tk()
win.title('checkout')
win.configure(bg='black')

def clear():
    var1.set('')
    var2.set('')
    var3.set('')
    var4.set('')
    var5.set('')
    e1.set(value='choose meal')
    e3.set(value='choose drink')
    e6.set(value='choose room')
    e5.deselect()
    e7.delete(0,END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)
    e16.delete(0,END)
    display.delete(0,END)


def cost_of_meal():
    if indicator1.get()=='FRIED RICE':
        p=100
    elif indicator1.get()=='SHAWRAMA':
        p=80
    elif indicator1.get()=='BUTTER CHICKEN':
        p=300
    elif indicator1.get()=='CHICKEN TIKKA':
        p=200
    elif indicator1.get()=='PIZZA':
        p=150
    elif indicator1.get() == 'BURGER':
        p=50
    cost = var1.get()*p
    e7.insert(0,cost)
    return cost

def cost_of_drink():
    if indicator2.get()=='COCA COLA':
        q=20
    elif indicator2.get()=='FANTA':
        q=20
    elif indicator2.get()=='LIMCA':
        q=15
    elif indicator2.get()=='SPRITE':
        q=15
    elif indicator2.get()=='MOUNTAIN DEW':
        q=25
    elif indicator2.get() == 'SHIKANJI':
        q=30
    cost2 = var2.get()*q
    e8.insert(0,cost2)
    return cost2

def service_charges():
    if indicator3.get()=='VIP':
        e11.insert(0,200)
        return 200
    elif indicator3.get()=='NORMAL':
        e11.insert(0,100)
        return 100
    elif indicator3.get() == 'NO':
        e11.insert(0, 0)
        return 0

def cost_of_rooms():
    if indicator3.get()=='VIP':
        e10.insert(0,2000*var3.get())
        return 2000*var3.get()
    elif indicator3.get()=='NORMAL':
        e10.insert(0, 1000 * var3.get())
        return 1000*var3.get()
    elif indicator3.get() == 'NO':
        e10.insert(0, 0)
        return 0

def delivery():
    if checkvar.get()==1:
        cv=100
    else:
        cv=0
    e9.insert(0,cv)
    return cv

def total():
    cm=cost_of_meal()
    cd=cost_of_drink()
    sc=service_charges()
    cr=cost_of_rooms()
    cv=delivery()
    total_cost = cm+cd+sc+cr+cv
    e16.insert(0,total_cost)
    indicator4.set('PLEASE PAY ₹'+str(total_cost)+'/-')
    customer_info.write(str(var4.get()))
    customer_info.write('\t')
    customer_info.write(str(var5.get()))
    customer_info.write('\t')
    customer_info.write(str(var6.get()))
    customer_info.write('\t\n')
    pb.push_sms(pb.devices[0], str(var4.get()), 'Thanks '+str(var5.get())+
                ' for staying.\nYour total bill is ₹ '+str(total_cost))
    
#--------------------------------------------
indicator1 = StringVar(value='Choose meal')
indicator2 = StringVar(value='Choose drink')
indicator3 = StringVar(value='Choose room')
indicator4 = StringVar(value='------WELCOME------    ')
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = StringVar(value='')
var5 = StringVar(value='')
var6 = StringVar(value='')
checkvar = IntVar()

#-------------------DISPLAY-------------------
display = Entry(win,font =('arial',80),fg='white',bg='#0099CC'
                ,justify='right',bd='45',textvariable=indicator4)
display.grid(columnspan=10)

#----------------------------------------------

Label(text='choose meal',font=('arial',15,'bold'),bg='black',fg='white').grid(row=1,sticky='W')
e1= ttk.Combobox(width=18,font=('arial',15),textvariable=indicator1)
e1['values']=('FRIED RICE','SHAWRAMA','BUTTER CHICKEN','CHICKEN TIKKA','PIZZA','BURGER')
e1.grid(row=1,column=1)
#----------------------------------------------

Label(text='quantity of meal',font=('arial',15,'bold'),bg='black',fg='white').grid(row=2,sticky='W')
e2 = Entry(width=19,font=('arial',15),bd=6,textvariable=var1)
e2.grid(row=2,column=1)
#----------------------------------------------

Label(text='choose drink',font=('arial',15,'bold'),bg='black',fg='white').grid(row=3,sticky='W')
e3= ttk.Combobox(width=18,font=('arial',15),textvariable=indicator2)
e3['values']=('COCA COLA','FANTA','LIMCA','SPRITE','MOUNTAIN DEW','SHIKANJI')
e3.grid(row=3,column=1)
#----------------------------------------------

Label(text='quantity of drink',font=('arial',15,'bold'),bg='black',fg='white').grid(row=4,sticky='W')
e4 = Entry(width=19,font=('arial',15),bd=6,textvariable=var2)
e4.grid(row=4,column=1)
#----------------------------------------------

Label(text='order delivery',font=('arial',15,'bold'),bg='black',fg='white').grid(row=5,sticky='W')
e5 = Checkbutton(text='YES',font=('arial',10,'bold'),variable=checkvar)
e5.grid(row=5,column=1)

#----------------------------------------------

Label(text='room booking',font=('arial',15,'bold'),bg='black',fg='white').grid(row=6,sticky='W')
e6= ttk.Combobox(width=18,font=('arial',15),textvariable=indicator3)
e6['values']=('VIP','NORMAL','NO')
e6.grid(row=6,column=1)

#----------------------------------------------------------
Label(text='Cost of meal(₹)',font=('arial',15,'bold'),bg='black',fg='white').grid(row=1,column=2)
e7 = Entry(width=19,font=('arial',15),bd=6,bg='white',fg='black')
e7.grid(row=1,column=3)


Label(text='Cost of drink(₹)',font=('arial',15,'bold'),bg='black',fg='white').grid(row=2,column=2)
e8 = Entry(width=19,font=('arial',15),bd=6,bg='white',fg='black')
e8.grid(row=2,column=3)

Label(text='Delivery cost(₹)',font=('arial',15,'bold'),bg='black',fg='white').grid(row=3,column=2)
e9 = Entry(width=19,font=('arial',15),bd=6,bg='white',fg='black')
e9.grid(row=3,column=3)

Label(text='Cost of room(₹) ',font=('arial',15,'bold'),bg='black',fg='white').grid(row=4,column=2)
e10 = Entry(width=19,font=('arial',15),bd=6,bg='white',fg='black')
e10.grid(row=4,column=3)

Label(text='Service fee(₹)',font=('arial',15,'bold'),bg='black',fg='white').grid(row=5,column=2)
e11 = Entry(width=19,font=('arial',15),bd=6,bg='white',fg='black')
e11.grid(row=5,column=3)

Label(text='   ',font=('arial',15,'bold'),bg='black',fg='white').grid(row=6,column=4)
Label(text='Your E-mail ID',font=('arial',15,'bold'),bg='black',fg='white').grid(row=7,column=2)
e12 = Entry(width=19,font=('arial',15),bd=6,bg='white',fg='black',textvariable=var6)
e12.grid(row=7,column=3)
#-----------------------------------------------------

Label(text='no. of days',font=('arial',15,'bold'),bg='black',fg='white').grid(row=7,sticky='W')
e13 = Entry(width=19,font=('arial',15),bd=6,textvariable=var3)
e13.grid(row=7,column=1)

#-------------------------------------------------------
Label(text='   ',font=('arial',15,'bold'),bg='black',fg='white').grid(row=9,column=1)
Label(text='Your name',font=('arial',15,'bold'),bg='black',fg='white').grid(row=8,sticky='W')
e14 = Entry(width=19,font=('arial',15),bd=6,textvariable=var5)
e14.grid(row=8,column=1)
#--------------------------------------------------------
Label(text='Your contact no.',font=('arial',15,'bold'),bg='black',fg='white').grid(row=9,sticky='W')
e15 = Entry(width=19,font=('arial',15),bd=6,textvariable=var4)
e15.grid(row=9,column=1)

#--------------------------------------------------------
Label(text='Total cost(₹)',font=('arial',25,'bold'),bg='black',fg='white').grid(row=9,column=2)
e16 = Entry(width=19,font=('arial',20),bd=10)
e16.grid(row=9,column=3)
#--------------------------------------------------------
Button(text='TOTAL',padx=20,font=('arial',17,'bold'),bg='orange',fg='white',bd=15,command=total)\
    .grid(row=3,column=5)
Button(text='CLEAR',padx=20,font=('arial',17,'bold'),bg='blue',
       fg='white',bd=15,command=clear).grid(row=5,column=5)
Button(text='EXIT',padx=36,font=('arial',17,'bold'),bg='red',
       fg='white',bd=15,command=win.destroy).grid(row=7,column=5)

win.mainloop()

#remove your pushbullet api before uploading