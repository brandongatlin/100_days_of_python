from tkinter import *

window = Tk()
window.title('Miles to kM Converter')
window.minsize(height=300, width=200)
window.config(padx=20, pady=20)

def convert():
  miles = float(input.get())
  v.set(miles * 1.6)

input = Entry(border=1.2)
input.grid(row=0, column=2, padx=20, pady=20)

label1 = Label(text='Miles')
label1.grid(row=0, column=3, padx=20, pady=20)

label2 = Label(text="Is Equal To").grid(row=1, column=0, padx=20, pady=20)

v = StringVar()
output_label = Label(text=0, textvariable=v).grid(row=1, column=1, padx=20, pady=20)

label3 = Label(text='kM').grid(row=1, column=2, padx=20, pady=20)

btn = Button(text='Convert!', command=convert).grid(row=2, column=1, padx=20, pady=20)

window.mainloop()