from tkinter import *

def button_clicked():
    my_label["text"] = input.get()
    print("I got clicked")

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx = 20,pady = 20)

# Label

my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# my_label.pack(side="bottom")
#my_label.pack()
#my_label.place(x= 100,y=0)
my_label.grid(column=0,row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=50,pady=50)

# Entry

input = Entry(width=50)
input.grid(column =3, row =2)

# Button

my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1,row=1)

new_button = Button(text="MeinNayaButton")
new_button.grid(row=0,column=2)
#my_button.pack()

window.mainloop()
