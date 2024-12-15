import tkinter as tk

root = tk.Tk()
root.title("My App")

lbl = tk.Label(root, text="This Label")
lbl.grid(row=0, column=0)

btn = tk.Button(root, text="Press Me!")
btn.grid(row=0, column=0)

root.mainloop()