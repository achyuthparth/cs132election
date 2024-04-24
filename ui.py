import geopandas as gpd
import matplotlib.pyplot as plt
import tkinter
from new_shape_generator import generator
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

option = {
    "Alabama": "al",
    "Alaska": "ak",
    "Arizona": "az",
    "Arkansas": "ar",
    "California": "ca",
    "Colorado": "co",
    "Connecticut": "ct",
    "Delaware": "de",
    "Florida": "fl",
    "Georgia": "ga",
    "Hawaii": "hi",
    "Idaho": "id",
    "Illinois": "il",
    "Indiana": "in",
    "Iowa": "ia",
    "Kansas": "ks",
    "Kentucky": "ky",
    "Louisiana": "la",
    "Maine": "me",
    "Maryland": "md",
    "Massachusetts": "ma",
    "Michigan": "mi",
    "Minnesota": "mn",
    "Mississippi": "ms",
    "Missouri": "mo",
    "Montana": "mt",
    "Nebraska": "ne",
    "Nevada": "nv",
    "New Hampshire": "nh",
    "New Jersey": "nj",
    "New Mexico": "nm",
    "New York": "ny",
    "North Carolina": "nc",
    "North Dakota": "nd",
    "Ohio": "oh",
    "Oklahoma": "ok",
    "Oregon": "or",
    "Pennsylvania": "pa",
    "Rhode Island": "ri",
    "South Carolina": "sc",
    "South Dakota": "sd",
    "Tennessee": "tn",
    "Texas": "tx",
    "Utah": "ut",
    "Vermont": "vt",
    "Virginia": "va",
    "Washington": "wa",
    "West Virginia": "wv",
    "Wisconsin": "wi",
    "Wyoming": "wy"
}

def drawMap(state_shape):
    for widget in frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(5, 4))
    state_shape.plot(ax=ax, color=state_shape['max_color'], edgecolor = "black", linewidth = 0.25)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def updateState():
    zipfile = r"C:\Users\achyu\git\cs132election\state_zip" + "/" + str(option[dropdown.get()]) + "_2020.zip"
    #us = gpd.read_file(zipfile)
    state_shape = generator(zipfile)
    drawMap(state_shape)

root = tkinter.Tk()
root.wm_title("Political Heatmap")
frame = ttk.Frame(root)
frame.pack(fill=tkinter.BOTH, expand=True)

dropdown = tkinter.StringVar()
dropdown.set("Alabama")
drop = tkinter.OptionMenu(root, dropdown, *option.keys())
drop.pack(side=tkinter.LEFT)

update = tkinter.Button(root,text="Update",command=updateState).pack(side=tkinter.LEFT)

def _quit():
    root.quit()
    root.destroy()

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.RIGHT,padx=5)

updateState()

tkinter.mainloop()