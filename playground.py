from tkinter import Tk, Label

window = Tk()
window.title("Password Manager")

r = Label(bg="red", width=20, height=5)
r.grid(column=1, row=1)

g = Label(bg="green", width=20, height=5)
g.grid(column=2, row=1)
b = Label(bg="black", width=20, height=5)
b.grid(column=3, row=1)
gr = Label(bg="gray", width=20, height=5)
gr.grid(column=2, row=2)
p = Label(bg="pink", width=20, height=5)
p.grid(column=3, row=2)
y = Label(bg="yellow", width=20, height=5)
y.grid(column=1, row=2)
blue = Label(bg="blue", width=60, height=5)
blue.grid(column=1, row=3, columnspan=3)


window.mainloop()