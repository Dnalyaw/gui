from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog

#Always put root.Tk() in any tkinter gui
#root.title("Creates a title for the project")
#root.iconbitmap('put the directory in, and you can put an icon into the app')
#root.quit quits the program
#root.geometry("400x400") changes how the box looks in size
root = Tk()

#creating widget
    # Adding a label: 'variable' = Label(root, text = "string of text")
    # Adding an Entry widget/ giving the user an input: 'variable' = Entry(root);
    # Adding a button: 'variable' = Button(root, text = "string of text");
    # Adding a radio button: 'variable' = Radiobutton(root, text = "string of text");
    # Adding another window: 'variable' = Toplevel()
    # Adding a bad slider:
#def slide():
#     root.geometry(str(horizontal.get()) + "x" + (str(vertical.get())))
# vertical = Scale(root, from_=0, to=400)
# vertical.pack()
# horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
# horizontal.pack()
# my_button = Button(root, text="Slider number", command=slide).pack()
    #Adding a dropdown menu:
#clicked = StringVar()
#clicked.set(weekdays[0])
#drop = OptionMenu(root, clicked, *type of list)
#drop.pack()
        # .destroy will destroy that window
    # Adding a frame: 'variable' = LabelFrame(root, text = "string of text"); to put something inside the frame, change root to the variable used for the frame
    # Adding a popup/messagebox(after importing messagebox): messagebox.showwinfo("Title", "Text")
        #Types of popups: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    #Adding a checkbox: Checkbutton(root, text="Checkbox", variable=var, onvalue="on", offvalue="off")
    # Adding an image (after importing PIL) = ImageTk.PhotoImage(Image.open(Photo in folder))
        # Extra commands:
        # state=DISABLED -> disables
        # padx/pady or width/length = 50 -> changes the width/length
        # command = 'function' -> tells app what to do if the button is clicked
            #command = lambda: ->gives parameters for those
        # Text Color: fg='blue'
        # Background color: bg="red"
        # make a border: bd=1
        # making a bolder border: borderwidth=5
        # Because tkinter uses rows and columns in making apps, you can make something span some rows or columns with :columnspan/rowspan = 3
        # Bring sink a text to the bottom of the screen: relief=SUNKEN
        # sticky= W+E spreads the thing from west to east
        # anchor = E changes the type of alignment to the right side, so E, or east, is right align
        #adding a value: value=topping


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

def popup():
    messagebox.showinfo("You Just Got RickRolled", "Never Gonna Give you Up!")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in MODES:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myButton = Button(root, text="Which topping are you picking?", command=lambda: clicked(pizza.get()))
myButton.pack()

my_info_button = Button(root, text="Popup", command=popup).pack()

#shoving it onto screen
 # .pack places the text and packs it a big as the stuff inside is; it also mid aligns the text
 # .grid places your inputs into the app, but makes you input the location(row= 2, column=2)
 # .grid_forget places
 # .get saves an input for use later/puts it in the system; for example , after a user types an entry widget, you can use .get to use that information later on
 # .insert is mainly used for entry widgets where you have to input : index, string
 # .delete deletes whatever is in the widget




#Extras:
    #IntVar()/StringVar(): constructing a variable
    #opening files dialog box: root.filename = filedialog.askopenfilename(initialdir="D:/Photoshops", title="Photoshops", filetypes=(("jpeg files", "*.JPG"), ("all files", "*.*")))



#looping it
root.mainloop()