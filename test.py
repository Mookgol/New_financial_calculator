import tkinter as tk
from tkinter import simpledialog

def process():
    btn_process.config(state="disabled")  # Disable button during processing
    username = simpledialog.askstring("Prompt", "Enter username:")
    # Perform your processing here...
    btn_process.config(state="normal")  # Enable button after processing

root = tk.Tk()
root.title("Prevent Multiple Pop-ups")

btn_process = tk.Button(root, text="Process", command=process)
btn_process.pack(padx=20, pady=10)

root.mainloop()
