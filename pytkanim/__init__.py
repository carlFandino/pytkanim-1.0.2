# PyTkAnim : Animator for Tkinter GUI module.

# Copyright (c) 2021 Carl Fandino

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
PyTkAnim is extension for tkinter that provides animator and simple usage.

# animate Y when button is clicked
import tkinter as tk
from pytkanim import CustomAnimations
root = tk.Tk() 
                                   #Widget Name    can be also 'up'
Label = CustomAnimations.NormalAnimY(tk.Label(bg="Black"),"down") 
Button = tk.Button(text="Click Me",command=Label.run)
Button.pack()
root.geometry("800x600")
root.mainloop()


# animate X when button is clicked
import tkinter as tk
from pytkanim import CustomAnimations
root = tk.Tk()
                                  #Widget Name    can be also 'backwards'
Label = CustomAnimations.NormalAnimX(tk.Label(bg="Black"),"forward") 
Button = tk.Button(text="Click Me",command=Label.run)
Button.pack()
root.geometry("800x600")
root.mainloop()


# You can add starter X and Y positions too! by simple doing this
import tkinter as tk
from pytkanim import CustomAnimations
root = tk.Tk()
Label = CustomAnimations.NormalAnimX(tk.Label(bg="Black"),"backwards",startAX=0.5,startAY=0.5)
Button = tk.Button(text="Click Me",command=Label.run)
Button.pack()
root.geometry("800x600")
root.mainloop()


# and also how speed to animate is.
import tkinter as tk
from pytkanim import CustomAnimations
root = tk.Tk()
Label = CustomAnimations.NormalAnimX(tk.Label(bg="Black"),"forward",startAX=0.5,startAY=0.5,speed=10) #Higher amount of speed the more it goes slower
Button = tk.Button(text="Click Me",command=Label.run)
Button.pack()
root.geometry("800x600")
root.mainloop()

# Stop and Continue Animation 
import tkinter as tk
from pytkanim import CustomAnimations
stopped = False
root = tk.Tk()
Label = CustomAnimations.NormalAnimX(tk.Label(bg="Black"),"forward",startAX=0,startAY=0.5,speed=10)
Label.run()
def continueAndStop():
    global stopped,Label
    if stopped == False:
        stopped = True
        Label.stop()
    else:
        stopped = False
        Label.continueAnim()
Button = tk.Button(text="Stop/Continue",command=continueAndStop)
Button.pack()
root.geometry("800x600")
root.mainloop()

# Changing Direction
import tkinter as tk
from pytkanim import CustomAnimations
directionChanged = True
root = tk.Tk()
Label = CustomAnimations.NormalAnimX(tk.Label(bg="Black"),"forward",startAX=0,startAY=0.5,speed=10)
Label.run()

def changingDirection():
    global directionChanged,Label
    if directionChanged == False:
        directionChanged = True
        Label.changeDirection("forward")
    else:
        directionChanged = False
        Label.changeDirection("backwards")


Button = tk.Button(text="Click to Change Direction",command=changingDirection)
Button.pack()
root.geometry("800x600")
root.mainloop()
"""

from . import __easingfunctionsX__
from . import __easingfunctionsY__
import os


__author__ = "Carl Fandiño"
__version__ = "1.0.2"
printIntro = False



EaseInSineX = __easingfunctionsX__.ease_in_sine.ease_in_sine
EaseInSineY = __easingfunctionsY__.ease_in_sine.ease_in_sine


if printIntro:
    print(f"Using PyTkAnim Version {__version__} Author: {__author__}")
    print(f"You can turn off this message by turning 'printIntro' to False in __init__ file.")
else:
    pass



