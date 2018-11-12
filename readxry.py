"""
@Title:         Readxry
@Description:   Reads .xry data from Leybold X-ray apparatus and plots the data.
@Author:        R.D. Beerman
@Date:          14/09/2018
@License:       GNU General Public License v3.0
"""
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Canvas(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.config_vars()
        self.config_ui()
        self.config_background()
        self.config_buttons()
        self.canvas.bind("<Configure>", self.resize)

    def config_ui(self):
        self.width = 300
        self.height = 600
        self.master.title("FreeDar")
        self.master.resizable(True, True)
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=1)

    def config_background(self):
        self.title = self.canvas.create_text(10, 10, text=' Readxry v1.0 by R.D. Beerman', anchor=tk.NW)
        self.beta = self.canvas.create_text(10, 80, text='Min angle:', anchor=tk.NW)
        self.beta = self.canvas.create_text(10, 100, text='Max angle:', anchor=tk.NW)
        self.beta = self.canvas.create_text(10, 120, text='Angle step:', anchor=tk.NW)
        self.beta = self.canvas.create_text(10, 140, text='Time step:', anchor=tk.NW)

        self.beta = self.canvas.create_text(100, 80, text=self.Bmin.get(), anchor=tk.NW, tag='Bmin')
        self.beta = self.canvas.create_text(100, 100, text=self.Bmax.get(), anchor=tk.NW, tag='Bmax')
        self.beta = self.canvas.create_text(100, 120, text=self.Bstep.get(), anchor=tk.NW, tag='Bstep')
        self.beta = self.canvas.create_text(100, 140, text=self.Tstep.get(), anchor=tk.NW, tag='Tstep')

    def config_vars(self):
        self.filename = tk.StringVar()
        self.filename.set("N/A")

        self.Bmin = tk.StringVar()
        self.Bmin.set("-")
        self.Bmax = tk.StringVar()
        self.Bmax.set("-")
        self.Bstep = tk.StringVar()
        self.Bstep.set("-")
        self.Tstep = tk.StringVar()
        self.Tstep.set("-")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()

    def resize(self, event):
        self.w, self.h = event.width, event.height

    def config_buttons(self):
        self.button_lines = tk.Button(self.canvas, text = 'Select file', command=self.fileselector, anchor=tk.NW)
        self.button_lines_window = self.canvas.create_window(10, 30, anchor=tk.NW, window=self.button_lines)

    def fileselector(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = ((".xry files","*.xry"),("all files","*.*")))

        with open(self.filename, 'r') as self.file:
            self.rawdata = self.file.read().splitlines()

        self.Bmin.set(self.rawdata[4][:3])
        self.Bmax.set(self.rawdata[4][4:6])
        self.Bstep.set(self.rawdata[4][9:13])
        self.Tstep.set(self.rawdata[4][7:9])

        self.canvas.delete("Bmax", "Bmin", "Bstep","Tstep")
        self.config_background()

        self.plotdata()

    def plotdata(self):
        self.data_beta = np.arange(float(self.Bmin.get()),float(self.Bmax.get()) + float(self.Bstep.get()),float(self.Bstep.get()))
        self.data_rate = np.array(self.rawdata[18:len(self.rawdata)-11]).astype(float)

        #print(self.data_rate)
        #print(self.data_beta)

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(self.data_beta, self.data_rate)
        plt.xlabel('angle (degrees)')
        plt.ylabel('rate (s^-1)')
        plt.ylim(0)
        plt.xlim(float(self.Bmin.get()), float(self.Bmax.get()))

        #a = anim.FuncAnimation(fig, self.plotdata(), frames=3, repeat=False)
        self.update()
        plt.show(block=False)

root = tk.Tk()
mainWindow = Canvas(root)

while True:
    root.protocol("WM_DELETE_WINDOW", mainWindow.on_closing)
    root.mainloop()