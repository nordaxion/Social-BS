import tkinter as tk
from tkinter import *
import os

# Creates the GUI
root = tk.Tk()

root.title("SocialBS")

canvas = tk.Canvas(root, height=720, width=1280, bg="#ff7ac3")
canvas.pack()  # Attaches canvas to the root

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Creates an input field
usernameField = Entry(root, width=30)
usernameField.pack()

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="red")
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="black")

# Runs the GUI
root.mainloop()
