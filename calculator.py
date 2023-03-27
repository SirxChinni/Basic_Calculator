from tkinter import *
import math


def ONE(text):
    ent.insert(END, text)


def TWO(text):
    ent.insert(END, text)


def THREE(text):
    ent.insert(END, text)


def FOUR(text):
    ent.insert(END, text)


def FIVE(text):
    ent.insert(END, text)


def SIX(text):
    ent.insert(END, text)


def SEVEN(text):
    ent.insert(END, text)


def EIGHT(text):
    ent.insert(END, text)


def NINE(text):
    ent.insert(END, text)


def ZERO(text):
    ent.insert(END, text)


def delete():
    ent.delete(0, END)


def backspace():
    ent.delete(len(ent.get()) - 1, END)


def MUL(text):
    ent.insert(END, text)


def DIV(text):
    ent.insert(END, text)


def ADD(text):
    ent.insert(END, text)


def SUB(text):
    ent.insert(END, text)


def SQR():
    global var
    var = ent.get()
    var = float(var) ** 2
    ent.delete(0, END)
    ent.insert(END, var)


def ROOT():
    global var
    var = ent.get()
    var = math.sqrt(float(var))
    ent.delete(0, END)
    ent.insert(END, var)


def PI():
    ent.insert(END, '3.14')


def LB(text):
    ent.insert(END, text)


def RB(text):
    ent.insert(END, text)


def POINT(text):
    ent.insert(END, text)


def RES():
    global result
    result = ent.get()
    ent.delete(0, END)
    try:
        ent.insert(END, eval(result))
    except:
        ent.insert(END, 'ERROR')



root = Tk()
result = StringVar()
var = StringVar()
root.config(background='black')
root.geometry('750x750')
root.title("Basic Calculator")
f_null = Frame(root)
f0 = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)

label = Label(f_null, text='Calculator', bg="yellow", font=('Times new roman', 30, 'bold'), compound='bottom')
label.config(padx=20, pady=10, relief=SUNKEN)

ent = Entry(f0, width=20, font='Arial 24', fg="yellow", bg="Black", justify='right')

f_null.pack(pady=20)
f0.pack(pady=25)
f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()

seven = Button(f1, text='7', font=('arial', 25, 'bold'), command=lambda: SEVEN("7"), relief=SUNKEN, fg="yellow",
               bg="black", activeforeground="yellow", activebackground="black")
seven.pack(side='left', padx=8, pady=8)
eight = Button(f1, text='8', font=('arial', 25, 'bold'), command=lambda: EIGHT("8"), relief=SUNKEN, fg="yellow",
               bg="black", activeforeground="yellow", activebackground="black")
eight.pack(side='left', padx=8, pady=8)
nine = Button(f1, text='9', font=('arial', 25, 'bold'), command=lambda: NINE("9"), relief=SUNKEN, fg="yellow",
              bg="black", activeforeground="yellow", activebackground="black")
nine.pack(side='left', padx=8, pady=8)
mul = Button(f1, text='*', font=('arial', 25, 'bold'), command=lambda: MUL("*"), relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
mul.pack(side='left', padx=8, pady=8)

four = Button(f2, text='4', font=('arial', 25, 'bold'), command=lambda: FOUR("4"), relief=SUNKEN, fg="yellow",
              bg="black", activeforeground="yellow", activebackground="black")
four.pack(side='left', padx=8, pady=8)
five = Button(f2, text='5', font=('arial', 25, 'bold'), command=lambda: FIVE("5"), relief=SUNKEN, fg="yellow",
              bg="black", activeforeground="yellow", activebackground="black")
five.pack(side='left', padx=8, pady=8)
six = Button(f2, text='6', font=('arial', 25, 'bold'), command=lambda: SIX("6"), relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
six.pack(side='left', padx=8, pady=8)
div = Button(f2, text='/', font=('arial', 26, 'bold'), command=lambda: DIV("/"), relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
div.pack(side='left', padx=8, pady=8)

one = Button(f3, text='1', font=('arial', 25, 'bold'), command=lambda: ONE("1"), relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
one.pack(side='left', padx=8, pady=8)
two = Button(f3, text='2', font=('arial', 25, 'bold'), command=lambda: TWO("2"), relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
two.pack(side='left', padx=8, pady=8)
three = Button(f3, text='3', font=('arial', 25, 'bold'), command=lambda: THREE("3"), relief=SUNKEN, fg="yellow",
               bg="black", activeforeground="yellow", activebackground="black")
three.pack(side='left', padx=8, pady=8)
add = Button(f3, text='+', font=('arial', 21, 'bold'), command=lambda: ADD("+"), relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
add.pack(side='left', padx=8, pady=8)

delete_bt = Button(f4, font=('arial', 25, 'bold'), text="c", command=delete, relief=SUNKEN, fg="yellow",
                   bg="black", activeforeground="yellow", activebackground="black")
delete_bt.pack(side='left', padx=8, pady=8)
zero = Button(f4, text='0', font=('arial', 25, 'bold'), command=lambda: ZERO("0"), relief=SUNKEN, fg="yellow",
              bg="black", activeforeground="yellow", activebackground="black")
zero.pack(side='left', padx=8, pady=8)
backspace_bt = Button(f4, text="b", font=('arial', 25, 'bold'), command=backspace, relief=SUNKEN, fg="yellow",
                      bg="black", activeforeground="yellow", activebackground="black")
backspace_bt.pack(side='left', padx=8, pady=8)
sub = Button(f4, text='-', font=('arial', 25, 'bold'), command=lambda: SUB("-"), relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
sub.pack(side='left', padx=8, pady=8)

sqr = Button(f5, text='²', font=('arial', 25, 'bold'), command=lambda: SQR(), relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
sqr.pack(side='left', padx=8, pady=8)
root = Button(f5, text='√', font=('arial', 25, 'bold'), command=lambda: ROOT(), relief=SUNKEN, fg="yellow",
              bg="black", activeforeground="yellow", activebackground="black")
root.pack(side='left', padx=8, pady=8)
pi = Button(f5, text='π', font=('arial', 25, 'bold'), command=lambda: PI(), relief=SUNKEN, fg="yellow",
            bg="black", activeforeground="yellow", activebackground="black")
pi.pack(side='left', padx=8, pady=8)
res = Button(f5, text='=', font=('arial', 21, 'bold'), command=RES, relief=SUNKEN, fg="yellow",
             bg="black", activeforeground="yellow", activebackground="black")
res.pack(side='left', padx=8, pady=8)

lb = Button(f6, text='(', font=('arial', 25, 'bold'), command=lambda: LB("("), relief=SUNKEN, fg="yellow",
            bg="black", activeforeground="yellow", activebackground="black")
lb.pack(side='left', padx=8, pady=8)
point = Button(f6, text='.', font=('arial', 25, 'bold'), command=lambda: POINT("."), relief=SUNKEN, fg="yellow",
               bg="black", activeforeground="yellow", activebackground="black")
point.pack(side='left', padx=8, pady=8)
rb = Button(f6, text=')', font=('arial', 25, 'bold'), command=lambda: RB(")"), relief=SUNKEN, fg="yellow",
            bg="black", activeforeground="yellow", activebackground="black")
rb.pack(side='left', padx=8, pady=8)

ent.pack()
label.pack()
root.mainloop()
