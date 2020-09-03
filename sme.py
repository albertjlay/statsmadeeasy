from tkinter import *
from scipy.stats import norm
import tkinter.font as tkfont


root = Tk()
root.title ("Stats Made Easy")
root.geometry ("1200x400")

#Text Levels
header1 = tkfont.Font(size = 36, family = "Impact")
header2 = tkfont.Font(size = 24, family = "Impact")
inline = tkfont.Font(size = 14, family = "Helvetica")
equation = tkfont.Font(size = 14, family = "Baskerville")


#Function to calculate normal probability
def normal ():
    #If variance was inputted, change to SD first before calculaton. If SD, store SD as float.
    if sd_var.get() == "Variance":
        sigma = math.sqrt(float(sd_entry.get()))
    else:
        sigma = float(sd_entry.get())

    #Determines whether probability being searched is less than or more than X
    if operation_var.get() == "<":
        probability = (norm.cdf (float(x_entry.get()), loc = float(mean_entry.get()), scale = sigma))
    elif operation_var.get() == ">":
        probability = 1 - (norm.cdf (float(x_entry.get()), loc = float(mean_entry.get()), scale = sigma))

    #Prints label into GUI
    result_label.config(text = "The probability that X is lower than " + x_entry.get() + " is " + str(round(probability,3)))



#Frame for main navigation. Left side
navframe = LabelFrame (root)
navframe.grid (row = 0, column = 0)

#Inside of navframe
mainheader = Label (navframe, text = "STATS MADE EASY", width = 20, font = header1, fg = "#f2c022")
instruction = Label (navframe, text = "Hi, fellow students!\nUse this programs as a tool to help you study for your A-Level Mathematics: Statistics Module.", width = 40, height = 5, font = inline, fg = "black", wraplength = 310)
binombutton = Button (navframe, text = "BINOMIAL", width = 31, font = header2, height = 2)
poissonbutton = Button (navframe, text = "POISSON", width = 31, font = header2, height = 2)
normalbutton = Button (navframe, text = "NORMAL", width = 31, font = header2, height = 2)

mainheader.grid(row = 0, column = 0)
instruction.grid (row = 1, column = 0)
binombutton.grid (row = 2, column = 0, pady = 5)
poissonbutton.grid (row = 3, column = 0, pady = 5)
normalbutton.grid (row = 4, column = 0, pady = 5)

#Frame for calculation. Right side.
calcframe = LabelFrame (root)
calcframe.grid (row = 0, column = 1, padx = 80)

#Inside of calcframe
sd_var = StringVar()
sd_var.set("Standard Deviation")

operation_var = StringVar()
operation_var.set("<")

header_normal = Label (calcframe, text = "Normal Distribution", width = 20, font = header1, fg = "#14a795")
mean_label = Label (calcframe, text = "Mean", font = equation)
mean_entry = Entry (calcframe, width = 10)
sd_dropdown = OptionMenu (calcframe, sd_var, "Standard Deviation", "Variance")
sd_dropdown.config (font = equation, width = 15, anchor = W, padx = 10)
sd_entry = Entry (calcframe, width = 10)
x_label = Label (calcframe, text = "X", font = equation)
x_entry = Entry (calcframe, width = 10)
normal_submit = Button (calcframe, text = "SUBMIT", font = inline, command = normal, width = 20)
operation_label1 = Label (calcframe, text = "=", font = equation)
operation_label2 = Label (calcframe, text = "=", font = equation)
operation_dropdown = OptionMenu (calcframe, operation_var, "<", ">")
result_label = Label (calcframe, text = "Result will be shown here.", font = inline)


header_normal.grid (row = 0, column = 0, columnspan = 3, pady = (0, 20))
mean_label.grid (row = 1, column = 0, sticky = W, padx = 3)
mean_entry.grid (row = 1, column = 2)
sd_dropdown.grid (row = 2, column = 0, sticky = W, padx = 3)
sd_entry.grid (row = 2, column = 2)
x_label.grid (row = 3, column = 0, sticky = W, padx = 3)
x_entry.grid (row = 3, column = 2, pady = 10)
normal_submit.grid (row = 4, column = 0, columnspan = 3)
operation_label1.grid (row = 1, column = 1)
operation_label2.grid (row = 2, column = 1)
operation_dropdown.grid (row = 3, column = 1)
result_label.grid(row = 5, column = 0, columnspan = 2)



root.mainloop()
