
from enum import unique
from os import read
from tkinter import *
from tkinter import filedialog
import string

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\",
                                          title="Open text File!",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    
    file = open(filepath,'r')
    Readf(file)


def Readf(file):
   AllWords = []
   # Taking sentences in the file and splitting them into words by the spaces.
   for line in file:
        Clean_line= line.translate(str.maketrans('', '', string.punctuation))
        words = Clean_line.split() # split by spaces in the sentence
        for word in words:
            word = word.strip('')
            word = word.lower()
            if word:
                AllWords.append(word)
                
   print(AllWords)
   uniqueList = list(set(AllWords))
   print(uniqueList)
   return AllWords   

window = Tk()
window.geometry("200x200")
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()
