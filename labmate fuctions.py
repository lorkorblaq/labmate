def submit():
    z=username.get()
    y=item_inuse.get()
    x=Quantity.get()
    w=date.get()
    v=lot_no.get()
    u=qc_issues.get()  
    
def clear():
    [widget.delete(0, tk.END) for widget in main.winfo_children() if isinstance(widget, tk.Entry)]