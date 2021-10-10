from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title('DigiClock')
app_window.geometry('470x140')
app_window.resizable(1, 1)
app_window.configure(bg='black')

text_font = ("Boulder", 68, 'bold')
background = 'black'
foreground = 'red'
border_width = 10

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digi_clock():
    time_now = time.strftime("%H:%M:%S")
    label.config(text=time_now)
    label.after(200, digi_clock)


digi_clock()
app_window.mainloop()
