from tkinter import *
import os
import math

def clk(num):
    global op
    op+=str(num)
    text_input.set(op)
def clear():
    global op
    op=''
    text_input.set('')
    
def eq():
    global op
    result=str(eval(op))
    text_input.set(result)
    op=''
    
window=Tk()
op=''
text_input=StringVar()
window.title('Calculator')
window.geometry('400x360')
window.configure(background='black')

label1=Label(window,text='CASIO',height=2,width=15)
label1.place(x=150,y=50)

b0=Button(window,text='0',width=8,height=1,command=lambda:clk(1),bg='powder blue')
b0.place(x=240,y=157)

b1=Button(window,text='1',width=8,height=1,command=lambda:clk(1),bg='powder blue')
b1.place(x=100,y=200)

b2=Button(window,text='2',width=8,height=1,command=lambda:clk(2),bg='powder blue')
b2.place(x=170,y=200)

b3=Button(window,text='3',width=8,height=1,bg='powder blue',command=lambda:clk(3))
b3.place(x=240,y=200)

b4=Button(window,text='4',width=8,height=1,bg='powder blue',command=lambda:clk(4))
b4.place(x=100,y=250)

b5=Button(window,text='5',width=8,height=1,bg='powder blue',command=lambda:clk(5))
b5.place(x=170,y=250)

b6=Button(window,text='6',width=8,height=1,bg='powder blue',command=lambda:clk(6))
b6.place(x=240,y=250)

b7=Button(window,text='7',width=8,height=1,bg='powder blue',command=lambda:clk(7))
b7.place(x=100,y=300)

b8=Button(window,text='8',width=8,height=1,bg='powder blue',command=lambda:clk(8))
b8.place(x=170,y=300)

b9=Button(window,text='9',width=8,height=1,bg='powder blue',command=lambda:clk(9))
b9.place(x=240,y=300)

add=Button(window,text='+',width=5,height=1,bg='green',command=lambda:clk('+'),font=('bold'))
add.place(x=320,y=150)

sub=Button(window,text='-',width=5,height=1,bg='green',command=lambda:clk('-'),font=('bold'))
sub.place(x=320,y=200)

mul=Button(window,text='*',width=5,height=1,bg='green',command=lambda:clk('*'),font=('bold'))
mul.place(x=320,y=250)

div=Button(window,text='/',width=5,height=1,bg='green',command=lambda:clk('/'),font=('bold'))
div.place(x=320,y=300)

cl=Button(window,text='C',width=5,height=1,bg='green',command=clear,font=('bold'))
cl.place(x=100,y=150)

equal=Button(window,text='ans',width=5,height=1,bg='green',command=eq,font=('bold'))
equal.place(x=170,y=150)

display=Entry(window,bg='blue',width=35,textvariable=text_input,justify='right')
display.place(x=100,y=100)



window.resizable(0,0)
window.mainloop()
