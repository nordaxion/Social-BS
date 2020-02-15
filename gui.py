import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

# Creates the GUI
root = tk.Tk()

root.title("SocialBS")
root.iconbitmap("images/icon.ico")

canvas = tk.Canvas(root, height=720, width=1280, bg="#4CA3DD")
canvas.pack()  # Attaches canvas to the root

logo = ImageTk.PhotoImage(Image.open("images/logo.jpeg"))
logo_label = tk.Label(image=logo)
logo_label.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

# Creates an input field
usernameField = Entry(frame, width=30)
usernameField.pack()

openFile = tk.Button(frame, text="Open File", padx=10,
                     pady=5, fg="white", bg="red")
openFile.pack()

runApps = tk.Button(frame, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="black")

# Runs the GUI
root.mainloop()
