from tkinter import *
from pygame import mixer


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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    364.5, 232.0,
    image=background_img)

# Select button
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 442, y = 232,
    width = 106,
    height = 41)

# Play function 
mixer.init()
sound = mixer.Sound("ConvertedAudio/samples_msp_4_msp.2.4.pr.wav")

# Play button
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = sound.play,
    relief = "flat")

b1.place(
    x = 442, y = 314,
    width = 106,
    height = 41)


# Convert button
img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 580, y = 232,
    width = 106,
    height = 41)

# Exit function
def exit():

    window.destroy()

# Exit button
img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = exit,
    relief = "flat")

b3.place(
    x = 580, y = 314,
    width = 106,
    height = 41)

window.resizable(False, False)
window.mainloop()
