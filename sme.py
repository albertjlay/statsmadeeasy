from tkinter import *
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import tkinter.font as tkfont



root = Tk()
root.title ("Stats Made Easy")
root.geometry ("1200x800")

#Text Levels
header1 = tkfont.Font(size = 36, family = "Impact")
header2 = tkfont.Font(size = 18, family = "Impact")
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
        #Stores mean in mu
        mu = float(norm_mean_entry.get())
        #Stores X in random_var
        random_var = float(norm_x_entry.get())

        #Determines whether probability being searched is less than or more than X. Then calculate probability.
        if norm_operation_var.get() == "<":
            probability = (norm.cdf (random_var, loc = mu, scale = sigma))
            norm_result.config(text = "The probability that X is lower than " + str(random_var) + " is " + str(round(probability,3)))
        elif norm_operation_var.get() == ">":
            probability = 1 - (norm.cdf (random_var, loc = mu, scale = sigma))
            norm_result.config(text = "The probability that X is more than " + str(random_var) + " is " + str(round(probability,3)))

def graph_normal (x):
    if x == 0:
        #If variance was inputted, change to SD first before calculaton. If SD, store SD as float.
        if norm_sd_var.get() == "Variance":
            sigma = math.sqrt(float(norm_sd_entry.get()))
        else:
            sigma = float(norm_sd_entry.get())

        #Stores mean in mu
        mu = float(norm_mean_entry.get())

        #Sets x limits based on mu and sigma. Sets y limits based on height of mean.
        plt.xlim(mu - 4 * sigma, mu + 4 * sigma)
        plt.ylim (0, norm.pdf(mu, mu, sigma) + 0.1)

        #Stores legendx and legendy in variables
        legendx = norm_legendx_entry.get().strip()
        legendy = norm_legendy_entry.get().strip()
        #Sets up labels for x-axis and y-axis, if inputted.
        if legendx != "Optional" and legendx != "":
            plt.xlabel (legendx)
        if legendy != "Optional" and legendy != "":
            plt.ylabel (legendy)

        #Generates 200 plot points linearly spaced between (mean - 4SD) and (mean + 4SD) for x-axis
        x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 200)
        #Inserts all 200 values of X into a pdf of normal distribution
        y = norm.pdf(x, mu, sigma)
        #Plots coordinates and show graph
        plt.plot (x, y, color = "#14a795")
        plt.show()


#Function that checks for bad inputs. Also takes a parameter a which will be used to determine whether graph or calculate is desired.
def normal_errorcheck(a):
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
    if a == 0:
        normal (x)
    elif a == 1:
        graph_normal (x)


#Frame for Normal distribution section.
normalframe = LabelFrame (root)
normalframe.grid (row = 0, column = 1, padx = 20)

#Inside of normalframe
#Stores whether user chooses SD or variance.
norm_sd_var = StringVar()
norm_sd_var.set("Standard Deviation")

#Stores which operation user chooses.
norm_operation_var = StringVar()
norm_operation_var.set("<")

norm_header = Label (normalframe, text = "Normal Distribution", width = 20, font = header1, fg = "#14a795")

norm_calculate_label = Label (normalframe, text = "Calculate Probability", width = 20, font = header2, anchor = W)

norm_mean_label = Label (normalframe, text = "Mean", font = equation)
norm_mean_entry = Entry (normalframe, width = 25)

norm_sd_dropdown = OptionMenu (normalframe, norm_sd_var, "Standard Deviation", "Variance")
norm_sd_dropdown.config (font = equation, width = 15, anchor = W, padx = 10)
norm_sd_entry = Entry (normalframe, width = 25)

norm_x_label = Label (normalframe, text = "X", font = equation)
norm_x_entry = Entry (normalframe, width = 25)

norm_calculate = Button (normalframe, text = "CALCULATE", font = inline, command = lambda: normal_errorcheck(0), width = 60)

#Tuple for all norm_entry fields
norm_entries = (norm_mean_entry, norm_sd_entry, norm_x_entry)

norm_operation_label1 = Label (normalframe, text = "=", font = equation)
norm_operation_label2 = Label (normalframe, text = "=", font = equation)
norm_operation_dropdown = OptionMenu (normalframe, norm_operation_var, "<", ">")

norm_result = Label (normalframe, text = "  ", font = inline, fg = "#14a795")



norm_graph_label = Label (normalframe, text = "Graph Function", width = 20, font = header2, anchor = W)
norm_graph_desc = Label (normalframe, text = "This section will graph a Normal distribution probability density function.", width = 60, font = inline, anchor = W)

norm_legendx_label = Label (normalframe, text = "x-axis label", font = equation)
norm_legendx_entry = Entry (normalframe, width = 25)
norm_legendx_entry.insert (0, "Optional")

norm_legendy_label = Label (normalframe, text = "y-axis label", font = equation)
norm_legendy_entry = Entry (normalframe, width = 25)
norm_legendy_entry.insert (0, "Optional")

norm_operation_label3 = Label (normalframe, text = "=", font = equation)
norm_operation_label4 = Label (normalframe, text = "=", font = equation)

norm_graph = Button (normalframe, text = "GRAPH", font = inline, command = lambda : normal_errorcheck(1), width = 60)



#Places Normal widget on screen
norm_header.grid (row = 0, column = 0, columnspan = 3, pady = (0, 20))
norm_calculate_label.grid (row = 2, column = 0, padx = 3)
norm_mean_label.grid (row = 3, column = 0, sticky = W, padx = 3)
norm_mean_entry.grid (row = 3, column = 2)
norm_sd_dropdown.grid (row = 4, column = 0, sticky = W, padx = 3)
norm_sd_entry.grid (row = 4, column = 2)
norm_x_label.grid (row = 5, column = 0, sticky = W, padx = 3)
norm_x_entry.grid (row = 5, column = 2, pady = 10)
norm_calculate.grid (row = 6, column = 0, columnspan = 3)
norm_operation_label1.grid (row = 3, column = 1)
norm_operation_label2.grid (row = 4, column = 1)
norm_operation_dropdown.grid (row = 5, column = 1)
norm_result.grid(row = 7, column = 0, columnspan = 3)

norm_graph_label.grid (row = 8, column = 0, padx = 3, pady = (20, 0), columnspan = 3, sticky = W)
norm_graph_desc.grid (row = 9, column = 0, columnspan = 3, padx = 1, sticky = W)
norm_legendx_label.grid (row = 10, column = 0, sticky = W, padx = 3)
norm_legendx_entry.grid (row = 10, column = 2)
norm_legendy_label.grid (row = 11, column = 0, sticky = W, padx = 3)
norm_legendy_entry.grid (row = 11, column = 2)
norm_operation_label3.grid (row = 10, column = 1)
norm_operation_label4.grid (row = 11, column = 1)
norm_graph.grid (row = 12, column = 0, columnspan = 3)





root.mainloop()
