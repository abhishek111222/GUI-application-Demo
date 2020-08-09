from tkinter import *


root = Tk()

def kg_to_others():
    grams = float(e1_value.get()) * 1000 
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274

    t1.delete("1.0", END)
    t1.insert(END, grams)
    
    t2.delete("1.0", END)
    t2.insert(END,pounds)
    
    t3.delete("1.0", END)
    t3.insert(END,ounces)
   
   
root.title("Weights")


# Create a button widget
# The kg_to_others() function is called when the button is pushed
b1 = Button(root, text = "Convert", command = kg_to_others)
b1.grid(row = 0, column = 3)


# Create a Label widget with "Kg" as label
l1 = Label(root, text = "kg")
l1.grid(row= 0, column = 0)


e1_value = StringVar()                                     # Create a special StringVar object
e1 = Entry(root, textvariable = e1_value)
e1.grid(row = 0, column = 1)

# Create three empty text boxes, t1, t2, and t3
t1 = Text(root, width = 20, height = 1)
t1.grid(row = 1, column = 0)

t2 = Text(root, width = 20, height = 1)
t2.grid(row = 1, column = 1)

t3 = Text(root, width = 20, height = 1)
t3.grid(row = 1, column = 2)


#This makes sure to keep the main window open
root.mainloop()