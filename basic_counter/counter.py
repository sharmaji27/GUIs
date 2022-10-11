from tkinter import *
counter =0

def digit_counter(my_label):
    def digit():
        global counter
        my_label.config(text=str(counter))
        my_label.after(100,digit)
        counter += 1
    digit()

win = Tk()
win.title('digit counter')

my_label = Label(font=10,fg='red')
my_label.pack()

terminate =Button(text='terminate',padx=100,command= win.destroy)
terminate.pack()

digit_counter(my_label)
win.mainloop()