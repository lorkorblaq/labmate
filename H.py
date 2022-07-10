
from tkinter import *
from tkinter import filedialog

import PyPDF2

#Create an instance of tkinter frame
win= Tk()
#Set the Geometry
win.geometry("750x450")
#Create a Text Box
text= Text(win,width= 80,height=30)
text.pack(pady=20)
#Define a function to clear the text
def clear_text():
   text.delete(1.0, END)
#Define a function to open the pdf file
def open_pdf():
   file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      #Open the PDF File
      pdf_file= PyPDF2.PdfFileReader(file)
      #Select a Page to read
      page= pdf_file.getPage(0)
      #Get the content of the Page
      content=page.extractText()
      #Add the content to TextBox
      text.insert(1.0,content)

#Define function to Quit the window
def quit_app():
   win.destroy()
#Create a Menu
my_menu= Menu(win)
win.config(menu=my_menu)
#Add dropdown to the Menus
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu= file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Clear",command=clear_text)
file_menu.add_command(label="Quit",command=quit_app)
win.mainloop()

from tkinter import *

# Importing tkPDFViewer to place pdf file in gui.
# In tkPDFViewer library there is
# an tkPDFViewer module. That I have imported as pdf
from tkPDFViewer import tkPDFViewer as pdf

# Initializing tk
root = Tk()

# Set the width and height of our root window.
root.geometry("550x750")

# creating object of ShowPdf from tkPDFViewer.
v1 = pdf.ShowPdf()

# Adding pdf location and width and height.
v2 = v1.pdf_view(root,
                 pdf_location=r"location",
                 width=50, height=100)

# Placing Pdf in my gui.
v2.pack()
root.mainloop()