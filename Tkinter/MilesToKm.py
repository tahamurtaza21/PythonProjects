from tkinter import *

window = Tk()
window.minsize(width=200,height=100)
window.title("Miles to Kilometer")


equal_to_label = Label(text="is equal to")
equal_to_label.grid(row=1,column=0)

input = Entry(width=40)
input.grid(row=0,column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0,column=2)

def calculateMilestoKM():
    final_value_label["text"] = float(input.get()) * 1.689

calculate_button = Button(text="Calculate",command=calculateMilestoKM)
calculate_button.grid(row=2,column=1)

final_value_label = Label()
final_value_label.grid(row=1,column=1)

km_label = Label(text="KM")
km_label.grid(row=1,column=2)


window.mainloop()