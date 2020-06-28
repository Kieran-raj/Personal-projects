import tkinter as tk
from tkinter import messagebox
import math

calc = tk.Tk()
calc.title("Calc")



calc.rowconfigure([0,1,2,3,4,5], minsize=50, weight=1)
calc.columnconfigure([0,1,2,3,4], minsize=50, weight=1)
calc.configure()
index = 0

# button functions
isequalClicked = 0

def number0_click(num):
    global isequalClicked
    if isequalClicked > 0:
        entry.delete(0,"end")
        isequalClicked -= 1
    elif num in range(10):
        entry.insert("end",num)


def dec_click():
    entry.insert("end" ,".")


def operators_click(var):
    global isequalClicked
    isequalClicked -= 1
    entry.insert("end", var)


def sqr():
    string = entry.get()
    if "." in string:
        ans = float(string)**2
    else:
        ans = int(string)**2
    entry.delete(0, "end")
    entry.insert(0, ans)


def sqrt():
    string = entry.get()
    if "." in string:
        ans = math.sqrt(float(string))
    else:
        ans = int(math.sqrt(int(string)))
    entry.delete(0, "end")
    entry.insert(0, ans)


def trig(var):
    string = entry.get()
    if "." in string:
        if var == "sin()":
            ans = math.sin(float(string))
        elif var == "cos()":
            ans = math.cos(float(string))
        else:
            ans = math.tan(float(string))
    else:
        if var == "sin()":
            ans = math.sin(int(string))
        elif var == "cos()":
            ans = math.cos(int(string))
        else:
            ans = math.tan(int(string))
    entry.delete(0, "end")
    entry.insert(0, ans)


def clr_click():
    entry.delete(0,"end")


def del_click():
    length = len(entry.get())
    entry.delete(length - 1)


def equal_click():
    global isequalClicked
    isequalClicked += 1
    string = entry.get()
    if string != "":
        try:
            ans = eval(string)
            entry.delete(0,"end")
            entry.insert(0,ans)
        except ZeroDivisionError:
            entry.delete(0,"end")
            messagebox.showerror("Mathematical Error","Cannot divide by zero")
        except ValueError:
            entry.delete(0,"end")
            messagebox.showerror("Error", "Unknown Error!!")
        except SyntaxError:
            entry.delete(0,"end")
            messagebox.showerror("Error", "Invalid input")


def equal_key(event):
    string = entry.get()
    if string != "":
        try:
            if string.endswith(".0"):
                ans = float(eval(string))
            else:
                ans = int(eval(string))
            entry.delete(0, "end")
            entry.insert(0, ans)
        except ZeroDivisionError:
            entry.delete(0, "end")
            messagebox.showerror("Mathematical Error", "Cannot divide by zero")
        except ValueError:
            entry.delete(0, "end")
            messagebox.showerror("Error", "Unknown Error!!")
    else:
        messagebox.showerror("Input Error", "Not valid input")


# entry box for text and input
entry = tk.Entry(calc, font=12, relief="solid", borderwidth=0)
entry.bind("<Return>", equal_key)
entry.grid(row=0, column=0, columnspan=5, sticky="nesw")
entry.insert(0, "")


# frame for cos, tan and sin
frame_width = 45
frame = tk.Frame(calc)
frame.grid(row=4, column=4, rowspan=2, columnspan=1, sticky="")

# buttons
# numbers
button_0 = tk.Button(calc, width=5, height=int(2.5), text="0",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(0))
button_0.grid(row=5, column=1, columnspan=1, sticky="nesw")

button_1 = tk.Button(calc, width=5, height=int(2.5), text="1",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(1))
button_1.grid(row=4, column=0, sticky="nesw")

button_2 = tk.Button(calc, width=5, height=int(2.5), text="2",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(2))
button_2.grid(row=4, column=1, columnspan=1, sticky="nesw")

button_3 = tk.Button(calc, width=5, height=int(2.5), text="3",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(3))
button_3.grid(row=4, column=2, columnspan=1, sticky="nesw")

button_4 = tk.Button(calc, width=5, height=int(2.5), text="4",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(4))
button_4.grid(row=3, column=0, columnspan=1, sticky="nesw")

button_5 = tk.Button(calc, width=5, height=int(2.5), text="5",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(5))
button_5.grid(row=3, column=1, columnspan=1, sticky="nesw")

button_6 = tk.Button(calc, width=5, height=int(2.5), text="6",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(6))
button_6.grid(row=3, column=2, columnspan=1, sticky="nesw")

button_7 = tk.Button(calc, width=5, height=int(2.5), text="7",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(7))
button_7.grid(row=2, column=0, columnspan=1, sticky="nesw")

button_8 = tk.Button(calc, width=5, height=int(2.5), text="8",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(8))
button_8.grid(row=2, column=1, columnspan=1, sticky="nesw")

button_9 = tk.Button(calc, width=5, height=int(2.5), text="9",
                     relief="flat", activebackground="#BEBEBE", command=lambda: number0_click(9))
button_9.grid(row=2, column=2, columnspan=1, sticky="nesw")

# decimal
button_dec = tk.Button(calc, width=5, height=int(2.5), text=".", relief="flat",
                       activebackground="#BEBEBE", command=dec_click)
button_dec.grid(row=5, column=2, columnspan=1, sticky="nesw")

# operators
button_plu = tk.Button(calc, width=5, height=int(2.5), text="+",
                       relief = "flat", activebackground="#BEBEBE", command=lambda: operators_click("+"))
button_plu.grid(row=1, column=0, columnspan=1, sticky="nesw")

button_sub = tk.Button(calc, width=5, height=int(2.5), text="-",
                       relief="flat", activebackground="#BEBEBE", command=lambda: operators_click("-"))
button_sub.grid(row=1, column=1, columnspan=1, sticky="nesw")

button_mul = tk.Button(calc, width=5, height=int(2.5), text="*",
                       relief = "flat", activebackground="#BEBEBE", command=lambda: operators_click("*"))
button_mul.grid(row=1, column=2, columnspan=1, sticky="nesw")

button_div = tk.Button(calc, width=5, height=int(2.5), text="/",
                       relief = "flat", activebackground="#BEBEBE", command=lambda: operators_click("/"))
button_div.grid(row=1, column=3, columnspan=1, sticky="nesw")

# sqr and sqrt
button_sqr = tk.Button(calc, width=5, height=int(2.5), text="x^2", relief="flat",
                       activebackground="#BEBEBE", command=sqr)
button_sqr.grid(row=1, column=4, rowspan=1, columnspan=1, sticky="nesw")

button_sqrt = tk.Button(calc, width=5, height=int(2.5), text="sqrt", relief="flat",
                        activebackground="#BEBEBE", command=sqrt)
button_sqrt.grid(row=2, column=4, rowspan=1, columnspan=1, sticky="nesw")


# sin, cos and tan
button_s = tk.Button(frame, width=6, height=int(1.5), text="sin()",
                     relief="flat", activebackground="#BEBEBE", command=lambda: trig("sin()"))
button_s.grid(row=0, column =0, pady=0, sticky="nesw")

button_c = tk.Button(frame, width=6, height=int(1.5), text="cos()",
                     relief="flat", activebackground="#BEBEBE", command=lambda: trig("cos()"))
button_c.grid(row=1, column=0, pady=11, sticky="nesw")

button_t = tk.Button(frame, width=6, height=int(1.5), text="tan()",
                     relief="flat", activebackground="#BEBEBE", command=lambda: trig("tan()"))
button_t.grid(row=2, column=0, sticky="nesw")


# answer and clear
button_equ = tk.Button(calc, width=5, height=5, text="=", relief="flat",
                       activebackground="#BEBEBE", command=equal_click)
button_equ.grid(row=4, column=3, rowspan=2, columnspan=1, sticky="nesw")
# when working in rows, changes in height will cause elongation downwards
button_clr = tk.Button(calc, width=5, height=int(2.5), text="clear", relief="flat",
                       activebackground="#BEBEBE", command=clr_click)
button_clr.grid(row=3, column=3, rowspan=1, columnspan=1, sticky="nesw")
button_del = tk.Button(calc, width=5, height=int(2.5), text="del", relief="flat",
                       activebackground="#BEBEBE", command=del_click)
button_del.grid(row=2, column=3, rowspan=1, columnspan=1, sticky="nesw")



calc.resizable(0,0)
calc.mainloop()
