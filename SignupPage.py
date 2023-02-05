from tkinter import *
import pyrelog as pl
from tkinter.messagebox import showinfo, showwarning


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("753x464")
window.configure(bg = "#ffffff")
window.title("Audio Resulotion")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 464,
    width = 753,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"SignupPageImages/background.png")
background = canvas.create_image(
    349.0, 232.0,
    image=background_img)

# Get started function
def signup_button():
    user = entry0.get()
    password = entry1.get()
    try:
        pl.signup(user, password)
        window.destroy()
        import LoginPage
    except:
        # switch with tkinter display of failed login (password under 6 character, existing email)
        showwarning(
            title='Warning',
            message="Invalid input! Please try again"
        )

# Get started button
img0 = PhotoImage(file = f"SignupPageImages/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = signup_button,
    relief = "flat")

b0.place(
    x = 443, y = 321,
    width = 106,
    height = 41)

def clear():
    entry0.delete(0, END)
    entry1.delete(0, END)
# Clear button
img1 = PhotoImage(file = f"SignupPageImages/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = clear,
    relief = "flat")

b1.place(
    x = 443, y = 383,
    width = 106,
    height = 41)
# Back function
def back_button():
    window.destroy()
    import LoginPage

# Back button
img2 = PhotoImage(file = f"SignupPageImages/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = back_button,
    relief = "flat")

b2.place(
    x = 572, y = 321,
    width = 106,
    height = 41)
# Exit function
def exit():

    window.destroy()

img3 = PhotoImage(file = f"SignupPageImages/img3.png")

# Exit button
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = exit,
    relief = "flat")

b3.place(
    x = 575, y = 383,
    width = 106,
    height = 41)

entry0_img = PhotoImage(file = f"SignupPageImages/img_textBox0.png")
entry0_bg = canvas.create_image(
    556.5, 229.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    highlightthickness = 0)

entry0.place(
    x = 462.5, y = 215,
    width = 188.0,
    height = 27)

# Password entry
entry1_img = PhotoImage(file = f"SignupPageImages/img_textBox1.png")
entry1_bg = canvas.create_image(
    556.5, 285.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    show = '*',
    highlightthickness = 0)

entry1.place(
    x = 462.5, y = 271,
    width = 188.0,
    height = 27)

window.resizable(False, False)
window.mainloop()
