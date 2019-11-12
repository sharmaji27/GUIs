import tkinter as tk
from tkinter import messagebox
from tkinter import *
import wolframalpha
import wikipedia
import pyttsx3
import webbrowser

engine = pyttsx3.init()  #for text to speech
engine1 = pyttsx3.init()
engine2 = pyttsx3.init()
engine.say('welcome')

def get(event):
    while (1):
        query =var.get()
        try:                                 #try search using wolfram alpha
            client = wolframalpha.Client('your api here') #please write your wolframalpha api here
            res=client.query(query)
            ans=next(res.results).text
            messagebox.showinfo(title='Result',message=ans)
            engine2.say('searched for'+query)
            engine2.runAndWait()
            break

        except:                                             #otherwise try search using wikipedia
            try:
                #wikipedia.set_lang("hi") #for hindi lang    #uncomment this line for hindi language
                query1=query
                # query1=query1.split(' ')
                # query1=' '.join(query1[2:])
                ans=wikipedia.summary(query1,sentences=15)
                engine2.say('searched for '+query1)
                engine2.runAndWait()
                messagebox.showinfo(title='Result', message=ans)
                break
            except:
                engine2.say('searched for ' + query)
                engine2.runAndWait()
                webbrowser.open_new_tab(query)
                break


#creating a label and entry in  tkinter
        
win=tk.Tk()
win.title('PyDa')
win.configure(bg='black')
var=StringVar(value='')

Label(win,bg='black',fg='white',text='Hello I am PyDa the python digital assistant.\n How may I help you ?',font=('arial',20,'bold'),padx=100,pady=20).grid(row=0,column=1)
e1=Entry(win,width=30,font=('arial',25),bd=10,bg='white',fg='black',textvariable=var)
e1.grid(row=1,column=1)
e1.bind('<Return>',get) #search on enter
Label(win,text='note : please write full question',font=('arial',16,'italic'),bg='black',fg='red').grid(row=3,column=1)

engine.runAndWait()

win.mainloop()
