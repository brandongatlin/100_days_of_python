from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
  password_input.insert(0, 'raNd0M')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  site = website_input.get()
  username = email_input.get()
  password = password_input.get()
  
  if site == '' or username == '' or password == '':
    return messagebox.showerror(message='You forgot to enter all the data')
  
  confirm = messagebox.askyesno(message=f"You entered: \n {site} \n {username} \n {password} \n Save?")
  if confirm:
    with open('passwords.txt', 'a') as file:
      file.write(f"\n{site},{username},{password}")
      messagebox.showinfo(message='Saved!')
      pyperclip.copy(password)
      file.close()
  website_input.delete(0, 'end')
  email_input.delete(0, 'end')
  email_input.insert(0, 'brandongatlin1981@me.com')
  password_input.delete(0, 'end')
  
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(height=512, width=512)
logo = PhotoImage(file='logo.gif')
canvas.create_image(256, 256, image=logo)
canvas.grid(row=0, column=1)

website_lbl = Label(text='Website:')
website_lbl.grid(row=1, column=0)
email_lbl = Label(text='Email/Username:')
email_lbl.grid(row=2, column=0)
password_lbl = Label(text='Password:')
password_lbl.grid(row=3, column=0)

website_input = Entry(width=35, border=1.2)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)
email_input = Entry(width=35, border=1.2)
email_input.insert(0, 'brandongatlin1981@me.com')
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=20, border=1.2)
password_input.grid(row=3, column=1)

generate_btn = Button(text='Gen Password', command=gen_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text='Add', width=20, command=save_password)
add_btn.grid(row=4, column=1)






window.mainloop()