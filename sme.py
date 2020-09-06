from tkinter import *
from scipy.stats import norm, binom,poisson
import matplotlib.pyplot as plt
import numpy as np
import tkinter.font as tkfont



root = Tk()
root.title ("Stats Made Easy")
root.geometry ("1400x500")

#Text Levels
header1 = tkfont.Font(size = 36, family = "Impact")
header2 = tkfont.Font(size = 18, family = "Impact")
inline = tkfont.Font(size = 14, family = "Helvetica")
equation = tkfont.Font(size = 14, family = "Baskerville")
result =  tkfont.Font(size = 18, family = "Baskerville")



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
            norm_result.config(text = "P ( X < " + str(random_var) + " ) = " + str(round(probability,norm_accuracy_var.get())))
        elif norm_operation_var.get() == ">":
            probability = 1 - (norm.cdf (random_var, loc = mu, scale = sigma))
            norm_result.config(text = "P ( X > " + str(random_var) + " ) = " + str(round(probability,norm_accuracy_var.get())))

def graph_normal (n):
    if n == 0:
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
        if legendx != "":
            plt.xlabel (legendx)
        if legendy != "":
            plt.ylabel (legendy)

        #Generates 200 plot points linearly spaced between (mean - 4SD) and (mean + 4SD) for x-axis
        x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 200)

        #Inserts all 200 values of X into a pdf of normal distribution
        y = norm.pdf(x, mu, sigma)
        #Plots coordinates and show graph
        plt.plot (x, y, color = "#ea5252")

        #Colors the area under the normal distribution that corresponds to probability
        if norm_operation_var.get() == "<":    #Colors from (mean - 4SD) to X
            #Generates 200 plot points, linearly spaced in range.
            a = np.linspace (mu - 4*sigma, float(norm_x_entry.get()), 200)
            #Colors according to range. Note that norm.pdf is used instead of y because the first parameter must be according to area. If not, a different norm will be created.
            plt.fill_between (a, norm.pdf(a, mu, sigma), color = "#ea5252")
        else:    #Colors from X to (mean + 4SD)
            a = np.linspace (float(norm_x_entry.get()), mu + 4 * sigma, 200)
            #Colors according to range. Note that norm.pdf is used instead of y because the first parameter must be according to area. If not, a different norm will be created.
            plt.fill_between (a, norm.pdf(a, mu, sigma), color = "#ea5252")

        #Shows figure in matplotlib software
        plt.show()


#Function that checks for bad inputs. Also takes a parameter a which will be used to determine whether graph or calculate is desired.
def normal_errorcheck(a):
    #m is variable that will be returned to the normal function to indicate whether an error occurred. 0 means no error.
    m = 0
    for i in norm_entries:
        #Checks for Error 1 : No input was given
        if i.get().strip() == "":
            i.insert (0,"Error 1: This is a required field.")
            m = 1
        else:
            #Checks for error 2: Input was not a number.
            try:
                float(i.get().strip())
            except:
                i.delete (0, END)
                i.insert (0,"Error 2: Input must be a number.")
                m = 2
    if a == 0:
        normal (m)
    elif a == 1:
        graph_normal (m)


#Frame for Normal distribution section.
normalframe = LabelFrame (root)
normalframe.grid (row = 0, column = 0, padx = 20)

#Inside of normalframe
#Stores whether user chooses SD or variance.
norm_sd_var = StringVar()
norm_sd_var.set("Standard Deviation")

#Stores which operation user chooses.
norm_operation_var = StringVar()
norm_operation_var.set("<")

#Stores Accuracy
norm_accuracy_var = IntVar()
norm_accuracy_var.set(3)

norm_header = Label (normalframe, text = "Normal Distribution", width = 20, font = header1, fg = "#ea5252")

norm_calculate_label = Label (normalframe, text = "Calculate Probability", width = 20, font = header2, anchor = W)
norm_calculate_desc = Label (normalframe, text = "This section will calculate the probability of a random variable X.", width = 50, font = inline, anchor = W)

norm_mean_label = Label (normalframe, text = "Mean", font = equation)
norm_mean_entry = Entry (normalframe, width = 15)

norm_sd_dropdown = OptionMenu (normalframe, norm_sd_var, "Standard Deviation", "Variance")
norm_sd_dropdown.config (font = equation, width = 15, anchor = W, padx = 10)
norm_sd_entry = Entry (normalframe, width = 15)

norm_x_label = Label (normalframe, text = "X", font = equation)
norm_x_entry = Entry (normalframe, width = 15)

norm_accuracy_label =  Label (normalframe, text = "Accuracy (d.p.)", font = equation)
norm_accuracy_dropdown = OptionMenu (normalframe, norm_accuracy_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
norm_accuracy_dropdown.config (width = 13)

norm_calculate = Button (normalframe, text = "CALCULATE", font = inline, command = lambda: normal_errorcheck(0), width = 50, height = 2)

#Tuple for all norm_entry fields
norm_entries = (norm_mean_entry, norm_sd_entry, norm_x_entry)

norm_operation_label1 = Label (normalframe, text = "=", font = equation)
norm_operation_label2 = Label (normalframe, text = "=", font = equation)
norm_operation_label3 = Label (normalframe, text = "=", font = equation)
norm_operation_dropdown = OptionMenu (normalframe, norm_operation_var, "<", ">")

norm_result = Label (normalframe, text = "  ", font = result, fg = "#ea5252")


norm_graph_label = Label (normalframe, text = "Graph Function", width = 20, font = header2, anchor = W)
norm_graph_desc = Label (normalframe, text = "This section will graph a Normal distribution PDF.", width = 50, font = inline, anchor = W)

norm_legendx_label = Label (normalframe, text = "x-axis label (optional)", font = equation)
norm_legendx_entry = Entry (normalframe, width = 15)

norm_legendy_label = Label (normalframe, text = "y-axis label (optional)", font = equation)
norm_legendy_entry = Entry (normalframe, width = 15)

norm_operation_labela = Label (normalframe, text = "=", font = equation)
norm_operation_labelb = Label (normalframe, text = "=", font = equation)

norm_graph = Button (normalframe, text = "GRAPH", font = inline, command = lambda : normal_errorcheck(1), width = 50, height = 2, bg = "black")






#Places Normal widget on screen
norm_header.grid (row = 0, column = 0, columnspan = 3, pady = (0, 20))
norm_calculate_label.grid (row = 1, column = 0, padx = 3)
norm_calculate_desc.grid(row = 2, column = 0 , padx = 3, columnspan = 3, sticky = W)
norm_mean_label.grid (row = 3, column = 0, sticky = W, padx = 3)
norm_mean_entry.grid (row = 3, column = 2)
norm_sd_dropdown.grid (row = 4, column = 0, sticky = W, padx = 3)
norm_sd_entry.grid (row = 4, column = 2)
norm_x_label.grid (row = 5, column = 0, sticky = W, padx = 3)
norm_x_entry.grid (row = 5, column = 2)
norm_calculate.grid (row = 6, column = 0, columnspan = 3, pady = 3)
norm_accuracy_label.grid (row = 7, column = 0, sticky = W)
norm_accuracy_dropdown.grid (row = 7, column = 2)
norm_operation_label1.grid (row = 3, column = 1)
norm_operation_label2.grid (row = 4, column = 1)
norm_operation_dropdown.grid (row = 5, column = 1)
norm_operation_label3.grid (row = 7, column = 1)
norm_result.grid(row = 8, column = 0, columnspan = 3, pady = (10,0))

norm_graph_label.grid (row = 9, column = 0, padx = 3, pady = (20, 0), columnspan = 3, sticky = W)
norm_graph_desc.grid (row = 10, column = 0, columnspan = 3, padx = 3, sticky = W)
norm_legendx_label.grid (row = 11, column = 0, sticky = W, padx = 3)
norm_legendx_entry.grid (row = 11, column = 2)
norm_legendy_label.grid (row = 12, column = 0, sticky = W, padx = 3)
norm_legendy_entry.grid (row = 12, column = 2)
norm_operation_labela.grid (row = 11, column = 1)
norm_operation_labelb.grid (row = 12, column = 1)
norm_graph.grid (row = 13, column = 0, columnspan = 3, pady = 3)




#Function to calculate binomial probability
def binomial (m):
    if m == 0:
        #Stores entries in variables.
        n = int(binom_n_entry.get().strip())
        p = float (binom_p_entry.get().strip())
        y = int (binom_y_entry.get().strip())

        #Initializes probability to 0
        probability = 0

        if binom_operation_var.get() == "=":
            probability = binom.pmf(y, n, p)
            binom_result.config(text = "P ( Y = " + str(y) + " ) = " + str(round(probability,binom_accuracy_var.get())))

        #Cumulative probabilities
        elif binom_operation_var.get() == "<" or binom_operation_var.get() == "<=":
            for i in range (0, y):
                probability += binom.pmf(i, n, p)
            if binom_operation_var.get() == "<=":
                probability += binom.pmf (y,n,p)
                binom_result.config(text = "P ( Y <= " + str(y) + " ) = " + str(round(probability,binom_accuracy_var.get())))
            else:
                binom_result.config(text = "P ( Y < " + str(y) + " ) = " + str(round(probability,binom_accuracy_var.get())))
        else:
            for i in range (y + 1,n + 1):
                probability += binom.pmf(i, n, p)
            if binom_operation_var.get() == ">=":
                probability += binom.pmf (y,n,p)
                binom_result.config(text = "P ( Y >= " + str(y) + " ) = " + str(round(probability,binom_accuracy_var.get())))
            else:
                binom_result.config(text = "P ( Y > " + str(y) + " ) = " + str(round(probability,binom_accuracy_var.get())))




#Function that checks for bad inputs.
def binom_errorcheck():
    #m is variable that will be returned to the binomial function to indicate whether an error occurred. 0 means no error.
    m = 0
    for i in binom_entries:
        #Checks for Error 1 : No input was given
        if i.get().strip() == "":
            i.insert (0,"Error 1: This is a required field.")
            m = 1
        else:
            #Checks for Error 2 : i is not a number
            try:
                float(i.get().strip())
            except:
                i.delete (0, END)
                i.insert (0,"Error 2: Input must be a number.")
                m = 2

    if m == 0: #If all entry fields are numbers.
        #Assigns entries to variables.
        p = float(binom_p_entry.get().strip())
        n = float (binom_n_entry.get().strip())
        y = float(binom_y_entry.get().strip())

        #Checks for Error 3: p is not between 0 and 1, inclusive.
        if p > 1 or p < 0:
            binom_p_entry.delete(0, END)
            binom_p_entry.insert(0, "Error 3: p must be between 0 and 1 inclusive")
            m = 3

        #Checks for error 4: n is not an integer
        try:

            int (n)
            #Checks for error 5: n is not positive
            if n < 1:
                binom_n_entry.delete(0, END)
                binom_n_entry.insert(0, "Error 5: n must be positive")
                m = 5
        except:
            binom_n_entry.delete(0, END)
            binom_n_entry.insert(0, "Error 4: n must be an integer.")
            m = 4

        #Checks for error 4: n is not an integer
        try:
            int (y)
            #Checks for error 5: y is not positive
            if y < 1:
                binom_y_entry.delete(0, END)
                binom_y_entry.insert(0, "Error 5: Y is not positive.")
                m = 5
            #Checks for error 6: y is not in range of n
            if y > n:
                binom_y_entry.delete(0, END)
                binom_y_entry.insert(0, "Error 6: Y must be between 0 and n, inclusive.")
                m = 6
        except:
            binom_y_entry.delete(0, END)
            binom_y_entry.insert(0, "Error 4: Y must be an integer.")
            m = 4

    binomial (m)



#Frame for Normal distribution section.
binomframe = LabelFrame (root)
binomframe.grid (row = 0, column = 1, padx = 20)

#Inside of binomframe

#Stores which operation user chooses.
binom_operation_var = StringVar()
binom_operation_var.set("=")

#Stores Accuracy
binom_accuracy_var = IntVar()
binom_accuracy_var.set(3)

binom_header = Label (binomframe, text = "Binomial Distribution", width = 20, font = header1, fg = "#a9df32")

binom_calculate_label = Label (binomframe, text = "Calculate Probability", width = 20, font = header2, anchor = W)
binom_calculate_desc = Label (binomframe, text = "This section will calculate the probability of a random variable Y.", width = 50, font = inline, anchor = W)

binom_n_label = Label (binomframe, text = "n (Number of occurences)", font = equation)
binom_n_entry = Entry (binomframe, width = 15)

binom_p_label = Label (binomframe, text = "p (Probability of success)", font = equation)
binom_p_entry = Entry (binomframe, width = 15)

binom_y_label = Label (binomframe, text = "Y", font = equation)
binom_y_entry = Entry (binomframe, width = 15)

binom_accuracy_label =  Label (binomframe, text = "Accuracy (d.p.)", font = equation)
binom_accuracy_dropdown = OptionMenu (binomframe, binom_accuracy_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
binom_accuracy_dropdown.config (width = 13)

binom_calculate = Button (binomframe, text = "CALCULATE", font = inline, command = binom_errorcheck, width = 50, height = 2)

#Tuple for all norm_entry fields
binom_entries = (binom_n_entry, binom_p_entry, binom_y_entry)

binom_operation_label1 = Label (binomframe, text = "=", font = equation)
binom_operation_label2 = Label (binomframe, text = "=", font = equation)
binom_operation_label3 = Label (binomframe, text = "=", font = equation)
binom_operation_dropdown = OptionMenu (binomframe, binom_operation_var, "=", "<", "<=", ">", ">=")

binom_result = Label (binomframe, text = "  ", font = result, fg = "#a9df32")




#Places Normal widget on screen
binom_header.grid (row = 0, column = 0, columnspan = 3, pady = (0, 20))
binom_calculate_label.grid (row = 1, column = 0, padx = 3)
binom_calculate_desc.grid(row = 2, column = 0 , padx = 3, columnspan = 3, sticky = W)
binom_p_label.grid (row = 3, column = 0, sticky = W, padx = 3)
binom_p_entry.grid (row = 3, column = 2)
binom_n_label.grid (row = 4, column = 0, sticky = W, padx = 3)
binom_n_entry.grid (row = 4, column = 2)
binom_y_label.grid (row = 5, column = 0, sticky = W, padx = 3)
binom_y_entry.grid (row = 5, column = 2)
binom_calculate.grid (row = 6, column = 0, columnspan = 3, pady = 3)
binom_accuracy_label.grid (row = 7, column = 0, sticky = W)
binom_accuracy_dropdown.grid (row = 7, column = 2)
binom_result.grid(row = 8, column = 0, columnspan = 3, pady = (10, 173))


binom_operation_label1.grid (row = 3, column = 1)
binom_operation_label2.grid (row = 4, column = 1)
binom_operation_dropdown.grid (row = 5, column = 1)
binom_operation_label3.grid (row = 7, column = 1)






#Function to calculate Poisson probability
def poisson (m):
    if m == 0:
        #Stores entries in variables.
        l = float (poisson_l_entry.get().strip())
        z = int (poisson_z_entry.get().strip())

        #Initializes probability to 0
        probability = 0

        if poisson_operation_var.get() == "=":
            probability = poisson.pmf(z, l)
            poisson_result.config(text = "P ( Z = " + str(z) + " ) = " + str(round(probability,poisson_accuracy_var.get())))

        #Cumulative probabilities
        elif poisson_operation_var.get() == "<" or poisson_operation_var.get() == "<=":
            for i in range (0, z):
                probability += poisson.pmf(i, l)
            if poisson_operation_var.get() == "<=":
                probability += poisson.pmf (z, l)
                poisson_result.config(text = "P ( Z <= " + str(z) + " ) = " + str(round(probability,poisson_accuracy_var.get())))
            else:
                poisson_result.config(text = "P ( Z < " + str(z) + " ) = " + str(round(probability,poisson_accuracy_var.get())))
        else: #Uses the identity that all sum of all probability = 1
            probability = 1
            for i in range (0, z):
                probability -= poisson.pmf(i, l)
            if poisson_operation_var.get() == ">":
                probability -= poisson.pmf(z,l)
                poisson_result.config(text = "P ( Z > " + str(z) + " ) = " + str(round(probability,poisson_accuracy_var.get())))
            else:
                poisson_result.config(text = "P ( Z >= " + str(z) + " ) = " + str(round(probability,poisson_accuracy_var.get())))


#Function that checks for bad inputs.
def poisson_errorcheck():
    #m is variable that will be returned to the binomial function to indicate whether an error occurred. 0 means no error.
    m = 0
    for i in poisson_entries:
        #Checks for Error 1 : No input was given
        if i.get().strip() == "":
            i.insert (0,"Error 1: This is a required field")
            m = 1
        else:
            #Checks for Error 2: Input not float
            try:
                float(i.get().strip())
                #Check for Error 3: Input not positive
                if i < 0:
                    poisson_z_entry.delete(0, END)
                    poisson_z_entry.insert(0, "Error 3: Input must be positive.")
                    m = 3
            except:
                i.delete (0, END)
                i.insert (0,"Error 2: Input was not a float.")
                m = 2

    poisson (m)



#Frame for Poisson distribution section.
poissonframe = LabelFrame (root)
poissonframe.grid (row = 0, column = 2, padx = 20)


#Inside of poissonframe
#Stores which operation user chooses.
poisson_operation_var = StringVar()
poisson_operation_var.set("=")

#Stores Accuracy
poisson_accuracy_var = IntVar()
poisson_accuracy_var.set(3)

poisson_header = Label (poissonframe, text = "Poisson Distribution", width = 20, font = header1, fg = "#14a795")

poisson_calculate_label = Label (poissonframe, text = "Calculate Probability", width = 20, font = header2, anchor = W)
poisson_calculate_desc = Label (poissonframe, text = "This section will calculate the probability of a random variable Z.", width = 50, font = inline, anchor = W)

poisson_l_label = Label (poissonframe, text = "λ (Mean number of events)", font = equation)
poisson_l_entry = Entry (poissonframe, width = 15)

poisson_z_label = Label (poissonframe, text = "Z", font = equation)
poisson_z_entry = Entry (poissonframe, width = 15)

poisson_accuracy_label =  Label (poissonframe, text = "Accuracy (d.p.)", font = equation)
poisson_accuracy_dropdown = OptionMenu (poissonframe, poisson_accuracy_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
poisson_accuracy_dropdown.config (width = 13)

poisson_calculate = Button (poissonframe, text = "CALCULATE", font = inline, command = poisson_errorcheck, width = 50, height = 2)

#Tuple for all poisson_entry fields
poisson_entries = (poisson_l_entry, poisson_z_entry)

poisson_operation_label1 = Label (poissonframe, text = "=", font = equation)
poisson_operation_label2 = Label (poissonframe, text = "=", font = equation)
poisson_operation_dropdown = OptionMenu (poissonframe, poisson_operation_var, "=", "<", "<=", ">", ">=")

poisson_result = Label (poissonframe, text = "  ", font = result, fg = "#14a795")




#Places Poisson widget on screen
poisson_header.grid (row = 0, column = 0, columnspan = 3, pady = (0, 20))
poisson_calculate_label.grid (row = 1, column = 0, padx = 3)
poisson_calculate_desc.grid(row = 2, column = 0 , padx = 3, columnspan = 3, sticky = W)
poisson_l_label.grid (row = 3, column = 0, sticky = W, padx = 3)
poisson_l_entry.grid (row = 3, column = 2)
poisson_z_label.grid (row = 4, column = 0, sticky = W, padx = 3)
poisson_z_entry.grid (row = 4, column = 2)
poisson_calculate.grid (row = 5, column = 0, columnspan = 3, pady = 3)
poisson_accuracy_label.grid (row = 6, column = 0, sticky = W)
poisson_accuracy_dropdown.grid (row = 6, column = 2)
poisson_result.grid(row = 7, column = 0, columnspan = 3, pady = (10, 200))


poisson_operation_label1.grid (row = 3, column = 1)
poisson_operation_label2.grid (row = 6, column = 1)
poisson_operation_dropdown.grid (row = 4, column = 1)


root.mainloop()
