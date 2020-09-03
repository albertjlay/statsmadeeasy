from tkinter import *
from scipy.stats import norm
import tkinter.font as tkfont


root = Tk()
root.title ("Stats Made Easy")
root.geometry ("800x400")

#Text Levels
header1 = tkfont.Font(size = 36, family = "Impact")
header2 = tkfont.Font(size = 24, family = "Impact")
inline = tkfont.Font(size = 14, family = "Helvetica")

def normal ():
    print (norm.pdf (float(x_entry.get()), loc = float(mean_entry.get()), scale = float(sd_entry.get())))


#Frame for main navigation. Left side
navframe = LabelFrame (root)
navframe.grid (row = 0, column = 0)

#Inside of navframe
mainheader = Label (navframe, text = "STATS MADE EASY", width = 20, font = header1, fg = "#f2c022")
instruction = Label (navframe, text = "Hi, fellow students!\nUse this programs as a tool to help you study for your A-Level Mathematics: Statistics Module.", width = 40, height = 5, font = inline, fg = "black", wraplength = 310)
binombutton = Button (navframe, text = "BINOMIAL", width = 31, font = header2, fg = "white", bg = "#14a795")
poissonbutton = Button (navframe, text = "POISSON", width = 31, font = header2, fg = "white", bg = "#14a795")
normalbutton = Button (navframe, text = "NORMAL", width = 31, font = header2, fg = "white", bg = "#14a795")

mainheader.grid(row = 0, column = 0)
instruction.grid (row = 1, column = 0)
binombutton.grid (row = 2, column = 0)
poissonbutton.grid (row = 3, column = 0)
normalbutton.grid (row = 4, column = 0)

#Frame for calculation. Right side.
calcframe = LabelFrame (root)
calcframe.grid (row = 0, column = 1)

#Inside of calcframe
header_normal = Label (calcframe, text = "Normal Distribution", width = 20, font = header1, fg = "#14a795")
mean_label = Label (calcframe, text = "Mean:", font = inline)
mean_entry = Entry (calcframe)
sd_label = Label (calcframe, text = "Variance:", font = inline)
sd_entry = Entry (calcframe)
x_label = Label (calcframe, text = "X:", font = inline)
x_entry = Entry (calcframe)
normal_submit = Button (calcframe, text = "SUBMIT", font = inline, command = normal)

header_normal.grid (row = 0, column = 0, columnspan = 2)
mean_label.grid (row = 1, column = 0)
mean_entry.grid (row = 1, column = 1)
sd_label.grid (row = 2, column = 0)
sd_entry.grid (row = 2, column = 1)
x_label.grid (row = 3, column = 0)
x_entry.grid (row = 3, column = 1)
normal_submit.grid (row = 4, column = 0, columnspan = 2)



root.mainloop()
