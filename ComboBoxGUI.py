import tkinter as tk
from tkinter.ttk import *
def submit():
    selectedOption = combo.get()
    lblResult["text"] = selectedOption
window = tk.Tk()
window.title("Dropdown list example")
combo = Combobox(window)
combo['values'] = ("IN", "CA", "MA")
btnSubmit = tk.Button(window, text="Submit", command=submit)
lblResult = tk.Label(window)
combo.grid(column=0,row=0)
btnSubmit.grid(column=1,row=0)
lblResult.grid(column=2,row=0)
window.mainloop()