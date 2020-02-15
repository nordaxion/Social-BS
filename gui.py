import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

# Creates the GUI
root = tk.Tk()

# Title and Icon
root.title("SocialBS")
root.iconbitmap("images/icon.ico")

# Creates the logo at the top of the GUI
logo = ImageTk.PhotoImage(Image.open("images/logo_script_75.jpeg"))
logo_label = tk.Label(root, image=logo)
logo_label.pack()

# Sets the canvas up
canvas = tk.Canvas(root, height=720, width=1280, bg="#4CA3DD")
canvas.pack()  # Attaches canvas to the root

"""
    This whole section is for the search interface
"""
# Canvas for searches
blank_search = tk.Frame(canvas, bg="white")
blank_search.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.05)

# Creates a search frame
search_frame = tk.Frame(blank_search, bg="white")
search_frame.place(relwidth=0.4, relheight=1, relx=0.3)

# Creates an input field in the frame
empty_search1 = tk.Label(search_frame)
empty_search2 = tk.Label(search_frame)
usernameLabel = tk.Label(search_frame, text="Enter username")
usernameField = Entry(search_frame, width=30)
usernameLabel.grid(row=2, column=0)
usernameField.grid(row=2, column=1)
# usernameField.pack()

openFile = tk.Button(search_frame, text="Search", padx=10,
                     pady=5, fg="#4CA3DD", bg="red")
openFile.grid(row=2, column=0, columnspan=2)


"""
    Data Section
"""

# blank_data = tk.Frame(canvas, bg="white")

# blank_data.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.15)






# Runs the GUI
root.mainloop()
