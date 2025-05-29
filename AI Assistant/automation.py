import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

#define the main window
root = tk.Tk()
root.title("YOUR AI ASSISTANT")

#adding a background color
root.configure(bg='darkblue')

#define the function to automate youtube search
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

#define the function to automate google search
def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

#define the function to automate instagram search
def search_instagram():
    Username = entry.get().replace('@', "") #ensure username is clean of '@'
    url = f"www.instagram.com/{Username}/"
    webbrowser.open(url)

def search_x():
    Username = entry.get().replace('@', "") #ensure username is clean of '@'
    url = f"https://x.com/{Username}/"
    webbrowser.open(url)

#creat input field, labels, and buttons
Label(root, text = 'Enter your command:').pack(pady=10)
entry = Entry(root, width = 50)
entry.pack(pady=10)
Button(root, text = "Search on Youtube", command = search_youtube).pack(pady = 5)
Button(root, text = "Search on Google", command = search_google).pack(pady = 5)
Button(root, text = "Search on Instagram", command = search_instagram).pack(pady = 5)
Button(root, text = "Search on X", command = search_x).pack(pady = 5)

#RUN the GUI event loop
root.mainloop()