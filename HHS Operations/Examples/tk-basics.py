# !Python3                                              A3R0NA$
from tkinter import *
from tkinter import messagebox as mb


# Main steps
# 1 Create a window
root = Tk()
# 2 Create a widget
new_label = Label(root, text="Hello World!")
# 3 Place widget into window
new_label.pack()
# 4 Create work loop
root.mainloop()


# Widgets
tk_variable = IntVar()  # TK variable used by some widgets
# Label
my_label = Label(root, text="Hello")
# Button-Press (dead)
dead_button = Button(root, text="No Press", state=DISABLED)
# Button-Press (live)
def my_func():
    func_label = Label(root, text="BOOM!")
    func_label.pack()
my_button = Button(root, text="Click, Click...", command=my_func)
# Button-Radio
Radiobutton(root, text='Option 1', variable=tk_variable, value=1)
Radiobutton(root, text='Option 2', variable=tk_variable, value=2)
# Input box
my_entry = Entry(root, width=50)
get_my_entry = my_input.get()
# Frame
my_frame = LabelFrame(root, text='My Frame')
# Slider/counter bar
my_slider = Scale(root, from_=0, to=200, orient=VERTICAL)
    my_slider.get() # Use value of slider position
# Checkbox (default 0/1 value)
ch_box = Checkbutton(root, text='Select Me', variable=tk_variable, onvalue='Yes', offvalue='No')
    # NOTE: If setting custom value, add a deselect() func after


# Widget/Window functions
root.bitmapimage('path')  # Add ico file as icon
w.pack()  # Place widget into next available position
w.grid()  # Place widget into grid positions
w.place()  # Place widget into specific position
w.insert(0, 'Text')  # Enters text into widget
w.delete(0, End)  # Delete text in widget
w.get()  # Grab data from widget
w.deselect()  # Un-select button


# Message box windows (symbol)
    # Typlically used as a function with x = mb.box()
mb.showinfo('Title', 'Message')  # Info popup (i) with ok; ok as response
mb.showwarning()  # Warning popup (!) with ok; ok as response
mb.showerror()  # Error popup (x) with ok; ok as response
mb.askquestion()  # Question popup (?) with yes/no buttons; 1/0 as response
mb.askokcancel()  # Question popup (?) with ok/cancel; 1/0 as response
mb.askyesno()  # Question popup (?) with yes/no; yes/no as response
mb.askyesnocancel()  # Question popup (?) with yes/no/cancel; 1/0/NONE response


# Widget Parameters - Widget(window, param)
text='Text Here'  # Add text or label
fg='blue'  # Foreground/Text color
bg='red'  # Background color
height=50  # Set height
width=50  # Set width
row=0  # First row
column=0  # First column
rowspan=2  # Size to height of 2 rows
columnspan=2  # Size to width of 2 columns
sticky=W+E  # Sticks from West to East side (grid)
anchor=E  # Anchors text to East side
padx=50  # Spacing on x-axis
pady=50  # Spacing on y-axis
bd=1  # Set boarder
relief=SUNKEN  # Sets relief to sunken down
borderwidth=25  # Set boarder size
command=function  # Set an actions command
state=DISABLED  # Set status
variable=x, value=1  # Set widgit variable name and value
    x = IntVar()  # Sets type of variable
    x = StringVar()
    x.set()  # Set the variable & default
    x.get()  # Get the variable

# Basic Commands (root = window name)
root.quit()
