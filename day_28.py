from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_interval = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global timer_interval, reps
  reps = 0
  window.after_cancel(timer_interval)
  timer_lbl.config(text='TIMER')
  canvas.itemconfigure(timer, text='0:00')
  checkmark_area.config()
  
  
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1
  
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60
  
  if reps % 2 == 1:
    countdown(work_sec) # 1/3/5/7
    timer_lbl.config(text='TIMER')
  elif reps == 8:
    countdown(long_break_sec) # 8
    timer_lbl.config(text='LONG Break')
  else:
    countdown(short_break_sec) # 2/4/6
    timer_lbl.config(text='short BREAK')
  
  
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
  if count >= 0:
    minutes = str(count // 60)
    seconds = str(count % 60)
    if len(seconds) == 1:
      seconds = f"0{seconds}"
    formatted = f"{minutes}:{seconds}"
    canvas.itemconfigure(timer, text=formatted)
    global timer_interval
    timer_interval = window.after(1000, countdown, count - 1)
  else:
    start_timer()
    current_checkmarks = '✅' * (reps // 2)
    checkmark_area.config(text=current_checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomo Timer')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(height=400, width=400, bg=YELLOW, highlightthickness=0)
timer_lbl = Label(text='TIMER', font=(FONT_NAME, 40, 'bold'))
timer_lbl.grid(row=0, column=1)
photo = PhotoImage(file='tomato.gif')
canvas.create_image(200, 200, image=photo)
timer = canvas.create_text(200, 300, text='00:00', font=(FONT_NAME, 24, 'bold'))
canvas.grid(row=1, column=1)

start_btn = Button(text='Start', highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)
reset_btn = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)
checkmark_area = Label()
checkmark_area.grid(row=3, column=1)



window.mainloop()