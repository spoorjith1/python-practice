import tkinter as tk

window = tk.Tk()
window.geometry("300x150")
window.title("Calculator")

l1 = tk.Label(window, text="Number", font=("Arial", 18))
l2 = tk.Label(window, text="Number", font=("Arial", 18))
l3 = tk.Label(window, text="Result", font=("Arial", 18))

e1 = tk.Entry(window, font=("Arial", 18))
e2 = tk.Entry(window, font=("Arial", 18))
e3 = tk.Entry(window, font=("Arial", 18))

def add():
    n1 = eval(e1.get())
    n2 = eval(e2.get())
    n3 = n1+n2
    e3.delete(0, tk.END)
    e3.insert(0,str(n3))
def sub():
    n1 = eval(e1.get())
    n2 = eval(e2.get())
    n3 = n1-n2
    e3.delete(0, tk.END)
    e3.insert(0,str(n3))

b1 = tk.Button(window, text="Add", font=("Arial", 18), command=add)
b2 = tk.Button(window, text="Sub", font=("Arial", 18), command=sub)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)

window.mainloop()
