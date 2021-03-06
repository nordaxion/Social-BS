import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
from profanityfilter import ProfanityFilter
import TwitterBS
from time import sleep
import os

# Creates the GUI
root = tk.Tk()

# Title and Icon
root.title("SocialBS")
root.iconbitmap("images/icont_.ico")

# Creates the logo at the top of the GUI
logo = ImageTk.PhotoImage(Image.open("images/logo_script_75.png"))
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
blank_search = tk.Frame(blank_search, bg="white")
# Jed's Old Code blank_search.place(relwidth=0.4, relheight=1, relx=0.3)
blank_search.place(relx=0.5, rely=0.5, anchor=CENTER)

# Creates an input field in the frame
empty_search1 = tk.Label(blank_search)
usernameLabel = tk.Label(blank_search, text="Enter username")
usernameField = Entry(blank_search, width=30)
empty_search1.grid(row=0)
usernameLabel.grid(row=1, column=0)
usernameField.grid(row=1, column=1)
# usernameField.pack()

# Button
openFile = tk.Button(blank_search, text="Search", padx=10, pady=5, fg="#4CA3DD", bg="red",
                     command=lambda: start(usernameField.get()))
openFile.grid(row=2, column=0, columnspan=2)

"""
    Data Section
"""

blank_data = tk.Frame(canvas, bg="white")
blank_data.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.25)
# blank_data.place(width=tk.Frame.winfo_screenwidth, height=tk.Frame.winfo_screenheight, anchor=CENTER)

# blank_data = tk.Frame(blank_data, bg="white")
# blank_data.place(relwidth=0.5, relx=0.3)

"""
    Progress Bar
"""


# progress_bar = Progressbar(progress_data, orient="horizontal", length=400)
# progress_bar.grid(column=0, row=0, pady=10)

def start(entered_username=""):
    openFile.config(state=DISABLED)

    loading_label = tk.Label(blank_data, text="Please wait... system processing. Give me a moment.")
    loading_label.pack()

    sleep(3)

    username = entered_username.strip(" ")
    url = "http://www.twitter.com/" + username


    for widget in blank_data.winfo_children():
        widget.destroy()

    if username == "":
        empty_search5 = tk.Label(blank_data)
        empty_search5.pack()
        message = tk.Label(blank_data, text="Please enter a username")
        message.pack()
        openFile.config(state=NORMAL)

    else:
        print("\nDownloading tweets for " + username)
        response = None
        try:
            response = requests.get(url)
        except Exception as e:
            print(repr(e))
            return

        if response.status_code != 200:
            alert_message = tk.Label(blank_data, text="Please enter a valid username")
            alert_message.pack()
            usernameField.delete(0, "end")
            print("Non success status code returned " + str(response.status_code))
            openFile.config(state=NORMAL)

        else:
            soup = BeautifulSoup(response.text, 'lxml')

            if soup.find("div", {"class": "errorpage-topbar"}):
                print("\n\n Error: Invalid username.")
                sys.exit(1)
            masterTList = []
            tweets = TwitterBS.get_tweets_data(username, soup)
            TwitterBS.test_data(username, tweets, masterTList)
            print(masterTList)
            profPercent = len(masterTList) / len(tweets) * 100

            if profPercent >= 100:
                profPercent = 99.99

            for widget in blank_data.winfo_children():
                widget.destroy()

            percent = tk.Label(blank_data, text=f"This user has a {profPercent:4.2f}% of being potentially offensive")
            percent.pack()

            empty_search5 = tk.Label(blank_data)
            empty_search5.pack()

            tweet = Text(blank_data, wrap=WORD)

            for profTweets in masterTList:
                tweet.insert(END, profTweets + "\n\n")
                # tk.Text(blank_data, text=profTweets)

            tweet.config(state=DISABLED, font="Arial", width=90)
            tweet.pack()

            openFile.config(state=NORMAL)

            print(masterTList)


# Runs the GUI
root.mainloop()
