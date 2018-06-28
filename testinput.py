# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.withdraw()

# file_path = filedialog.askopenfilename()

import textract
#mport docx2txt
import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()

t = tkFileDialog.askopenfilename()
text = textract.process(t)
#text2 = docx2txt.process(t)
print(text)
