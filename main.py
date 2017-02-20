import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

import matplotlib.animation as animation
from matplotlib import style

from matplotlib.figure import Figure

import matplotlib.dates as mdates
import matplotlib.ticker as mticker

from scipy import stats
from scipy.stats import norm
import scipy.special
from scipy.special import erf


import numpy as np
import matplotlib.pyplot as plt
import math

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import numpy as np

import pylab
from pylab import *

from scipy.optimize import fsolve



LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
MEDIUM_FONT_BOLD = ("Verdana", 10, "bold")

style.use("dark_background")



def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!!!")
    label = ttk.Label(popup, text=msg, font=MEDIUM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="OK", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def errormsg(msg):
    tk.messagebox.showerror("Error", msg)


def exit_command(self):
    if tk.messagebox.askokcancel("Quit", "Do you really want to quit?"):
        self.destroy()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Method 1", command=lambda: controller.show_frame(Experiment))
        button1.pack()

        button2 = ttk.Button(self, text="Method 2", command=lambda: controller.show_frame(Empirical))
        button2.pack()

        button3 = ttk.Button(self, text="Method 3", command=lambda: controller.show_frame(Deterministic))
        button3.pack()

        button4 = ttk.Button(self, text="Quit", command=quit)
        button4.pack()


############################################################################################################################
class TesisApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "FATIGUE FAILURE ANALYSIS")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Print", command=lambda: errormsg("Not Finished Yet!!!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: exit_command(self))
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self, menu=menubar)
        self.frames = {}

        for F in (StartPage, Experiment, Empirical,Deterministic):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


# MULTI STRESS LEVEL
###########################################################################################################################
def choiceone(self):
    self.labeln1 = ttk.Label(self, text="1", justify="center")
    self.labeln1.grid(row=7, column=1)

    self.entry1 = ttk.Entry(self, width=15)
    self.entry1.grid(row=7, column=2)

    self.entry2 = ttk.Entry(self, width=15)
    self.entry2.grid(row=7, column=3)

    self.entry3 = ttk.Entry(self, width=15)
    self.entry3.grid(row=7, column=4)

    self.entry4 = ttk.Entry(self, width=15)
    self.entry4.grid(row=7, column=5)


def choicetwo(self):
    self.labeln2 = ttk.Label(self, text="2", justify="center")
    self.labeln2.grid(row=9, column=1)

    self.entry5 = ttk.Entry(self, width=15)
    self.entry5.grid(row=9, column=2)

    self.entry6 = ttk.Entry(self, width=15)
    self.entry6.grid(row=9, column=3)

    self.entry7 = ttk.Entry(self, width=15)
    self.entry7.grid(row=9, column=4)

    self.entry8 = ttk.Entry(self, width=15)
    self.entry8.grid(row=9, column=5)


def choicethree(self):
    self.labeln3 = ttk.Label(self, text="3", justify="center")
    self.labeln3.grid(row=11, column=1)

    self.entry9 = ttk.Entry(self, width=15)
    self.entry9.grid(row=11, column=2)

    self.entry10 = ttk.Entry(self, width=15)
    self.entry10.grid(row=11, column=3)

    self.entry11 = ttk.Entry(self, width=15)
    self.entry11.grid(row=11, column=4)

    self.entry12 = ttk.Entry(self, width=15)
    self.entry12.grid(row=11, column=5)


def choicefour(self):
    self.labeln4 = ttk.Label(self, text="4", justify="center")
    self.labeln4.grid(row=13, column=1)

    self.entry13 = ttk.Entry(self, width=15)
    self.entry13.grid(row=13, column=2)

    self.entry14 = ttk.Entry(self, width=15)
    self.entry14.grid(row=13, column=3)

    self.entry15 = ttk.Entry(self, width=15)
    self.entry15.grid(row=13, column=4)

    self.entry16 = ttk.Entry(self, width=15)
    self.entry16.grid(row=13, column=5)


def choicefive(self):
    self.labeln5 = ttk.Label(self, text="5", justify="center")
    self.labeln5.grid(row=15, column=1)

    self.entry17 = ttk.Entry(self, width=15)
    self.entry17.grid(row=15, column=2)

    self.entry18 = ttk.Entry(self, width=15)
    self.entry18.grid(row=15, column=3)

    self.entry19 = ttk.Entry(self, width=15)
    self.entry19.grid(row=15, column=4)

    self.entry20 = ttk.Entry(self, width=15)
    self.entry20.grid(row=15, column=5)

def deleteone(self):
    self.entry1.delete(0, 'end')
    self.entry2.delete(0, 'end')
    self.entry3.delete(0, 'end')
    self.entry4.delete(0, 'end')

def deletetwo(self):
    self.entry5.delete(0, 'end')
    self.entry6.delete(0, 'end')
    self.entry7.delete(0, 'end')
    self.entry8.delete(0, 'end')


def deletethree(self):
    self.entry9.delete(0, 'end')
    self.entry10.delete(0, 'end')
    self.entry11.delete(0, 'end')
    self.entry12.delete(0, 'end')

def deletefour(self):
    self.entry13.delete(0, 'end')
    self.entry14.delete(0, 'end')
    self.entry15.delete(0, 'end')
    self.entry16.delete(0, 'end')


def deletefive(self):
    self.entry17.delete(0, 'end')
    self.entry18.delete(0, 'end')
    self.entry19.delete(0, 'end')
    self.entry20.delete(0, 'end')

def gridremoveone(self):
    self.entry1.grid_forget()
    self.entry2.grid_forget()
    self.entry3.grid_forget()
    self.entry4.grid_forget()

    self.labeln1.grid_forget()

def gridremovetwo(self):
    self.entry5.grid_forget()
    self.entry6.grid_forget()
    self.entry7.grid_forget()
    self.entry8.grid_forget()

    self.labeln2.grid_forget()

def gridremovethree(self):
    self.entry9.grid_forget()
    self.entry10.grid_forget()
    self.entry11.grid_forget()
    self.entry12.grid_forget()

    self.labeln3.grid_forget()

def gridremovefour(self):
    self.entry13.grid_forget()
    self.entry14.grid_forget()
    self.entry15.grid_forget()
    self.entry16.grid_forget()

    self.labeln4.grid_forget()

def gridremovefive(self):
    self.entry17.grid_forget()
    self.entry18.grid_forget()
    self.entry19.grid_forget()
    self.entry20.grid_forget()

    self.labeln5.grid_forget()

def saveexp(self):
    if float(self.entry0.get())==1:
        fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str("Cycles") +"\t"+ str("PoF") +"\n"+ \
                    '\n'.join('\t'.join(map(str,x)) for x in zip(self.a1,self.pof1))
        fout.write(text2save)
        fout.close()

    elif float(self.entry0.get())==2:
        fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str("Cycles") +"\t"+ str("PoF1") +"\t"+ str("Cycles") +"\t"+ str("PoF2") +"\n"+\
                    '\n'.join('\t'.join(map(str,x)) for x in zip(self.a1,self.pof1,self.a2, self.pof2))
        fout.write(text2save)
        fout.close()

    elif float(self.entry0.get())==3:
        fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str("Cycles") +"\t"+ str("PoF1") +"\t"+ str("Cycles") +"\t"+ str("PoF2") +\
                    "\t"+ str("Cycles") +"\t"+ str("PoF3")+"\n"+\
                    '\n'.join('\t'.join(map(str,x)) for x in zip(self.a1, self.pof1, self.a2, self.pof2, self.a3, self.pof3))
        fout.write(text2save)
        fout.close()

    elif float(self.entry0.get())==4:
        fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str("Cycles") +"\t"+ str("PoF1") +"\t"+ str("Cycles") +"\t"+ str("PoF2") +\
                    "\t"+ str("Cycles") +"\t"+ str("PoF3")+"\t"+ str("Cycles") +"\t"+ str("PoF4")+"\n"+\
                    '\n'.join('\t'.join(map(str,x)) for x in zip(self.a1, self.pof1, self.a2, self.pof2, self.a3, self.pof3, self.a4, self.pof4))
        fout.write(text2save)
        fout.close()

    elif float(self.entry0.get())==5:
        fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str("Cycles") +"\t"+ str("PoF1") +"\t"+ str("Cycles") +"\t"+ str("PoF2") +\
                    "\t"+ str("Cycles") +"\t"+ str("PoF3")+"\t"+ str("Cycles") +"\t"+ str("PoF4")+"\t"+ str("Cycles") +"\t"+ str("pof5")+"\n"+\
                    '\n'.join('\t'.join(map(str,x)) for x in zip(self.a1, self.pof1, self.a2, self.pof2, self.a3, self.pof3, self.a4, self.pof4, self.a5, self.pof5))
        fout.write(text2save)
        fout.close()

class Experiment(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        homebutton=ttk.Button(self, text="Homepage", command=lambda: controller.show_frame(StartPage))
        homebutton.grid(row=1, column=1)

        backbutton=ttk.Button(self, text="Back", command=lambda: controller.show_frame(Empirical))
        backbutton.grid(row=1, column=2)

        labele1 = ttk.Label(self, text="METHOD 1", font=LARGE_FONT)
        labele1.grid(row=2, column=1, pady=5)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=3, columnspan=5, sticky="EW")

        label0 = ttk.Label(self, text="Number of \nStress Level: ", font=MEDIUM_FONT, justify="center")
        label0.grid(row=4, column=1, pady=5)
        self.entry0 = ttk.Entry(self, width=15)
        self.entry0.grid(row=4, column=2)

        button0 = ttk.Button(self, text="OK ", command=lambda: self.ok())
        button0.grid(row=4, column=3,sticky='w')

        choiceone(self)
        choicetwo(self)
        choicethree(self)
        choicefour(self)
        choicefive(self)

        gridremoveone(self)
        gridremovetwo(self)
        gridremovethree(self)
        gridremovefour(self)
        gridremovefive(self)


    def clear_txt(self):
        if float(self.entry0.get()) == 1:
            deleteone(self)

        elif float(self.entry0.get()) == 2:
            deleteone(self)
            deletetwo(self)

        elif float(self.entry0.get()) == 3:
            deleteone(self)
            deletetwo(self)
            deletethree(self)

        elif float(self.entry0.get()) == 4:
            deleteone(self)
            deletetwo(self)
            deletethree(self)
            deletefour(self)

        elif float(self.entry0.get()) == 5:
            deleteone(self)
            deletetwo(self)
            deletethree(self)
            deletefour(self)
            deletefive(self)


    def ok(self):
        try:
            float(self.entry0.get())

        except ValueError:
            errormsg("MASUKIN ANGKANNA LAH LEK")

        else:
            labele0 = ttk.Label(self, text="")
            labele0.grid(row=5, column=1)

            labeln = ttk.Label(self, text="No", justify="center",font=MEDIUM_FONT)
            labeln.grid(row=6, column=1)

            label1 = ttk.Label(self, text="Constant Stress \nAmplitude (Sa)", justify="center",font=SMALL_FONT)
            label1.grid(row=6, column=2)

            label2 = ttk.Label(self, text="Cycles to \nFailure (Nf)", justify="center",font=SMALL_FONT)
            label2.grid(row=6, column=3, padx=5)

            label3 = ttk.Label(self, text="Standard \nDeviation (σ Nf)", justify="center",font=SMALL_FONT)
            label3.grid(row=6, column=4, padx=3)

            label4 = ttk.Label(self, text="Applied\n Cycles (n)",justify="center",font=SMALL_FONT)
            label4.grid(row=6, column=5)

            labele1 = ttk.Label(self, text="")
            labele1.grid(row=8, column=1)

            labele2 = ttk.Label(self, text="")
            labele2.grid(row=10, column=1)

            labele3 = ttk.Label(self, text="")
            labele3.grid(row=12, column=1)

            labele3 = ttk.Label(self, text="")
            labele3.grid(row=14, column=1)

            labele4 = ttk.Label(self, text="")
            labele4.grid(row=21, column=1)

            button1 = ttk.Button(self, text="Calculate", command=lambda: self.calculate_sigmaD())
            button1.grid(row=16, column=5, pady=5, sticky='e')

            button2 = ttk.Button(self, text="Clear all ", command=lambda: self.clear_txt())
            button2.grid(row=16, column=6, pady=5, sticky='w')

            if float(self.entry0.get()) == 1:
                choiceone(self)

                gridremovetwo(self)
                gridremovethree(self)
                gridremovefour(self)
                gridremovefive(self)

            elif float(self.entry0.get()) == 2:
                choiceone(self)
                choicetwo(self)

                gridremovethree(self)
                gridremovefour(self)
                gridremovefive(self)

            elif float(self.entry0.get()) == 3:
                choiceone(self)
                choicetwo(self)
                choicethree(self)

                gridremovefour(self)
                gridremovefive(self)

            elif float(self.entry0.get()) == 4:
                choiceone(self)
                choicetwo(self)
                choicethree(self)
                choicefour(self)

                gridremovefive(self)

            elif float(self.entry0.get()) == 5:
                choiceone(self)
                choicetwo(self)
                choicethree(self)
                choicefour(self)
                choicefive(self)

            elif float(self.entry0.get()) > 5:
                errormsg("Cannot be more than 5")


    def calculate_sigmaD(self):
        try:
            float(self.entry0.get())

        except ValueError:
            errormsg("MASUKIN ANGKANNA LAH LEK")

        else:

            if float(self.entry0.get()) == 1:
                try:
                    float(self.entry1.get())
                    float(self.entry2.get())
                    float(self.entry3.get())
                    float(self.entry4.get())

                except ValueError:
                    errormsg("MASUKIN ANGKANNA LAH LEK")
                    print("")

                else:
                    button3 = ttk.Button(self, text="Save Result",width=23, command=lambda: saveexp(self))
                    button3.grid(row=17, column=5, columnspan=4, sticky='e')

                    sigmaDc1 = float(self.entry3.get())/float(self.entry2.get())

                    n1 = float(self.entry4.get())
                    self.a1 = np.arange(0.,n1,5000)

                    muD1 = self.a1/float(self.entry2.get())

                    Z1 = -(1-muD1)/np.sqrt((sigmaDc1**2)+muD1*(float(self.entry3.get())/float(self.entry2.get()))**2)
                    self.pof1 =(1.0 +erf(Z1/np.sqrt(2)))/2

                    style.use("dark_background")

                    f1 = plt.figure(figsize=(10,7))
                    plt.plot(self.a1,self.pof1, label=self.entry1.get()+" Mpa", color='#4dffdb', linewidth=1)

                    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

                    plt.xlabel("Number of Cycles")
                    plt.ylabel("Probability of Failure")

                    ax = plt.subplot(111)

                    box = ax.get_position()
                    ax.set_position([box.x0, box.y0 + box.height * -0.005,box.width, box.height * 0.95])
                    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),fancybox=True, shadow=True, ncol=5)

                    plt.show()


            elif float(self.entry0.get()) == 2:
                try:
                    float(self.entry1.get())
                    float(self.entry2.get())
                    float(self.entry3.get())
                    float(self.entry4.get())
                    float(self.entry5.get())
                    float(self.entry6.get())
                    float(self.entry7.get())
                    float(self.entry8.get())

                except ValueError:
                    errormsg("MASUKIN ANGKANNA LAH LEK")
                    print("")

                else:
                    button3 = ttk.Button(self, text="Save Result",width=23, command=lambda: saveexp(self))
                    button3.grid(row=17, column=5, columnspan=4, sticky='e')

                    #Stress Level 1
                    sigmaDc1 = float(self.entry3.get())/float(self.entry2.get())

                    n1 = float(self.entry4.get())
                    self.a1 = np.arange(0,n1,5000)

                    muD1 = self.a1/float(self.entry2.get())

                    Z1 = -(1-muD1)/np.sqrt((sigmaDc1**2)+muD1*(float(self.entry3.get())/float(self.entry2.get()))**2)
                    self.pof1 =(1.0 +erf(Z1/np.sqrt(2)))/2

                    #Stress Level 2
                    sigmaDc2 = float(self.entry7.get())/float(self.entry6.get())

                    n2 = float(self.entry8.get())
                    self.a2 = np.arange(0,n2,5000)

                    muD2 = self.a2/float(self.entry6.get())

                    Z2 = -(1-muD2)/np.sqrt((sigmaDc2**2)+muD2*(float(self.entry7.get())/float(self.entry6.get()))**2)
                    self.pof2 =(1.0 +erf(Z2/np.sqrt(2)))/2

                    #plot
                    style.use("dark_background")

                    f1 = plt.figure(figsize=(10,7))
                    plt.plot(self.a1, self.pof1, label=self.entry1.get()+" Mpa", color='#4dffdb', linewidth=1)
                    plt.plot(self.a2, self.pof2, label=self.entry5.get()+" Mpa", color='#ffff00', linewidth=1)

                    plt.axis([0,n2+10000,0,1.01])

                    plt.xlabel("Number of Cycles")
                    plt.ylabel("Probability of Failure")

                    ax = plt.subplot(111)

                    box = ax.get_position()
                    ax.set_position([box.x0, box.y0 + box.height * -0.005,box.width, box.height * 0.95])
                    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),fancybox=True, shadow=True, ncol=5)
                    plt.show()


            elif float(self.entry0.get()) == 3:
                try:
                    float(self.entry1.get())
                    float(self.entry2.get())
                    float(self.entry3.get())
                    float(self.entry4.get())
                    float(self.entry5.get())
                    float(self.entry6.get())
                    float(self.entry7.get())
                    float(self.entry8.get())
                    float(self.entry9.get())
                    float(self.entry10.get())
                    float(self.entry11.get())
                    float(self.entry12.get())

                except ValueError:
                    errormsg("MASUKIN ANGKANNA LAH LEK")
                    print("")

                else:
                    button3 = ttk.Button(self, text="Save Result",width=23, command=lambda: saveexp(self))
                    button3.grid(row=17, column=5, columnspan=4, sticky='e')

                    #Stress Level 1
                    sigmaDc1 = float(self.entry3.get())/float(self.entry2.get())

                    n1 = float(self.entry4.get())
                    self.a1 = np.arange(0,n1,5000)

                    muD1 = self.a1/float(self.entry2.get())

                    Z1 = -(1-muD1)/np.sqrt((sigmaDc1**2)+muD1*(float(self.entry3.get())/float(self.entry2.get()))**2)
                    self.pof1 =(1.0 +erf(Z1/np.sqrt(2)))/2

                    #Stress Level 2
                    sigmaDc2 = float(self.entry7.get())/float(self.entry6.get())

                    n2 = float(self.entry8.get())
                    self.a2 = np.arange(0,n2,5000)

                    muD2 = self.a2/float(self.entry6.get())

                    Z2 = -(1-muD2)/np.sqrt((sigmaDc2**2)+muD2*(float(self.entry7.get())/float(self.entry6.get()))**2)
                    self.pof2 =(1.0 +erf(Z2/np.sqrt(2)))/2

                    #Stress Level 3
                    sigmaDc3 = float(self.entry11.get())/float(self.entry10.get())

                    n3 = float(self.entry12.get())
                    self.a3 = np.arange(0,n3,5000)

                    muD3 = self.a3/float(self.entry10.get())

                    Z3 = -(1-muD3)/np.sqrt((sigmaDc3**2)+muD3*(float(self.entry11.get())/float(self.entry10.get()))**2)
                    self.pof3 =(1.0 +erf(Z3/np.sqrt(2)))/2

                    #plot
                    style.use("dark_background")

                    f1 = plt.figure(figsize=(10,7))
                    plt.plot(self.a1,self.pof1, label=self.entry1.get()+" Mpa", color='#4dffdb', linewidth=1)
                    plt.plot(self.a2,self.pof2, label=self.entry5.get()+" Mpa", color='#ffff00', linewidth=1)
                    plt.plot(self.a3,self.pof3, label=self.entry9.get()+" Mpa", color='#00ff00', linewidth=1)

                    plt.axis([0,n3+10000,0,1.01])

                    plt.xlabel("Number of Cycles")
                    plt.ylabel("Probability of Failure")

                    ax = plt.subplot(111)

                    box = ax.get_position()
                    ax.set_position([box.x0, box.y0 + box.height * -0.005,box.width, box.height * 0.95])
                    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),fancybox=True, shadow=True, ncol=5)
                    plt.show()

            elif float(self.entry0.get()) == 4:
                try:
                    float(self.entry1.get())
                    float(self.entry2.get())
                    float(self.entry3.get())
                    float(self.entry4.get())
                    float(self.entry5.get())
                    float(self.entry6.get())
                    float(self.entry7.get())
                    float(self.entry8.get())
                    float(self.entry9.get())
                    float(self.entry10.get())
                    float(self.entry11.get())
                    float(self.entry12.get())
                    float(self.entry13.get())
                    float(self.entry14.get())
                    float(self.entry15.get())
                    float(self.entry16.get())

                except ValueError:
                    errormsg("MASUKIN ANGKANNA LAH LEK")
                    print("")

                else:
                    button3 = ttk.Button(self, text="Save Result",width=23, command=lambda: saveexp(self))
                    button3.grid(row=17, column=5, columnspan=4, sticky='e')

                    #Stress Level 1
                    sigmaDc1 = float(self.entry3.get())/float(self.entry2.get())

                    n1 = float(self.entry4.get())
                    self.a1 = np.arange(0,n1,5000)

                    muD1 = self.a1/float(self.entry2.get())

                    Z1 = -(1-muD1)/np.sqrt((sigmaDc1**2)+muD1*(float(self.entry3.get())/float(self.entry2.get()))**2)
                    self.pof1 =(1.0 +erf(Z1/np.sqrt(2)))/2

                    #Stress Level 2
                    sigmaDc2 = float(self.entry7.get())/float(self.entry6.get())

                    n2 = float(self.entry8.get())
                    self.a2 = np.arange(0,n2,5000)

                    muD2 = self.a2/float(self.entry6.get())

                    Z2 = -(1-muD2)/np.sqrt((sigmaDc2**2)+muD2*(float(self.entry7.get())/float(self.entry6.get()))**2)
                    self.pof2 =(1.0 +erf(Z2/np.sqrt(2)))/2

                    #Stress Level 3
                    sigmaDc3 = float(self.entry11.get())/float(self.entry10.get())

                    n3 = float(self.entry12.get())
                    self.a3 = np.arange(0,n3,5000)

                    muD3 = self.a3/float(self.entry10.get())

                    Z3 = -(1-muD3)/np.sqrt((sigmaDc3**2)+muD3*(float(self.entry11.get())/float(self.entry10.get()))**2)
                    self.pof3 =(1.0 +erf(Z3/np.sqrt(2)))/2

                    #Stress Level 4
                    sigmaDc4 = float(self.entry15.get())/float(self.entry14.get())

                    n4 = float(self.entry16.get())
                    self.a4 = np.arange(0,n4,5000)

                    muD4 = self.a4/float(self.entry14.get())

                    Z4 = -(1-muD4)/np.sqrt((sigmaDc4**2)+muD4*(float(self.entry15.get())/float(self.entry14.get()))**2)
                    self.pof4 =(1.0 +erf(Z4/np.sqrt(2)))/2

                    #plot
                    style.use("dark_background")

                    f1 = plt.figure(figsize=(10,7))
                    plt.plot(self.a1,self.pof1, label=self.entry1.get()+" Mpa", color='#4dffdb', linewidth=1)
                    plt.plot(self.a2,self.pof2, label=self.entry5.get()+" Mpa", color='#ffff00', linewidth=1)
                    plt.plot(self.a3,self.pof3, label=self.entry9.get()+" Mpa", color='#00ff00', linewidth=1)
                    plt.plot(self.a4,self.pof4, label=self.entry13.get()+" Mpa", color='#ff0000', linewidth=1)

                    plt.axis([0,n3+10000,0,1.01])

                    plt.xlabel("Number of Cycles")
                    plt.ylabel("Probability of Failure")

                    ax = plt.subplot(111)

                    box = ax.get_position()
                    ax.set_position([box.x0, box.y0 + box.height * -0.005,box.width, box.height * 0.95])
                    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),fancybox=True, shadow=True, ncol=5)
                    plt.show()


            elif float(self.entry0.get()) == 5:
                try:
                    float(self.entry1.get())
                    float(self.entry2.get())
                    float(self.entry3.get())
                    float(self.entry4.get())
                    float(self.entry5.get())
                    float(self.entry6.get())
                    float(self.entry7.get())
                    float(self.entry8.get())
                    float(self.entry9.get())
                    float(self.entry10.get())
                    float(self.entry11.get())
                    float(self.entry12.get())
                    float(self.entry13.get())
                    float(self.entry14.get())
                    float(self.entry15.get())
                    float(self.entry16.get())
                    float(self.entry17.get())
                    float(self.entry18.get())
                    float(self.entry19.get())
                    float(self.entry20.get())

                except ValueError:
                    errormsg("MASUKIN ANGKANNA LAH LEK")
                    print("")

                else:
                    button3 = ttk.Button(self, text="Save Result",width=23, command=lambda: saveexp(self))
                    button3.grid(row=17, column=5, columnspan=4, sticky='e')

                    #Stress Level 1
                    sigmaDc1 = float(self.entry3.get())/float(self.entry2.get())

                    n1 = float(self.entry4.get())
                    self.a1 = np.arange(0,n1,5000)

                    muD1 = self.a1/float(self.entry2.get())

                    Z1 = -(1-muD1)/np.sqrt((sigmaDc1**2)+muD1*(float(self.entry3.get())/float(self.entry2.get()))**2)
                    self.pof1 =(1.0 +erf(Z1/np.sqrt(2)))/2

                    #Stress Level 2
                    sigmaDc2 = float(self.entry7.get())/float(self.entry6.get())

                    n2 = float(self.entry8.get())
                    self.a2 = np.arange(0,n2,5000)

                    muD2 = self.a2/float(self.entry6.get())

                    Z2 = -(1-muD2)/np.sqrt((sigmaDc2**2)+muD2*(float(self.entry7.get())/float(self.entry6.get()))**2)
                    self.pof2 =(1.0 +erf(Z2/np.sqrt(2)))/2

                    #Stress Level 3
                    sigmaDc3 = float(self.entry11.get())/float(self.entry10.get())

                    n3 = float(self.entry12.get())
                    self.a3 = np.arange(0,n3,5000)

                    muD3 = self.a3/float(self.entry10.get())

                    Z3 = -(1-muD3)/np.sqrt((sigmaDc3**2)+muD3*(float(self.entry11.get())/float(self.entry10.get()))**2)
                    self.pof3 =(1.0 +erf(Z3/np.sqrt(2)))/2

                    #Stress Level 4
                    sigmaDc4 = float(self.entry15.get())/float(self.entry14.get())

                    n4 = float(self.entry16.get())
                    self.a4 = np.arange(0,n4,5000)

                    muD4 = self.a4/float(self.entry14.get())

                    Z4 = -(1-muD4)/np.sqrt((sigmaDc4**2)+muD4*(float(self.entry15.get())/float(self.entry14.get()))**2)
                    self.pof4 =(1.0 +erf(Z4/np.sqrt(2)))/2

                    #Stress Level 5
                    sigmaDc5 = float(self.entry19.get())/float(self.entry18.get())

                    n5 = float(self.entry20.get())
                    self.a5 = np.arange(0,n5,5000)

                    muD5 = self.a5/float(self.entry18.get())

                    Z5 = -(1-muD5)/np.sqrt((sigmaDc5**2)+muD5*(float(self.entry19.get())/float(self.entry18.get()))**2)
                    self.pof5 =(1.0 +erf(Z5/np.sqrt(2)))/2


                    #plot
                    style.use("dark_background")

                    f1 = plt.figure(figsize=(10,7))
                    plt.plot(self.a1,self.pof1, label=self.entry1.get()+" Mpa", color='#4dffdb', linewidth=1)
                    plt.plot(self.a2,self.pof2, label=self.entry5.get()+" Mpa", color='#ffff00', linewidth=1)
                    plt.plot(self.a3,self.pof3, label=self.entry9.get()+" Mpa", color='#00ff00', linewidth=1)
                    plt.plot(self.a4,self.pof4, label=self.entry13.get()+" Mpa", color='#ff0000', linewidth=1)
                    plt.plot(self.a5,self.pof5, label=self.entry17.get()+" Mpa", color='#805500', linewidth=1)

                    plt.axis([0,n3+10000,0,1.01])

                    plt.xlabel("Number of Cycles")
                    plt.ylabel("Probability of Failure")

                    ax = plt.subplot(111)

                    box = ax.get_position()
                    ax.set_position([box.x0, box.y0 + box.height * -0.005,box.width, box.height * 0.95])
                    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),fancybox=True, shadow=True, ncol=5)
                    plt.show()

############################################################################################################################
def saveas(self):
    """get a filename and save the text in the editor widget"""
    # default extension is optional, here will add .txt if missing
    fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    text2save = str("Maximum Stress: ") + str(self.entry1.get()) +str(" Mpa")
    fout.write(text2save)
    fout.close()

class Empirical(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelm2 = ttk.Label(self, text="METHOD 2", font=LARGE_FONT)
        labelm2.grid(row=2, column=1, sticky='w')

        homebutton=ttk.Button(self, text="Homepage", command=lambda: controller.show_frame(StartPage))
        homebutton.grid(row=1, column=1,padx=10, sticky='w')

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=3, columnspan=4, sticky="EW")
        ttk.Separator(self, orient=tk.VERTICAL).grid(row=1, rowspan=12, column=4, sticky="NS")

        labelload = ttk.Label(self, text=" Loading ", font=MEDIUM_FONT_BOLD)
        labelload.grid(row=3, column=1)

        label1 = ttk.Label(self, text="Maximum Stress (S max): ", font=SMALL_FONT)
        label1.grid(row=4, column=1,pady=5, sticky="w")

        labelmpa1 = ttk.Label(self, text="Mpa", font=SMALL_FONT)
        labelmpa1.grid(row=4, column=3, sticky="w")

        self.entry1 = ttk.Entry(self, width=15)
        self.entry1.grid(row=4, column=2)

        label2 = ttk.Label(self, text="Minimum Stress (S min): ", font=SMALL_FONT)
        label2.grid(row=5, column=1, sticky="w")

        labelmpa2 = ttk.Label(self, text="Mpa", font=SMALL_FONT)
        labelmpa2.grid(row=5, column=3, sticky="w")

        self.entry2 = ttk.Entry(self, width=15)
        self.entry2.grid(row=5, column=2)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=6, columnspan=4, sticky="EW")

        labelmat = ttk.Label(self, text=" Material Properties ", font=MEDIUM_FONT_BOLD)
        labelmat.grid(row=6, column=1)

        label1 = ttk.Label(self, text="Ultimate Strength (Su): ", font=SMALL_FONT)
        label1.grid(row=8, column=1, sticky="w")

        self.entrySu = ttk.Entry(self, width=13)
        self.entrySu.grid(row=8, column=2)

        self.entrysdsu = ttk.Entry(self, width=13)
        self.entrysdsu.grid(row=8, column=3)

        label2 = ttk.Label(self, text="Fatigue Strength Fraction (f): ", font=SMALL_FONT)
        label2.grid(row=10, column=1,pady=5, sticky="w")

        self.entry4 = ttk.Entry(self, width=13)
        self.entry4.grid(row=10, column=2)

        labelSe = ttk.Label(self, text="Fatigue Limit (Se): ", font=SMALL_FONT)
        labelSe.grid(row=9, column=1, sticky="w")

        labelmpaSe = ttk.Label(self, text="Std Dev", font=MEDIUM_FONT_BOLD)
        labelmpaSe.grid(row=7, column=3)

        self.entrySe = ttk.Entry(self, width=13)
        self.entrySe.grid(row=9, column=2, pady=3)

        self.entrysdse = ttk.Entry(self, width=13)
        self.entrysdse.grid(row=9, column=3)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=1,column=5, columnspan=4, sticky="EW")

        labelmod = ttk.Label(self, text=" Modifying Factors ", font=MEDIUM_FONT_BOLD)
        labelmod.grid(row=1, column=5, pady=5)

        label5 = ttk.Label(self, text="Loading (C load): ", font=SMALL_FONT)
        label5.grid(row=2, column=5,pady=5, sticky="w")

        self.entry5 = ttk.Entry(self, width=15)
        self.entry5.grid(row=2, column=6)
        self.entry5.insert(0, 1)

        label6 = ttk.Label(self, text="Diameter (C size): ", font=SMALL_FONT)
        label6.grid(row=3, column=5, pady=5, sticky="w")

        labelmm = ttk.Label(self, text=" mm", font=SMALL_FONT)
        labelmm.grid(row=3, column=7, sticky="w")

        self.entry6 = ttk.Entry(self, width=15)
        self.entry6.grid(row=3, column=6)
        self.entry6.insert(0, 1)

        label7 = ttk.Label(self, text="Surface finish (C surf): ", font=SMALL_FONT)
        label7.grid(row=4, column=5, sticky="w")

        self.entry7 = ttk.Entry(self, width=15)
        self.entry7.grid(row=4, column=6)
        self.entry7.insert(0, 1)

        label8 = ttk.Label(self, text="Temperature (C temp): ", font=SMALL_FONT)
        label8.grid(row=5, column=5, pady=5, sticky="w")

        labelc = ttk.Label(self, text=" °C")
        labelc.grid(row=5, column=7, sticky="w")

        self.entry8 = ttk.Entry(self, width=15)
        self.entry8.grid(row=5, column=6)
        self.entry8.insert(0, 1)

        label9 = ttk.Label(self, text="Reliability (C rel): ", font=SMALL_FONT)
        label9.grid(row=6, column=5,pady=5, sticky="w")

        self.entry9 = ttk.Entry(self, width=15)
        self.entry9.grid(row=6, column=6)
        self.entry9.insert(0, 1)

        label10 = ttk.Label(self, text="Miscellanous (C misc): ", font=SMALL_FONT)
        label10.grid(row=7, column=5, pady=5, sticky="w")

        self.entry10 = ttk.Entry(self, width=15)
        self.entry10.grid(row=7, column=6)
        self.entry10.insert(0, 1)

        label11 = ttk.Label(self, text="Stress Concentration (Kt): ", font=SMALL_FONT)
        label11.grid(row=8, column=5, pady=5,sticky="w")

        self.entry11 = ttk.Entry(self, width=15)
        self.entry11.grid(row=8, column=6)
        self.entry11.insert(0, 0)

        label12 = ttk.Label(self, text="Notch Factor (q): ", font=SMALL_FONT)
        label12.grid(row=9, column=5, pady=5, sticky="w")

        self.entry12 = ttk.Entry(self, width=15)
        self.entry12.grid(row=9, column=6)
        self.entry12.insert(0, 0)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=12,columnspan=15, sticky="WE")
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=13,columnspan=15, sticky="WE")
        labelnf = ttk.Label(self, text=" Fatigue Life and Damage Calculation ", font=MEDIUM_FONT_BOLD)
        labelnf.grid(row=13,column=2,sticky='w', columnspan=5,pady=10)

        label14 = ttk.Label(self, text="Cycles to Failure (Nf): ", font=SMALL_FONT)
        label14.grid(row=14, column=1, sticky='w')

        self.entrynf = ttk.Entry(self, width=15)
        self.entrynf.grid(row=14, column=2)

        label13 = ttk.Label(self, text="Critical Damage (Dcr): ", font=SMALL_FONT)
        label13.grid(row=15, column=1, sticky='w')

        self.entrysd = ttk.Entry(self, width=15)
        self.entrysd.grid(row=15, column=2)

        label15 = ttk.Label(self, text="Applied Cycles (Nf): ", font=SMALL_FONT)
        label15.grid(row=16, column=1,pady=7, sticky='w')

        self.entryn = ttk.Entry(self, width=15)
        self.entryn.grid(row=16, column=2)

        calculatebutton  = ttk.Button(self, text='Calculate Cycle', command=lambda: self.calculatecycles())
        calculatebutton.grid(row=14, column=3, columnspan=3, sticky='w', pady=5, padx=5)

        plotbutton = ttk.Button(self, text='Plot', command=lambda: self.calculatedamage())
        plotbutton.grid(row=18, column=2,pady=5, sticky='e')

        clearbutton = ttk.Button(self, text="Clear all ", command=lambda: self.clear_text())
        clearbutton.grid(row=18, column=3, sticky='w')

        nextbutton = ttk.Button(self, text="Next", command=lambda: controller.show_frame(Experiment))
        nextbutton.grid(row=20, column=6, sticky='w')


    def clear_text(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entrysdse.delete(0, 'end')
        self.entrysdsu.delete(0, 'end')
        self.entrySe.delete(0, 'end')
        self.entrySu.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entrySe.delete(0, 'end')
        self.entryn.delete(0, 'end')
        self.entrysd.delete(0, 'end')
        self.entrynf.delete(0, 'end')


    def calculatecycles(self):
        try:
            float(self.entry1.get())
            float(self.entry2.get())
            float(self.entrySu.get())
            float(self.entry4.get())
            float(self.entry5.get())
            float(self.entry6.get())
            float(self.entry7.get())
            float(self.entry8.get())
            float(self.entry9.get())
            float(self.entry10.get())
            float(self.entry11.get())
            float(self.entry12.get())

        except ValueError:
            errormsg("MASUKIN ANGKANNA LAH LEK")
            print("")

        else:
            smax = float(self.entry1.get())
            smin = float(self.entry2.get())

            sa = (smax - smin)/2
            sm = (smax + smin)/2

            su = float(self.entrySu.get())
            f = float(self.entry4.get())

            snf = sa/(1-(sm/su))

            cload = float(self.entry5.get())

            size = float(self.entry6.get())
            if size <= 8:
                csize = 1
            elif size > 250:
                csize = 0.6
            else:
                csize = 1.189*(size**-0.097)

            csurf = float(self.entry7.get())

            temp = float(self.entry8.get())
            if temp <= 450:
                ctemp = 1
            elif temp > 550:
                ctemp = 0.1
            else:
                ctemp = 1-0.0058*(temp-450)

            crel = float(self.entry9.get())

            cmisc = float(self.entry10.get())

            Kt = float(self.entry11.get())

            q = float(self.entry12.get())

            Kf = q*(Kt-1)+1

            se = float(self.entrySe.get())

            if su < 1400:
                se_ =  (se*cload*csize*csurf*ctemp*crel*cmisc)/Kf
            else:
                se_ = 700

            a = ((f*su)**2)/se_
            b = (-1/4.35)*math.log10(f*su/se_)

            nf = (snf/a)**(1/b)
            self.entrynf.delete(0, 'end')
            self.entrynf.insert(0, int(nf))


    def calculatedamage(self):
        try:
            float(self.entryn.get())
            float(self.entrynf.get())
            float(self.entrysd.get())

        except ValueError:
            errormsg("MASUKIN ANGKANNA LAH LEK")
            print("")

        else:
            n =  float(self.entryn.get())
            Nf = float(self.entrynf.get())
            sd = float(self.entrynf.get())/10
            sa = (float(self.entry1.get()) - float(self.entry2.get()))/2

            sdDc = sd/Nf

            self.a1 = np.arange(0.,n,5000)

            meanD = self.a1/Nf

            Z = -(1-meanD)/np.sqrt((sdDc**2)+meanD*((sd/Nf)**2))
            self.pof1 =(1.0 +erf(Z/np.sqrt(2)))/2

            style.use("dark_background")

            f1 = plt.figure(figsize=(10,7))
            plt.plot(self.a1,self.pof1, label= str(sa)+" Mpa", color='#4dffdb', linewidth=1)

            plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

            plt.xlabel("Number of Cycles")
            plt.ylabel("Probability of Failure")

            ax = plt.subplot(111)

            box = ax.get_position()
            ax.set_position([box.x0, box.y0 + box.height * -0.005,box.width, box.height * 0.95])
            ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),fancybox=True, shadow=True, ncol=5)

            plt.show()





############################################################################################################################
class Deterministic(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelm2 = ttk.Label(self, text="METHOD 2", font=LARGE_FONT)
        labelm2.grid(row=2, column=1, sticky='w')

        homebutton=ttk.Button(self, text="Homepage", command=lambda: controller.show_frame(StartPage))
        homebutton.grid(row=1, column=1,padx=10, sticky='w')

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=3, columnspan=4, sticky="EW")
        ttk.Separator(self, orient=tk.VERTICAL).grid(row=1, rowspan=12, column=4, sticky="NS")

        labelload = ttk.Label(self, text=" Loading ", font=MEDIUM_FONT_BOLD)
        labelload.grid(row=3, column=1)

        label1 = ttk.Label(self, text="Maximum Stress (S max): ", font=SMALL_FONT)
        label1.grid(row=4, column=1,pady=5, sticky="w")

        labelmpa1 = ttk.Label(self, text="Mpa", font=SMALL_FONT)
        labelmpa1.grid(row=4, column=3, sticky="w")

        self.entry1 = ttk.Entry(self, width=15)
        self.entry1.grid(row=4, column=2)

        label2 = ttk.Label(self, text="Minimum Stress (S min): ", font=SMALL_FONT)
        label2.grid(row=5, column=1, sticky="w")

        labelmpa2 = ttk.Label(self, text="Mpa", font=SMALL_FONT)
        labelmpa2.grid(row=5, column=3, sticky="w")

        self.entry2 = ttk.Entry(self, width=15)
        self.entry2.grid(row=5, column=2)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=7, columnspan=4, sticky="EW")

        labelmat = ttk.Label(self, text=" Material Properties ", font=MEDIUM_FONT_BOLD)
        labelmat.grid(row=7, column=1)

        label1 = ttk.Label(self, text="Ultimate Strength (Su): ", font=SMALL_FONT)
        label1.grid(row=8, column=1, sticky="w")

        labelmpa3 = ttk.Label(self, text="Mpa", font=SMALL_FONT)
        labelmpa3.grid(row=8, column=3, sticky="w")

        self.entry3 = ttk.Entry(self, width=15)
        self.entry3.grid(row=8, column=2)

        label2 = ttk.Label(self, text="Fatigue Strength Fraction (f): ", font=SMALL_FONT)
        label2.grid(row=9, column=1,pady=5, sticky="w")

        self.entry4 = ttk.Entry(self, width=15)
        self.entry4.grid(row=9, column=2)

        labelSe = ttk.Label(self, text="Fatigue Limit (Se): ", font=SMALL_FONT)
        labelSe.grid(row=10, column=1, sticky="w")

        labelmpaSe = ttk.Label(self, text="Mpa", font=SMALL_FONT)
        labelmpaSe.grid(row=10, column=3, sticky="w")

        self.entrySe = ttk.Entry(self, width=15)
        self.entrySe.grid(row=10, column=2, pady=3)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=1,column=5, columnspan=4, sticky="EW")

        labelmod = ttk.Label(self, text=" Modifying Factors ", font=MEDIUM_FONT_BOLD)
        labelmod.grid(row=1, column=5, pady=5)

        label5 = ttk.Label(self, text="Loading (C load): ", font=SMALL_FONT)
        label5.grid(row=2, column=5,pady=5, sticky="w")

        self.entry5 = ttk.Entry(self, width=15)
        self.entry5.grid(row=2, column=6)
        self.entry5.insert(0, 1)

        label6 = ttk.Label(self, text="Diameter (C size): ", font=SMALL_FONT)
        label6.grid(row=3, column=5, pady=5, sticky="w")

        labelmm = ttk.Label(self, text=" mm", font=SMALL_FONT)
        labelmm.grid(row=3, column=7, sticky="w")

        self.entry6 = ttk.Entry(self, width=15)
        self.entry6.grid(row=3, column=6)
        self.entry6.insert(0, 1)

        label7 = ttk.Label(self, text="Surface finish (C surf): ", font=SMALL_FONT)
        label7.grid(row=4, column=5, sticky="w")

        self.entry7 = ttk.Entry(self, width=15)
        self.entry7.grid(row=4, column=6)
        self.entry7.insert(0, 1)

        label8 = ttk.Label(self, text="Temperature (C temp): ", font=SMALL_FONT)
        label8.grid(row=5, column=5, pady=5, sticky="w")

        labelc = ttk.Label(self, text=" °C")
        labelc.grid(row=5, column=7, sticky="w")

        self.entry8 = ttk.Entry(self, width=15)
        self.entry8.grid(row=5, column=6)
        self.entry8.insert(0, 1)

        label9 = ttk.Label(self, text="Reliability (C rel): ", font=SMALL_FONT)
        label9.grid(row=6, column=5,pady=5, sticky="w")

        self.entry9 = ttk.Entry(self, width=15)
        self.entry9.grid(row=6, column=6)
        self.entry9.insert(0, 1)

        label10 = ttk.Label(self, text="Miscellanous (C misc): ", font=SMALL_FONT)
        label10.grid(row=7, column=5, pady=5, sticky="w")

        self.entry10 = ttk.Entry(self, width=15)
        self.entry10.grid(row=7, column=6)
        self.entry10.insert(0, 1)

        label11 = ttk.Label(self, text="Stress Concentration (Kt): ", font=SMALL_FONT)
        label11.grid(row=8, column=5, pady=5,sticky="w")

        self.entry11 = ttk.Entry(self, width=15)
        self.entry11.grid(row=8, column=6)
        self.entry11.insert(0, 0)

        label12 = ttk.Label(self, text="Notch Factor (q): ", font=SMALL_FONT)
        label12.grid(row=9, column=5, pady=5, sticky="w")

        self.entry12 = ttk.Entry(self, width=15)
        self.entry12.grid(row=9, column=6)
        self.entry12.insert(0, 0)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=12,columnspan=15, sticky="WE")
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=13,columnspan=15, sticky="WE")
        labelnf = ttk.Label(self, text=" Fatigue Life and Damage Calculation ", font=MEDIUM_FONT_BOLD)
        labelnf.grid(row=13,column=2,sticky='w', columnspan=5,pady=10)

        label14 = ttk.Label(self, text="Cycles to Failure (Nf): ", font=SMALL_FONT)
        label14.grid(row=14, column=1, sticky='w')

        label13 = ttk.Label(self, text="Applied Cycles (n): ", font=SMALL_FONT)
        label13.grid(row=15, column=1, sticky='w')

        labelcycle = ttk.Label(self, text="Cycles", font=SMALL_FONT)
        labelcycle.grid(row=15, column=3, sticky='w', padx=5)

        self.entryn = ttk.Entry(self, width=15)
        self.entryn.grid(row=15, column=2)

        label15 = ttk.Label(self, text="Damage (D): ", font=SMALL_FONT)
        label15.grid(row=16, column=1,pady=7, sticky='w')

        self.entrynf = ttk.Entry(self, width=15)
        self.entrynf.grid(row=14, column=2)

        self.entrydam = ttk.Entry(self, width=15)
        self.entrydam.grid(row=16, column=2)

        calculatebutton  = ttk.Button(self, text='Calculate Cycle', command=lambda: self.calculatecycles())
        calculatebutton.grid(row=14, column=3, columnspan=3, sticky='w', pady=5, padx=5)

        calculatebutton = ttk.Button(self, text='Calculate Damage', command=lambda: self.calculatedamage())
        calculatebutton.grid(row=16, column=3, columnspan=3, sticky='w', pady=5, padx=5)

        plotbutton = ttk.Button(self, text='Save As', command=lambda: saveas(self))
        plotbutton.grid(row=18, column=2,pady=5, sticky='e')

        clearbutton = ttk.Button(self, text="Clear all ", command=lambda: self.clear_text())
        clearbutton.grid(row=18, column=3, sticky='w')

        nextbutton = ttk.Button(self, text="Next", command=lambda: controller.show_frame(Experiment))
        nextbutton.grid(row=20, column=6, sticky='w')


    def clear_text(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entrySe.delete(0, 'end')
        self.entryn.delete(0, 'end')
        self.entrydam.delete(0, 'end')
        self.entrynf.delete(0, 'end')


    def calculatecycles(self):
        try:
            float(self.entry1.get())
            float(self.entry2.get())
            float(self.entry3.get())
            float(self.entry4.get())
            float(self.entry5.get())
            float(self.entry6.get())
            float(self.entry7.get())
            float(self.entry8.get())
            float(self.entry9.get())
            float(self.entry10.get())
            float(self.entry11.get())
            float(self.entry12.get())

        except ValueError:
            errormsg("MASUKIN ANGKANNA LAH LEK")
            print("")

        else:
            smax = float(self.entry1.get())
            smin = float(self.entry2.get())

            sa = (smax - smin)/2
            sm = (smax + smin)/2

            su = float(self.entry3.get())
            f = float(self.entry4.get())

            snf = sa/(1-(sm/su))

            cload = float(self.entry5.get())

            size = float(self.entry6.get())
            if size <= 8:
                csize = 1
            elif size > 250:
                csize = 0.6
            else:
                csize = 1.189*(size**-0.097)

            csurf = float(self.entry7.get())

            temp = float(self.entry8.get())
            if temp <= 450:
                ctemp = 1
            elif temp > 550:
                ctemp = 0.1
            else:
                ctemp = 1-0.0058*(temp-450)

            crel = float(self.entry9.get())

            cmisc = float(self.entry10.get())

            Kt = float(self.entry11.get())

            q = float(self.entry12.get())

            Kf = q*(Kt-1)+1

            se = float(self.entrySe.get())

            if su < 1400:
                se_ =  (se*cload*csize*csurf*ctemp*crel*cmisc)/Kf
            else:
                se_ = 700

            a = ((f*su)**2)/se_
            b = (-1/4.35)*math.log10(f*su/se_)

            nf = (snf/a)**(1/b)
            self.entrynf.delete(0, 'end')
            self.entrynf.insert(0, int(nf))

            x1 = ([1,1000000, 1000000000])
            y1 = ([su, se, se_])
            plt.semilogx(x1,y1, color='r', linewidth=5)

            x2 =([1, nf])
            y2 = ([snf, snf])
            markers_on = [1,2,3]
            plt.semilogx(x2, y2, color='g',marker='s',markersize=12,  linewidth=5)

            plt.axis([0,1000000000,0,1000])
            'plt.show()'


    def calculatedamage(self):
        try:
            float(self.entryn.get())
            float(self.entrynf.get())

        except ValueError:
            errormsg("MASUKIN ANGKANNA LAH LEK")
            print("")

        else:
            n =  float(self.entryn.get())
            nf = float(self.entrynf.get())
            D = n/nf
            self.entrydam.delete(0, 'end')
            self.entrydam.insert(0, "%.3f" % D)






############################################################################################################################

app = TesisApp()
app.geometry("640x480")

app.mainloop()
