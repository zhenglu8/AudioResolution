from tkinter import *


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

background_img = PhotoImage(file = f"LoginPageImages/background.png")
background = canvas.create_image(
    340.5, 232.0,
    image=background_img)

# Login function
def login():
    window.destroy()
    import MainPage

# Login button
img0 = PhotoImage(file = f"LoginPageImages/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b0.place(
    x = 443, y = 321,
    width = 106,
    height = 41)

def clear():
    entry0.delete(0, END)
    entry1.delete(0, END)

# Clear button
img1 = PhotoImage(file = f"LoginPageImages/img1.png")
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
# Signup function
def signup():
    window.destroy()
    import SignupPage

# Signup button
img2 = PhotoImage(file = f"LoginPageImages/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = signup,
    relief = "flat")

b2.place(
    x = 572, y = 321,
    width = 106,
    height = 41)

# Exit function
def exit():

    window.destroy()

img3 = PhotoImage(file = f"LoginPageImages/img3.png")

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

entry0_img = PhotoImage(file = f"LoginPageImages/img_textBox0.png")
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

entry1_img = PhotoImage(file = f"LoginPageImages/img_textBox1.png")
entry1_bg = canvas.create_image(
    556.5, 285.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    highlightthickness = 0)

entry1.place(
    x = 462.5, y = 271,
    width = 188.0,
    height = 27)

window.resizable(False, False)
window.mainloop()
