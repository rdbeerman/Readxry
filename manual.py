"""
@Title:         Read rxy manual
@Description:   For manually reading and plotting multiple .xry files in the same plot.
@Author:        R.D. Beerman
@Date:          17/09/2018
@License:
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


filenames = ["meting_Nacl_5s.xry", "meting_LiF_5s.xry", "meting_KBr_5s.xry"]				#change filenames
labelnames = ["NaCl", "LiF", "KBr"]															#change label for each file (matplotlib)
d = [564, 402.7, 659.7]																		#for transfering data_beta to data_nlabda with known values for d

i = 0

while i < len(filenames):
    with open(filenames[i], 'r') as file:
        rawdata = file.read().splitlines()

    Bmin = rawdata[4][:3]
    Bmax = rawdata[4][4:6]
    Bstep = rawdata[4][9:13]
    Tstep = rawdata[4][7:9]

    data_beta = np.arange(float(Bmin), float(Bmax) + float(Bstep),
                                       float(Bstep))
    data_nlabda = d[i] * np.sin(np.deg2rad(data_beta))
    data_rate = np.array(rawdata[18:len(rawdata) - 11]).astype(float)

    plt.plot(data_blabda, data_rate, label=labelnames[i])
    plt.xlabel('nλ (pm)')
    plt.ylabel('rate (s^-1)')
    plt.ylim(0)
    #plt.xlim(float(Bmin), float(Bmax))
    i = i + 1

plt.legend()
plt.show()