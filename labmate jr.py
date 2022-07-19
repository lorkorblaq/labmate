import shutil
import sqlite3
import subprocess
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import customtkinter
from PIL import ImageTk
from tkcalendar import DateEntry

main = Tk()
tk = Tk

main.title('❤ &💡')
main.geometry('1366x760')
main.iconbitmap('')
main.config(highlightthickness=2, bg='black')

# frame1 ==========================QC FRAME
benchs = ["Endoserology", "Chemistry", "Haematology"]

endo_machine = ["Unicel DXI", "Access", "Abbott"]
chem_machine = ["AU 680", "BIORAD DJ"]
haema_machine = ["Sysmex XN550", "Sysmex XN31", "Biorad DM", "Sebia", "BD Fascount"]

endo_analyte = ['Free t4', 'TSH', 'free t3', 'Prolactin']
au_analyte = ['Na', 'K', 'Cl']
dj_analyte = ['HbA1C', 'Hb Elect']
xn550 = ['FBC']
xn31 = ['Malaria Parasite']
hb_analyte = ['Hb Elect', 'Hba1C']
bdfasc = ['CD4']
sebi = ['Hb Elect']
days = ['AM', 'PM']
conn= sqlite3.connect('clinicals.db')
c= conn.cursor()
c.execute('SELECT * FROM qc')
rows=c.fetchall()
conn.close()

def show_frame1():

    hide_frames()
    frame1.grid(sticky='nswe')

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)

    def update2():
        q = qc_management.get('1.0', END)
        e = eqa_no_entry.get()
        p = put_in_use.get('1.0', END)
        o = occurrences.get('1.0', END)
        dy = day.get()
        u = users.get()

        selected_iid = trv.focus()
        item_index = trv.index(selected_iid)

        conn= sqlite3.connect('clinicals.db')
        c=conn.cursor()
        query=f"UPDATE qc SET qc_management = ?, put_in_use=?,occurences=? WHERE rowid={item_index}"
        c.execute(query,(q,p,o))
        
        conn.commit()
        conn.close()
        occurrences.delete('1.0', END)
        put_in_use.delete('1.0', END)
        qc_management.delete('1.0', END)







    def pick_machine():
        if bench.get() == "Endoserology":
            machine.config(values=endo_machine)
            machine.current(0)
        elif bench.get() == "Chemistry":
            machine.config(values=chem_machine)
            machine.current(0)
        elif bench.get() == "Haematology":
            machine.config(values=haema_machine)
            machine.current(0)

    def pick_analyte(e):
        if machine.get() == ("Unicel DXI" or "Access" or "Abbott"):
            analyte_combobox.config(values=endo_analyte)
            analyte_combobox.current(0)
        elif machine.get() == "AU 680":
            analyte_combobox.config(values=au_analyte)
            analyte_combobox.current(0)
        elif machine.get() == "BIORAD DJ":
            analyte_combobox.config(values=dj_analyte)
            analyte_combobox.current(0)
        elif machine.get() == "Sysmex XN550":
            analyte_combobox.config(values=xn550)
            analyte_combobox.current(0)
        elif machine.get() == "Sysmex XN31":
            analyte_combobox.config(values=xn31)
            analyte_combobox.current(0)
        elif machine.get() == "Biorad DM":
            analyte_combobox.config(values=hb_analyte)
            analyte_combobox.current(0)
        elif machine.get() == "Sebia":
            analyte_combobox.config(values=sebi)
            analyte_combobox.current(0)
        elif machine.get() == "BD Fascount":
            analyte_combobox.config(values=bdfasc)
            analyte_combobox.current(0)



    def add():
        d = date.get()
        b = bench.get()
        q = qc_management.get('1.0', END)
        e = eqa_no_entry.get()
        p = put_in_use.get('1.0', END)
        o = occurrences.get('1.0', END)
        dy = day.get()
        u = users.get()
        bb = bias_l.get()
        t = trend_l.get()

        conn = sqlite3.connect('clinicals.db')
        c = conn.cursor()
        c.execute("INSERT INTO qc (date,bench,qc_management,put_in_use,occurences,day,user) VALUES (?,?,?,?,?,?,?)",
                  (d, b, q, p, o, dy, u,))

        rows =c.execute('SELECT * FROM qc')
        rows = c.fetchall()
        conn.commit()
        conn.close()
        update(rows)


        qc_management.delete('1.0', END)
        occurrences.delete('1.0', END)
        put_in_use.delete('1.0', END)
        bench.delete('0', END)
        machine.delete('0', END)
        analyte_combobox.delete('0', END)
        users.delete('0', END)
        eqa_no_entry.delete('0', END)
        day.delete('0', END)

    def getrows(e):
        rowid=trv.identify_row(e.y)
        #itemm=trv.item(rowid,values=[2])
        itemo=trv.item(trv.focus())
        qc_m= itemo['values'][2]
        put_m=itemo['values'][3]
        occ= itemo['values'][4]
        qc_management.insert(INSERT, qc_m)
        put_in_use.insert(INSERT, put_m)
        occurrences.insert(INSERT, occ)


    bench = ttk.Combobox(frame1, values=benchs)
    bench.grid(row=0, column=1, padx=5, sticky='nswe')
    bench.bind("<<ComboboxSelected>>", pick_machine)

    machine = ttk.Combobox(frame1, values=[" "])
    machine.grid(row=0, column=2, padx=5, sticky='nswe')
    machine.bind("<<ComboboxSelected>>", pick_analyte)

    analyte_combobox = ttk.Combobox(frame1, values=[" "])
    analyte_combobox.grid(row=0, column=3, padx=5, sticky='nswe')

    day = ttk.Combobox(frame1, values=days, width=20, )
    day.grid(row=0, column=4, padx=5, sticky='e')

    user = (
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

    users = ttk.Combobox(frame1, values=user)

    users.grid(row=0, column=5, sticky='nsew')

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

    qc_label = customtkinter.CTkLabel(frame1, text="Document root cause, troubleshooting and action taken(Where "
                                                   "applicable)",
                                      text_font=("Helvetica", -13))  # <- custom tuple-color
    qc_label.grid(row=2, column=1, sticky='s')

    qc_management = Text(frame1, width=75, height=6, bg='#cad5f2', fg='black')
    qc_management.grid(row=2, column=1, columnspan=3, rowspan=4, sticky='w')

    put_in= customtkinter.CTkLabel(frame1, text="Items put in use", text_font=("Helvetica", -12))
    put_in.grid(row=2, column=4, sticky='s')
    put_in_use = Text(frame1, width=30, height=6, bg='#cad5f2', fg='black')
    put_in_use.grid(row=2, column=4, rowspan=4, padx=10, sticky='e')

    occur= customtkinter.CTkLabel(frame1, text="Occurences",
                                             text_font=("Helvetica", -13))  # <- custom tuple-color
    occur.grid(row=2, column=5, sticky='se')

    occurrences = Text(frame1, width=20, height=6, bg='#cad5f2', fg='black')
    occurrences.grid(row=2, column=5, rowspan=4, sticky='')

    customtkinter.CTkLabel(frame1, text="Acceptable", text_font=("Helvetica", -16)).grid(row=6, column=1,
                                                                                         sticky='w')

    eqa_no_entry = customtkinter.CTkEntry(frame1, width=10, placeholder_text="EQA CYCLE/SAMPLE USED TO VALIDATE")
    eqa_no_entry.grid(row=5, column=1, sticky='we', ipadx=100)

    add_bt = customtkinter.CTkButton(frame1, text="ADD", text_font=("Helvetica", -16),command=add)
    add_bt.grid(row=6, column=5)

    qc_switch = customtkinter.CTkSwitch(frame1, text="QC PENDING")
    qc_switch.grid(row=5, column=5)

    sel = StringVar()

    date = DateEntry(frame1, variable=sel, selectmode='day', date_pattern="dd-mm-yyyy")
    date.grid(row=0, column=0)

    var1 = tkinter.IntVar(value=0)

    eqa_radio1 = customtkinter.CTkRadioButton(master=frame1, variable=var1,
                                              value=0, text="yes", text_font=("Helvetica", -16))
    eqa_radio1.grid(row=6, column=1, ipadx=65)

    eqa_radio2 = customtkinter.CTkRadioButton(frame1, variable=var1, value=1, text="no", text_font=("Helvetica", -16))
    eqa_radio2.grid(row=6, column=1)

    # treeview
    # treeview styling
    style = ttk.Style()
    style.theme_use('classic')
    style.configure('Treeview.Heading', background='cad5f2', foreground='black')
    style.configure('Treeview', fieldbackground='#cad5f2',background='#cad5f2')
    style.configure('DateEntry', fieldbackground='#cad5f2', foreground='black')



    style.map('Treeview.Heading', background=[('selected','yellow')])

    trv = ttk.Treeview(frame1, columns=('1', '2', '3', '4', '5', '6','7'), height=15, show='headings')
    trv.grid(row=8, column=0, rowspan=6, columnspan=6, padx=8,  sticky='nswe')
    #column

    trv.column("1", stretch=NO, minwidth=70, width=70)
    trv.column("2", stretch=NO, minwidth=80, width=80)
    trv.column("3", stretch=YES, minwidth=75, width=400)
    trv.column("4", stretch=NO, minwidth=80, width=80)
    trv.column("5", stretch=NO, minwidth=75, width=150)
    trv.column('6', stretch=NO, minwidth=30, width=30)
    trv.column("7", stretch=NO, minwidth=140, width=140)
    # headings
    trv.heading(1, text="date")
    trv.heading(2, text="bench")
    trv.heading(3, text="qc_management")
    trv.heading(4, text="put_in_use")
    trv.heading(5, text="occurences")
    trv.heading(6, text="day")
    trv.heading(7, text="user")





    trv.bind('<Double -1>', getrows)
    update(rows)






    # scrollbar
    scrollbary = Scrollbar(frame1)
    scrollbary.grid(row=8, column=5, rowspan=6, sticky='ens')
    scrollbary.config(command=trv.yview)
    trv.configure(yscrollcommand=scrollbary.set)

    update_bt = customtkinter.CTkButton(frame1, text="Update", command=update2)
    update_bt.grid(row=14, column=2, pady=10)

    del_bt = customtkinter.CTkButton(frame1, text="Delete", command=add)
    del_bt.grid(row=14, column=5, padx=5)

    customtkinter.CTkLabel(frame1, text='❤ &💡', text_font=("Chiller", -15)).grid(row=15, column=9, padx=15,
                                                                                  pady=30, sticky='s')

    # backend



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


def reviews():
    pass


def eqa_frame():
    frame7.forget()

    def reports():
        pass
    # Listbox(framee7, width=100, height=40).grid(row=5,column=5)

    # framee7= Frame(main).grid()


def iqa_frame():
    pass


# noinspection PyTypeChecker
def show_frame7():
    hide_frames()
    frame7.grid(sticky='nswe')

    def reader():
        # Add your pdf location and width and height.

        # file= filedialog.askopenfilename(title="Select ",filetype=("PDF Files","*.pdf"))
        file = r"C:\Users\DELL\Documents\tkinter.pdf"
        subprocess.Popen([file], shell=True)

        # filer= open(file,'r')

        # Get the content of the Page
        # content= page.extractText()

    '''
    def display(event):
        endo= eqa_combo.get() == 'Endoserology'
        chem= eqa_combo.get() == 'Chemistry'

        pass
        if endo:
            trv_eqa.grab_release()
            trv_eqa.insert('', index=0, iid=0, text='Immuno20/1')
            trv_eqa.insert('', index=1, iid=1, text='Immuno20/2')
            trv_eqa.insert('', index=2, iid=2, text='Immuno20/3')
            trv_eqa.insert('', index=3, iid=3, text='Immuno20/4')
            trv_eqa.insert('', index=4, iid=4, text='Immuno20/5')


        elif chem:
            trv_eqa.insert('', index=5, iid=5, text='chm19/1')
            trv_eqa.insert('', index=6, iid=6, text='chm19/2')
            trv_eqa.insert('', index=7, iid=7, text='chm19/3')
            trv_eqa.insert('', index=8, iid=8, text='chm19/4')
            trv_eqa.insert('', index=9, iid=9, text='chm19/5')
    '''

    def create_eqa():
        framee7 = tk()

        def report():
            dd= r"C:\Users\DELL\Documents\Labmate"
            g= filedialog.askopenfilename(initialdir=r"C:\Users\DELL\Downloads", title="Select a PDF",
                                          filetype=(("PDF    Files","*.pdf"),("pdf Files","*.pdf")))
            shutil.move(g,dd)

        def create_rv():
            pass

        cmb1 = ttk.Combobox(framee7, background='yellow', font="Helvetica", values=eqa, width=5)
        cmb1.grid(row=0, column=0)
        Button(framee7, text='Report', command=report).grid(row=2, column=0)
        Button(framee7, text='Review', command=create_rv).grid(row=3, column=0)
        Button(framee7, text='Attached documents', command=create_rv).grid(row=3, column=0)

        framee7.mainloop()

    # frame7.configure(bg='yellow')

    eqa = ('Endoserology', 'Chemistry', 'UrineChemistry', 'Haematology', 'Infectives', 'HbA1c & Cardiac', 'IQA')

    eqa_bt = customtkinter.CTkButton(frame7, width=20, height=50, text='Create', text_font=('Chiller', -60),
                                     command=create_eqa).grid(row=4, column=5)
    # iqa_bt= customtkinter.CTkButton(frame7,width=20, height=50, text='Edit',
    #              text_font=('Chiller', -60),command=eqa_frame).place(x=150,y=5)

    # treeview

    trv_eqa = ttk.Treeview(frame7, columns=(), height=19, padding=15, selectmode=BROWSE)
    trv_eqa.grid(row=5, column=3)
    trv_eqa.heading('#0', text='EQA & IQA', anchor='w')
    trv_eqa.column('#0', width=300, stretch=NO)

    def access(e):
        # selected_trv = trv_eqa.focus()
        # rowid=trv_eqa.index(selected_trv)
        # trv_eqa.get_children()
        # trv_eqa.index()
        rowid = trv_eqa.selection()
        # details=trv_eqa.item(trv_eqa.focus())
        if rowid == '46':
            print(rowid)
        # reader()

    trv_eqa.bind("<Double-1>", access)

    def endo():
        # for i in endo:
        # where iid=(46,47)
        pass

    # eqa
    trv_eqa.insert('', index=0, iid=1, text='Endoserology', values='')
    trv_eqa.insert('', index=1, iid=2, text='Chemistry', values='')
    trv_eqa.insert('', index=2, iid=3, text='UrineChemisty', values='')
    trv_eqa.insert('', index=3, iid=4, text='Haematology', values='')
    trv_eqa.insert('', index=4, iid=5, text='Infectives', values='')
    trv_eqa.insert('', index=5, iid=6, text='Hba1c & Cardiac', values='')
    trv_eqa.insert('', index=6, iid=7, text='IQA', values='')
    # endo
    trv_eqa.insert('1', index=0, iid=8, text='20/1', values='')
    trv_eqa.insert('1', index=1, iid=9, text='20/2', values='')
    trv_eqa.insert('1', index=2, iid=10, text='20/3', values='')
    trv_eqa.insert('1', index=3, iid=11, text='20/4', values='')
    trv_eqa.insert('1', index=4, iid=12, text='20/5', values='')
    trv_eqa.insert('1', index=5, iid=13, text='20/6', values='')
    # chem
    trv_eqa.insert('2', index=0, iid=14, text='19/1', values='')
    trv_eqa.insert('2', index=1, iid=15, text='19/2', values='')
    trv_eqa.insert('2', index=2, iid=16, text='19/3', values='')
    trv_eqa.insert('2', index=3, iid=17, text='19/4', values='')
    trv_eqa.insert('2', index=4, iid=18, text='19/5', values='')
    trv_eqa.insert('2', index=5, iid=19, text='19/6', values='')
    # urinechem
    trv_eqa.insert('3', index=0, iid=20, text='17/1', values='')
    trv_eqa.insert('3', index=1, iid=21, text='17/2', values='')
    trv_eqa.insert('3', index=2, iid=22, text='17/3', values='')
    trv_eqa.insert('3', index=3, iid=23, text='17/4', values='')
    trv_eqa.insert('3', index=4, iid=24, text='17/5', values='')
    trv_eqa.insert('3', index=5, iid=25, text='17/6', values='')
    # haeamtology
    trv_eqa.insert('4', index=0, iid=26, text='2/1', values='')
    trv_eqa.insert('4', index=1, iid=27, text='2/2', values='')
    trv_eqa.insert('4', index=2, iid=28, text='2/3', values='')
    trv_eqa.insert('4', index=3, iid=29, text='2/4', values='')
    trv_eqa.insert('4', index=4, iid=30, text='2/5', values='')
    trv_eqa.insert('4', index=5, iid=31, text='2/6', values='')
    # infectives
    trv_eqa.insert('5', index=0, iid=32, text='8/1', values='')
    trv_eqa.insert('5', index=1, iid=33, text='8/2', values='')
    trv_eqa.insert('5', index=2, iid=34, text='8/3', values='')
    trv_eqa.insert('5', index=3, iid=35, text='8/4', values='')
    trv_eqa.insert('5', index=4, iid=36, text='8/5', values='')
    trv_eqa.insert('5', index=5, iid=37, text='8/6', values='')
    # hba1c&infect
    trv_eqa.insert('6', index=0, iid=38, text='9/1', values='')
    trv_eqa.insert('6', index=1, iid=39, text='9/2', values='')
    trv_eqa.insert('6', index=2, iid=40, text='9/3', values='')
    trv_eqa.insert('6', index=3, iid=41, text='9/4', values='')
    trv_eqa.insert('6', index=4, iid=42, text='9/5', values='')
    trv_eqa.insert('6', index=5, iid=43, text='9/6', values='')
    # iqa
    trv_eqa.insert('7', index=0, iid=44, text='Haematology', values='')
    trv_eqa.insert('7', index=1, iid=45, text='Endoserology', values='')

    # documns
    endo201 = [(trv_eqa.insert('8', index=0, iid=46, text="Report", values=''),
                trv_eqa.insert('8', index=1, iid=47, text="Review", values=''))]
    endo202 = [(trv_eqa.insert('9', index=0, iid=48, text="Report", values=''),
                trv_eqa.insert('9', index=1, iid=49, text="Review", values=''))]
    endo203 = [(trv_eqa.insert('10', index=0, iid=50, text="Report", values=''),
                trv_eqa.insert('10', index=1, iid=51, text="Review", values=''))]


def hide_frames():
    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()
    frame4.grid_forget()
    frame5.grid_forget()
    frame6.grid_forget()
    frame7.grid_forget()


# frame1 ==========================QC FRAME
frame1 = Frame(main, width=600, height=500, bg='#758fd2')

#frame1.create_image(0,0, image=bgg, anchor='nw')

frame2 = Frame(main, width=600, height=500, bg='green')

frame3 = Frame(main, width=600, height=500, bg='yellow')

frame4 = Frame(main, width=600, height=500, bg='black')

frame5 = Frame(main, width=600, height=500, bg='white')

frame6 = Frame(main, width=600, height=500, bg='white')

frame7 = Canvas(main, width=1370, height=750, bg='white')
bg = ImageTk.PhotoImage(file='qcc.png')
frame7.create_image(650, 250, image=bg, )

'''
def clear():
    search_entry.delete(0,END)
    result_text.delete(0,END)
def search():
    data = wiki.page(search_entry.get())
    
    clear()
    result_text.insert(0.0, data.content)
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

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New...', command=show_frame)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=show_frame)

page_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Pages', menu=page_menu)
page_menu.add_command(label='QC...', command=show_frame1)
page_menu.add_command(label='Reagent Log', command=show_frame2)
page_menu.add_command(label='Instrument', command=show_frame3)
page_menu.add_command(label='Search', command=show_frame4)
page_menu.add_command(label='LIS', command=show_frame5)
page_menu.add_command(label='Mail', command=show_frame6)
page_menu.add_command(label='EQA & IQA', command=show_frame7)

'''


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
if __name__== '__main__':

    main.mainloop()

