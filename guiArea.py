import tkinter as tk
from tkinter import messagebox

def calcArea(w,h):
    return w*h

def clickArea():
    try:
        areaCalc["text"] = str(calcArea(int(entryWidth.get()),int(entryheight.get())))
    except ValueError:
        messagebox.showerror(message="Error: only numbers are allowed")

root = tk.Tk()
root.title("Rectangle Area")
root.geometry("300x200")
widthlab = tk.Label(root,text="Width")
entryWidth = tk.Entry()
heightlab = tk.Label(root,text="height")
entryheight = tk.Entry()
areaLab = tk.Label(root,text="area")
areaCalc = tk.Label(root,text="0")
calcButton= tk.Button(root,text="calculate",command=clickArea)

widthlab.grid(row=0,column=0)
entryWidth.grid(row=0,column=1)
heightlab.grid(row=1,column=0)
entryheight.grid(row=1,column=1)
areaLab.grid(row=2,column=0)
areaCalc.grid(row=2,column=1)
calcButton.grid(row=3,column=0,columnspan=2)
root.mainloop()