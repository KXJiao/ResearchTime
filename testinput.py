import textract
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

t = filedialog.askopenfilename()
text = textract.process(t)
print(text)

text.split()