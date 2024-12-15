import tkinter as tk

root = tk.Tk()
root.title("My App")

def on_click():
    lbl.config(text="Button click")

lbl = tk.Label(root, text="This Label")
lbl.grid(row=0, column=0)

print(lbl.config().keys())

btn = tk.Button(root, text="Press Me!", command=on_click)
btn.grid(row=0, column=1)

root.mainloop()