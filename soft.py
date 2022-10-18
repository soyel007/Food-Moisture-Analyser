from tkinter import *
from tkinter import messagebox

def reset_entry():
    A_tf.delete(0,'end')
    B_tf.delete(0,'end')
    C_tf.delete(0,'end')

def calculate_bmi():
    w = int(A_tf.get())
    w2 = int(C_tf.get())
    w1 = int(B_tf.get())
    
    numer = w1-w2
    denom = w1-w 
    if(denom <= 0):
        messagebox.showinfo('Result', f'Wrong Inputs')
    if(numer <= 0):
        messagebox.showinfo('Result', f'Wrong Inputs')
    mc=(numer/denom)*100
    mc_index(mc)

def mc_index(mc):
    
    if mc <= 20:
        messagebox.showinfo('Calculation Results', f'Moisture Percentage = {mc}% : Low Moisture Content Food')
    elif (mc > 20) and (mc <= 50):
        messagebox.showinfo('Calculation Results', f'Moisture Percentage = {mc}% : Intermediate Moisture Content Food')
    elif (mc > 50):
        messagebox.showinfo('Calculation Results', f'Moisture Percentage = {mc}% : High Moisture Content Food') 
    else:
        messagebox.showerror('Calculation Results', 'Something Went Wrong!')   

ws = Tk()
ws.title('Food Moisture Analyser')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)

A_lb = Label(
    frame,
    text="Empty Dish Weight (in gm)"
)
A_lb.grid(row=1, column=1)

A_tf = Entry(
    frame, 
)
A_tf.grid(row=1, column=2, pady=5)


B_lb = Label(
    frame,
    text="Dish + Sample Weight Before Drying (in gm) "
)
B_lb.grid(row=3, column=1)

C_lb = Label(
    frame,
    text="Dish + Sample Weight After Drying (in gm) ",

)
C_lb.grid(row=4, column=1)

B_tf = Entry(
    frame,
)
B_tf.grid(row=3, column=2, pady=5)

C_tf = Entry(
    frame,
)
C_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()