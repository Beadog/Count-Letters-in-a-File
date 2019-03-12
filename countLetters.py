'''
Corrie Stewart
Program counts letters in a file and displays results in a histogram using tkinter
Date: 10/28/18
'''

from tkinter import *  # Import tkinter
import tkinter.messagebox  # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename


def showResult():
    analyzeFile(filename.get())


def analyzeFile(filename):
    try:
        infile = open(filename, "r")  # Open the file

        counts = 26 * [0]  # Create and initialize counts
        for line in infile:
            # Invoke the countLetters function to count each letter
            countLetters(line.lower(), counts)

        # Display the results in a histogram
        bottomGap = 20
        canvas.delete("line")
        canvas.create_line(10, height - bottomGap, width - 10, height - bottomGap, tag="line")
        barWidth = (width - 20) / len(counts)

        maxCount = int(max(counts))
        for i in range(len(counts)):
            canvas.create_rectangle(i * barWidth + 10, (height - bottomGap) * (1 - counts[i] / (maxCount + 4)),
                                    (i + 1) * barWidth + 10, height - bottomGap, tag="line")
            canvas.create_text(i * barWidth + 10 + barWidth / 2,
                               height - bottomGap / 2,
                               text=str(chr(ord('a') + i)), tag="line")
            canvas.create_text(i * barWidth + 10 + barWidth / 2,
                               (height - bottomGap) * (1 - counts[i] / (maxCount + 4)) - 8,
                               text=str(counts[i]), tag="line")

        infile.close()  # Close file
    except IOError:
        tkinter.messagebox.showwarning("Analyze File",
                                       "File " + filename + " does not exist")

# Count each letter in the string
def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

def openFile():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)


window = Tk()  # Create a window
window.title("Occurrence of Letters Histogram")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()

# canvas for the histogram display
width = 340
height = 150
radius = 2
canvas = Canvas(window, width=width, height=height)
canvas.pack()


frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=openFile).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
