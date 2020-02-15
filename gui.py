import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
from profanityfilter import ProfanityFilter
import TwitterBS

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
search_frame = tk.Frame(blank_search, bg="white")
search_frame.place(relwidth=0.4, relheight=1, relx=0.3)

# Creates an input field in the frame
empty_search1 = tk.Label(search_frame)
empty_search2 = tk.Label(search_frame)
usernameLabel = tk.Label(search_frame, text="Enter username")
usernameField = Entry(search_frame, width=30)
empty_search1.grid(row=0)
empty_search2.grid(row=1)
usernameLabel.grid(row=2, column=0)
usernameField.grid(row=2, column=1)
# usernameField.pack()

''' pady=5, fg="#4CA3DD", bg="red", COMMAND= openFileCallback)
openFile.grid(row=3, column=0, columnspan=2)

def openFileCallback():
    openFile.destroy
    empty_search1.destroy
    empty_search2.destroy
    usernameField.destroy
    usernameField.destroy
    usernameLabel = tk.Label(search_frame, text=profPercent + "%")
    usernameLabel.grid(row=2, column=0)

'''

openFile = tk.Button(search_frame, text="Search", padx=10, pady=5, fg="#4CA3DD", bg="red", command=lambda: start(usernameField.get()))
openFile.grid(row=3, column=0, columnspan=2)


"""
    Data Section
"""

blank_data = tk.Frame(canvas, bg="white")
blank_data.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.25)

progress_data = tk.Frame(blank_data, bg="white")
progress_data.place(relwidth=0.5, relx=0.3)

"""
    Progress Bar
"""


# progress_bar = Progressbar(progress_data, orient="horizontal", length=400)
# progress_bar.grid(column=0, row=0, pady=10)

def start(entered_username=None):
    username = entered_username
    url = "http://www.twitter.com/" + username

    download_tweets = tk.Label(progress_data, bg="white", text=f"Downloading tweets for {username}")
    download_tweets.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.25)

    print("\nDownloading tweets for " + username)
    response = None
    try:
        response = requests.get(url)
    except Exception as e:
        print(repr(e))
        sys.exit(1)

    if response.status_code != 200:
        print("Non success status code returned " + str(response.status_code))
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'lxml')

    if soup.find("div", {"class": "errorpage-topbar"}):
        print("\n\n Error: Invalid username.")
        sys.exit(1)
    masterTList = []
    tweets = TwitterBS.get_tweets_data(username, soup)
    TwitterBS.test_data(username, tweets, masterTList)
    print(masterTList)


# Runs the GUI
root.mainloop()
