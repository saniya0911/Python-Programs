from tkinter import *

window = Tk()
window.minsize(height=300,width=300)
window.title("Miles to KM Converter")
window.config(padx=50,pady=30)
#input in miles
input = Entry(width=6)
input.grid(row=0, column=1)

#label Miles
miles = Label(text="Miles", font=("Arial",15))
miles.grid(row=0, column=2)

#isequalto label
isequalto = Label(text="is equal to",font=("Arial",15))
isequalto.grid(row=1, column=0)

#kmvalue label
kmvalue = Label(text="0",font=("Arial",15))
kmvalue.grid(row=1,column=1)

def button_clicked():
    mile=float(input.get())
    ans = mile * 1.609
    kmvalue.config(text=f"{ans}")

#km label
km=Label(text="Km",font=("Arial",15))
km.grid(row=1, column=2)

#calculatebutton
calculate = Button(text="Calculate",font=("Arial",15), command=button_clicked)
calculate.grid(row=2,column=1)

window.mainloop()