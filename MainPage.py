from tkinter import *
from pygame import mixer
from tkinter.filedialog import askopenfile,askopenfilename
from tkinter.messagebox import showinfo, showwarning
import os
import run as algro
import shutil

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

background_img = PhotoImage(file = f"MainPageImages/background.png")
background = canvas.create_image(
    364.5, 232.0,
    image=background_img)

# Select function
def select():
    file = askopenfilename(filetypes=[
        ('Audio files', '*.wav'), ('all files', '*.*')])
    
    shutil.copyfile(file,'./files/selected_audio.wav')
        
    showinfo(
        title='Selected Audio',
        #message= file.name + " is selected"
    )
    file.close()

# Select button
img0 = PhotoImage(file = f"MainPageImages/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = select,
    relief = "flat")

b0.place(
    x = 442, y = 232,
    width = 106,
    height = 41)

# Play function 
def play():
    #mixer.init()
    #sound = mixer.Sound("ConvertedAudio/samples_msp_4_msp.2.4.pr.wav")
    # sound.play
    pass
# Play button
img1 = PhotoImage(file = f"MainPageImages/music-player-icon.png")
img1 = img1.subsample(3)
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = play,
    relief = "flat")

b1.place(
    x = 515, y = 290,
    width = 110,
    height = 110)

# Convert function
def convert():
    s = ["eval","--logname", "./models/singlespeaker.lr0.000300.1.g4.b16/model.ckpt-10401", "--wav-file", "selected_audio.wav", "--r", "4", "--sr", "16000"]
    parser = algro.make_parser()
    args = parser.parse_args(s)
    args.func(args)
    #algro.eval(args)
# Convert button
img2 = PhotoImage(file = f"MainPageImages/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = convert,
    relief = "flat")

b2.place(
    x = 580, y = 232,
    width = 106,
    height = 41)

# Exit function
def exit():
    dir = os.listdir("files")
    
    if(len(dir) == 0):
        window.destroy()
    else:
        os.remove("files/selected_audio.wav")
        window.destroy()

# Exit button
img3 = PhotoImage(file = f"MainPageImages/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = exit,
    relief = "flat")

b3.place(
    x = 515, y = 425,
    width = 106,
    height = 41)

window.resizable(False, False)
window.mainloop()
