import tkinter as tk
from tkinter import *
from tkinter import filedialog
from googletrans import Translator
import pyttsx3
import os
from tkinter.ttk import Combobox


root = tk.Tk()
root.title("Audio-File")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#272727")

translator = Translator()
engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    translate_to = translate_combobox.get()
    
    # Translate text to the selected language
    translation = translator.translate(text, dest=translate_to)
    translated_text = translation.text
    
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

        engine.say(translated_text)
        engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == "Normal":
            engine.setProperty('rate', 120)
        else:
            engine.setProperty('rate', 60)
        
        setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    translate_to = translate_combobox.get()

    # Translate text to the selected language
    translation = translator.translate(text, dest=translate_to)
    translated_text = translation.text

    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

        path = filedialog.askdirectory()
        os.chdir(path)
        engine.save_to_file(translated_text, 'text.mp3')
        engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == "Normal":
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        
        setvoice()

# Top Frame
Top_frame = Frame(root, bg="#90EE90", width=900, height=100)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="say.png")
Logo = Logo.subsample(9, 9)
Label(Top_frame, image=Logo, bg="#90EE90").place(x=295, y=10)

Label(Top_frame, text="TEXT TO SPEECH", font="algerian 20 bold", bg="#90EE90", fg="black").place(x=380, y=30)

python_logo = PhotoImage(file="PythonLogo.png")
python_logo = python_logo.subsample(6, 6)
Label(Top_frame, image=python_logo, bg="#90EE90").place(x=760, y=40)

# Text Area
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

# Labels and Comboboxes
Label(root, text="VOICE", font="algerian 15 bold", bg="#272727", fg="white").place(x=580, y=140)
Label(root, text="SPEED", font="algerian 15 bold", bg="#272727", fg="white").place(x=760, y=140)
Label(root, text="Translate To", font="algerian 15 bold", bg="#272727", fg="white").place(x=630, y=235)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=170)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=170)
speed_combobox.set('Normal')

translate_combobox = Combobox(root, values=['en', 'hi', 'mr'], font="arial 14", state='r', width=10)
translate_combobox.place(x=640, y=265)
translate_combobox.set('en')

# Buttons
imageicon = PhotoImage(file="speak.png")
imageicon = imageicon.subsample(15, 15)
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=350)

imageicon2 = PhotoImage(file="download.png")
imageicon2 = imageicon2.subsample(10, 10)
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=130, bg="#39c790", font="arial 14 bold", command=download)
save.place(x=730, y=350)

root.mainloop()

