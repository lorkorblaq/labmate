import tkinter
from tkinter import *
from tkinter import ttk

import customtkinter
from tkcalendar import DateEntry

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

main = Tk()
main.title('Labmate')
main.geometry('1366x760')
main.iconbitmap('')
main.config(highlightthickness=2, bg='black')



# bg= PhotoImage(file='lovelight.png')


# frame1 ==========================QC FRAME
bench = ["Endoserology", "Haematology", "Chemistry"]

endo_machine = ["Unicel DXI", "Access", "Abbott"]
chem_machine = ["AU 680", "BIORAD DJ"]
haema_machine = ["Sysmex XN550", "Sysmex XN31", "Biorad DM", "BD Fascount", "Sebia"]

endo_analyte = ['Free t4', 'TSH', 'free t3']
au_analyte = ['Na', 'K', 'Cl']
dj_analyte = ['HBA1C']
xn550_31 = ['FBC']
hb_analyte = ['Hb Elect']
bdfasc= ['CD4']
day= ['AM', 'PM']



def pick_machine(e):
    if bench_combobox.get() == "Endoserology":
        machine_combobox.config(value=endo_machine)

def pick_analyte(e):
    if machine_combobox.get() == "Unicel DXI":
        analyte_combobox.config(value=endo_analyte)

def add():
    pass




def show_frame1():
    hide_frames()
    frame1.pack(fill='both', expand=1)

    bench_combobox = customtkinter.CTkComboBox(frame1, values=bench)
    bench_combobox.grid(row=0, column=1, padx=5, sticky= 'nsew')
    bench_combobox.bind("<<ComboboxSelected>>", pick_machine)

    machine_combobox = customtkinter.CTkComboBox(frame1, values=endo_machine)
    machine_combobox.grid(row=0, column=2, padx=5, sticky= 'nswe')
    machine_combobox.bind("<<ComboboxSelected>>",pick_analyte)

    analyte_combobox = customtkinter.CTkComboBox(frame1, values=endo_analyte)
    analyte_combobox.grid(row=0, column=3, padx=5, columnspan=4, sticky= 'nsew')
    analyte_combobox.bind('<<ComboboxSelected>>',pick_machine)

    day_combo= customtkinter.CTkComboBox(frame1, values=day,width=90,).grid(row=0, column=8, padx=5,sticky='e')


    users = (
        'Fortune Nwosu',
        'Amadi Uche',
        'Kenneth Michelle',
        'Osaigbovo Ebehrimen',
        'Maryann',
        'Eziebe CLaribel',
        'Oloko Olorunfemi',
        'Ndukwe Ruth',
        'Enebeli Gerald',
        'Trainee')

    combx = customtkinter.CTkComboBox(frame1, values=users, width=30)
    combx.grid(row=0, column=9, sticky= 'nsew')




    trend_l = customtkinter.CTkCheckBox(frame1, text="Trend", text_font=("Helvetica", -16))
    trend_l.grid(row=2, column=0, pady=20, padx=10, ipadx=27)

    bias_l = customtkinter.CTkCheckBox(frame1, text="Bias", text_font=("Helvetica", -16))
    bias_l.grid(row=3, column=0, pady=10, padx=10, ipadx=31)

    shift_l = customtkinter.CTkCheckBox(frame1, text="Shift", text_font=("Helvetica", -16))
    shift_l.grid(row=4, column=0, pady=20, padx=10, ipadx=31)

    imprecision_l = customtkinter.CTkCheckBox(frame1, text="Imprecision", text_font=("Helvetica", -16))
    imprecision_l.grid(row=5, column=0, pady=10, padx=10, ipadx=8)

    random_l = customtkinter.CTkCheckBox(frame1, text="Random Error", text_font=("Helvetica", -16))
    random_l.grid(row=6, column=0, pady=10, padx=0)

    qc_label = customtkinter.CTkLabel(frame1,text="Document root cause, troubleshooting and action taken(Where applicable)",
                                      text_font=("Helvetica", -13))  # <- custom tuple-color
    qc_label.grid(row=2, column=1, sticky='sw')

    add_items_label = customtkinter.CTkLabel(frame1,text="Items put in use",
                                      text_font=("Helvetica", -13))  # <- custom tuple-color
    add_items_label.grid(row=2, column=9, sticky='se')

    add_entry = Text(frame1,width=20, height=6, bg='grey', fg='white')
    add_entry.grid(row=1, column=9, rowspan=5, padx=6)

    qc_entry = Text(frame1,width=128, height=6, bg='grey', fg='white')
    qc_entry.grid(row=1, column=1, columnspan=8,rowspan=5)

    qc_label2 = customtkinter.CTkLabel(frame1, text= "Acceptable",text_font=("Helvetica", -16)).grid(row=6, column=1,sticky='w')


    eqa_no_entry= customtkinter.CTkEntry(frame1, width=10, placeholder_text="EQA CYCLE/SAMPLE USED TO VALIDATE")
    eqa_no_entry.grid(row=5, column=1, sticky='we',ipadx=100)

    add_bt = customtkinter.CTkButton(frame1,text="ADD",  command= add)
    add_bt.grid(row=6, column=8)


    qc_switch = customtkinter.CTkSwitch(frame1,text="QC PENDING")
    qc_switch.grid(row=5, column=8)

    sel= StringVar()

    DateEntry(frame1, selectmode='day', date_pattern="dd-mm-yyyy").grid(row=0, column=0)

    var1 = tkinter.IntVar(value=0)


    eqa_radio1 = customtkinter.CTkRadioButton(master=frame1, variable=var1,
                                              value=0, text= "yes",text_font=("Helvetica", -16))
    eqa_radio1.grid(row=6, column=1, ipadx=65)

    eqa_radio2 = customtkinter.CTkRadioButton(frame1,variable=var1,value=1,text= "no",text_font=("Helvetica", -16))
    eqa_radio2.grid(row=6, column=1)
    #treeview

    # ntreeview styling
    style=ttk.Style()
    style.theme_use('alt')
    style.configure('Treeview.Heading', background='black', foreground='white')
    style.configure('Treeview',fieldbackground='grey')
    style.configure('DateEntry', fieldbackground='#363636', foreground='white')

    #style.map('Treeview.Heading', background=[('selected','green')])


    trv = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6), height=15, show='headings')
    trv.grid(row=8, column=0, rowspan=6, columnspan=10, padx=10, sticky='nswe')

    # headings
    trv.heading(1, text="Date")
    trv.heading(2, text="User")
    trv.heading(3, text="Put in-use")
    trv.heading(4, text="DQC Problem")
    trv.heading(5, text="QC Management")
    trv.heading(6, text="Machine")

    # scrollbar
    scrollbary = Scrollbar(frame1, orient=VERTICAL)
    scrollbary.grid(row=8, column=9, rowspan=6, ipady=8,sticky='ens')
    scrollbary.configure(command=trv.yview())
    trv.configure(yscrollcommand=scrollbary.set)

    update_bt = customtkinter.CTkButton(frame1, text="Update", command=add)
    update_bt.grid(row=14, column=2, pady=10)

    del_bt = customtkinter.CTkButton(frame1,text="Delete", command=add)
    del_bt.grid(row=14, column=8, padx=5)

    blaq= customtkinter.CTkLabel(frame1, text='❤ &💡', text_font=("Chiller", -15)).grid(row=15, column=9, padx=15,pady=30, sticky='s')

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
    hide_frames()
    frame6.pack(fill='both', expand=1)


def show_frame7():
    hide_frames()
    frame7.pack(fill='both', expand=1)


def hide_frames():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()


# frame1 ==========================QC FRAME
frame1 = Frame(main, width=600, height=500, bg='black')

frame2 = Frame(main, width=600, height=500, bg='green')

frame3 = Frame(main, width=600, height=500, bg='yellow')

frame4 = Frame(main, width=600, height=500, bg='black')

frame5 = Frame(main, width=600, height=500, bg='white')

frame6 = Frame(main, width=600, height=500, bg='white')

frame7 = Frame(main, width=600, height=500, bg='white')

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
