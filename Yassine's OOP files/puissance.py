import tkinter as tk
from tkinter import ttk

def convert():
    puissance2 = entry_int.get()
    nombre_output = puissance2 ** 2
    output_var.set(nombre_output)

window = tk.Tk()
window.geometry("500x250")

title = ttk.Label(master=window, text="puissance2", font="calibri 30 bold")
title.pack()

frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=frame, textvariable=entry_int)
button = ttk.Button(master=frame, text="convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
frame.pack(pady=5)

output_var = tk.IntVar()
output_label = ttk.Label(master=window, text="output", font="bold 22", textvariable=output_var)
output_label.pack(pady=10)

window.mainloop()