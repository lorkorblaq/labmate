from tkinter import *

import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

main = Tk()
main.title('Labmate')
main.geometry('1366x760')
main.iconbitmap('')
main.config(highlightthickness=2, bg='#4f82ac')


# bg= PhotoImage(file='lovelight.png')

def show_frame1():
    hide_frames()
    frame1.pack(fill='both', expand=1)


def show_frame2():
    hide_frames()
    frame2.pack(fill='both', expand=1)


def show_frame3():
    hide_frames()
    frame3.pack(fill='both', expand=1)


def show_frame4():
    hide_frames()
    frame4.pack(fill='both', expand=1)


def show_frame5():
    hide_frames()
    frame5.pack(fill='both', expand=1)


def show_frame6():
    frame.tkraise()


def show_frame7():
    wrapper1.tkraise()

def hide_frames():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()


frame1 = Frame(main, width=600, height=500, bg='blue')

frame2 = Frame(main, width=600, height=500, bg='green')

frame3 = Frame(main, width=600, height=500, bg='yellow')

frame4 = Frame(main, width=600, height=500, bg='black')

frame5 = Frame(main, width=600, height=500, bg='white')

'''
def clear():
    search_entry.delete(0,END)
    result_text.delete(0,END)
def search():
    data = wiki.page(search_entry.get())
    
    clear()
    result_text.insert(0.0, data.content)
'''

'''
imageL= Label(main, image=bg)
imageL.pack()
'''
# canvas
'''

canvas = Canvas(main, width = 1360, height= 900, bd=0,highlightthickness=0)
canvas.pack(fill='both', expand='True')
canvas.create_image(0,0, image=bg, anchor='nw')

'''


# frame1


def show_frame():
    pass


def hide_frame():
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    frame4.destroy()
    frame5.destroy()


my_menu = Menu(main)
main.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New...', command=show_frame)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=show_frame)

page_menu = Menu(my_menu)
my_menu.add_cascade(label='Pages', menu=page_menu)
page_menu.add_command(label='QC...', command=show_frame1)
page_menu.add_command(label='Reagent Log', command=show_frame2)
page_menu.add_command(label='Instrument', command=show_frame3)
page_menu.add_command(label='Search', command=show_frame4)
page_menu.add_command(label='LIS', command=show_frame5)
page_menu.add_command(label='Mail', command=show_frame6)
page_menu.add_command(label='Calculator', command=show_frame7)

'''
#frames

#frame1
wrapper1= LabelFrame(main,text='Data screen')
wrapper1.pack(fill='both', expand='yes',padx=0, ipady=0, pady=0)

#treeview
trv= ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6),show='headings')
trv.pack(fill='both',expand='yes', pady=0, ipady=0)

#headings
trv.heading(1, text="Date")
trv.heading(2, text="User")
trv.heading(3, text="Put in-use")
trv.heading(4, text="QC Management")
trv.heading(5, text="Machine")

#scrollbar
scrollbary=Scrollbar(wrapper1, orient=VERTICAL)
scrollbary.place(relx=0.9848, rely=0.099999, width = 20, height= 215)
scrollbary.configure(command=trv.yview())
trv.configure(yscrollcommand=scrollbary.set)


#frame2
wrapper2= LabelFrame(main, text='Diary Diary')
wrapper2.pack(fill='both', expand='yes', ipady=16)

#entries & labels
#date entry
def my_upd():
    pass
sel=tk.StringVar()

cal=DateEntry(wrapper2,selectmode='day', date_pattern="dd-mm-y", extvariable=sel).place(relx=0.3, rely=0.8)

#combobox
users = (
        Fortune Nwosu,
        Amadi Uche,
        Kenneth Michelle,
        Osaigbovo Ebehrimen,
        Maryann, 
        Eziebe CLaribel,
        Oloko Olorunfemi,
        Ndukwe Ruth
        Enebeli Gerald
        Trainee
        )

 
combx= combobox(wrapper2, values=users)
combx.pack()

Label(wrapper2, text='QC Management').place(relx=0.01, rely=0.1)
textentry1 = tk.Text(wrapper2, width=60, height=1)
textentry1.pack( padx=5, pady=1, ipady= 30, side= LEFT, )

Label(wrapper2, text='Calibrations').place(relx=0.4, rely=0.1)
textentry2 = tk.Text(wrapper2, width=40, height=1)
textentry2.pack(padx=0, pady=1, ipady= 30, side= LEFT)

Label(wrapper2, text='Instrument Flags').place(relx=0.63, rely=0.1)
textentry3 = tk.Text(wrapper2, width=30, height=1)
textentry3.pack(padx=5, pady=1, ipady= 30, side= LEFT)

Label(wrapper2, text='To Do list').place(relx=0.8, rely=0.1)
textentry4 = tk.Entry(wrapper2, width=33)
textentry4.place(relx=0.8, rely=0.28)





#frame3
wrapper3= LabelFrame(main, text='Reagent log')
wrapper3.pack(fill='both', expand='yes',padx=5, ipady=30)

#entry&label
Label(wrapper3, text='Item:').grid(row=1, column=0)
item_inuse = Entry(wrapper3).grid(row=1, column=1)

Label(wrapper3, text='Quantity:').grid(row=1, column=2)
Quantity = Entry(wrapper3).grid(row=1, column=3)

Label(wrapper3, text='Lot No.:').grid(row=1, column=4)
lot_no = Entry(wrapper3).grid(row=1, column=5)

Label(wrapper3, text='Expiration:').grid(row=1, column=6, pady=5)
date = Entry(wrapper3).grid(row=1, column=7)




#radiobuttons
radiob1= Label(wrapper3, text= 'Bench:', width=30, font=('bold',10))
radiob1.grid(row=3, column=0)
var1=IntVar()
Radiobutton(wrapper3, text='Endoserology', variable=var1, value=1).grid(row=3, column=1)
Radiobutton(wrapper3, text='Chemistry', variable=var1, value=2).grid(row=3, column=2)
Radiobutton(wrapper3, text='Haematology', variable=var1, value=3).grid(row=3, column=3)

radiob2=Label(wrapper3, text='Material:', width=30, font=('bold',10))
radiob2.grid(row=5, column=0)
var2=IntVar()
Radiobutton(wrapper3, text='Reagent', padx=5, variable=var2, value=1).grid(row=5, column=1)
Radiobutton(wrapper3, text='QC', padx=5, variable=var2, value=2).grid(row=5, column=2)
Radiobutton(wrapper3, text='Calibrator', padx=5, variable=var2, value=3).grid(row=5, column=3)
Radiobutton(wrapper3, text='Consumable', padx=5, variable=var2, value=4).grid(row=5, column=4)



#frame4
wrapper4= LabelFrame(main, text='Search base')
wrapper4.pack(fill='both', expand='yes',padx=5,ipady=70, pady=10)

#label and entry
Button(wrapper4, text='Search').place(relx=0.237, rely=0.1)
search_entry = tk.Entry(wrapper4)
search_entry.place(relx=.01, rely=0.1, width=300, height=25)
result_text=tk.Text(wrapper4, yscrollcommand=scrollbary)
result_text.place(relx=.01, rely=0.3, width=1320, height=100)
Label(wrapper4, text='Result').place(relx=0.8, rely=0.1, height=25)

#scrollbar
scrollbary=Scrollbar(wrapper4, orient=VERTICAL)
scrollbary.place(relx=0.9848, rely=0.3, width = 20, height= 100)
scrollbary.configure(command=result_text.yview())
result_text.configure(yscrollcommand=scrollbary.set)
'''

main.mainloop()
