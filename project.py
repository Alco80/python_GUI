import tkinter as tk

root = tk.Tk()
root.title("My App")

lbl = tk.Label(root, text="This Label")
lbl.grid()

btn = tk.Button(root, text="Press Me!")
btn.grid()

root.mainloop()