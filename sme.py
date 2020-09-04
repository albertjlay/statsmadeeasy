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
def normal (x):
    if x == 0:
        #If variance was inputted, change to SD first before calculaton. If SD, store SD as float.
        if norm_sd_var.get() == "Variance":
            sigma = math.sqrt(float(norm_sd_entry.get()))
        else:
            sigma = float(norm_sd_entry.get())

            #Determines whether probability being searched is less than or more than X. Then calculate probability.
            if norm_operation_var.get() == "<":
                probability = (norm.cdf (float(norm_x_entry.get()), loc = float(norm_mean_entry.get()), scale = sigma))
                norm_result.config(text = "The probability that X is lower than " + norm_x_entry.get() + " is " + str(round(probability,3)))
            elif norm_operation_var.get() == ">":
                probability = 1 - (norm.cdf (float(norm_x_entry.get()), loc = float(norm_mean_entry.get()), scale = sigma))
                norm_result.config(text = "The probability that X is more than " + norm_x_entry.get() + " is " + str(round(probability,3)))


def normal_errorcheck():
    #x is variable that will be returned to the normal function to indicate whether an error occurred. 0 means no error.
    x = 0
    for i in norm_entries:
        #Checks for Error 1 : No input was given
        if i.get().strip() == "":
            i.insert (0,"Error 1: Please insert a parameter.")
            x = 1
        else:
            #Checks for error 2: Input was not a number.
            try:
                float(i.get().strip())
            except:
                i.delete (0, END)
                i.insert (0,"Error 2: Please insert a valid number.")
                x = 2
    normal (x)


#Frame for Normal distribution section.
normalframe = LabelFrame (root)
normalframe.grid (row = 0, column = 1, padx = 80)

#Inside of normalframe
#Stores whether user chooses SD or variance.
norm_sd_var = StringVar()
norm_sd_var.set("Standard Deviation")

#Stores which operation user chooses.
norm_operation_var = StringVar()
norm_operation_var.set("<")

norm_header = Label (normalframe, text = "Normal Distribution", width = 20, font = header1, fg = "#14a795")

norm_mean_label = Label (normalframe, text = "Mean", font = equation)
norm_mean_entry = Entry (normalframe, width = 25)

norm_sd_dropdown = OptionMenu (normalframe, norm_sd_var, "Standard Deviation", "Variance")
norm_sd_dropdown.config (font = equation, width = 15, anchor = W, padx = 10)
norm_sd_entry = Entry (normalframe, width = 25)

norm_x_label = Label (normalframe, text = "X", font = equation)
norm_x_entry = Entry (normalframe, width = 25)

norm_submit = Button (normalframe, text = "CALCULATE", font = inline, command = normal_errorcheck, width = 20)

norm_operation_label1 = Label (normalframe, text = "=", font = equation)
norm_operation_label2 = Label (normalframe, text = "=", font = equation)
norm_operation_dropdown = OptionMenu (normalframe, norm_operation_var, "<", ">")

norm_result = Label (normalframe, text = "Result will be shown here.", font = inline)

#Tuple for all norm_entry fields
norm_entries = (norm_mean_entry, norm_sd_entry, norm_x_entry)

#Places Normal widget on screen
norm_header.grid (row = 0, column = 0, columnspan = 3, pady = (0, 20))
norm_mean_label.grid (row = 1, column = 0, sticky = W, padx = 3)
norm_mean_entry.grid (row = 1, column = 2)
norm_sd_dropdown.grid (row = 2, column = 0, sticky = W, padx = 3)
norm_sd_entry.grid (row = 2, column = 2)
norm_x_label.grid (row = 3, column = 0, sticky = W, padx = 3)
norm_x_entry.grid (row = 3, column = 2, pady = 10)
norm_submit.grid (row = 4, column = 0, columnspan = 3)
norm_operation_label1.grid (row = 1, column = 1)
norm_operation_label2.grid (row = 2, column = 1)
norm_operation_dropdown.grid (row = 3, column = 1)
norm_result.grid(row = 5, column = 0, columnspan = 3)



root.mainloop()
