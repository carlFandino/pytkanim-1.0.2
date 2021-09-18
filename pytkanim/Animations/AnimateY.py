from .. import EaseInSineY

styles = ["easeinsine"]
class AnimateY:
    """
    >>> import tkinter
    >>> root = tkinter.Tk()
    >>> Label = AnimateY(0.9,0,'up',tkinter.Label(bg='Black'),style="easeinsine")
    >>> Label.run()
    >>> root.geometry("800x600")
    >>> root.mainloop()

    """

    def __init__(self,startY,endX,direction,widget,style,speed=200):
        if style == "":
            print("Please provide easing function.\n")

        style = style.lower()


        if style in styles:
            if style == "easeinsine":
                self.__widget__ = EaseInSineY(startY,endX,direction,widget,speed)
        else:
            raise AttributeError(f"No easing function called {style}.")


    def run(self):
        """ Start animating """
        self.__widget__.__run__()

    def stop(self):
        """Stops the animation"""
        self.__widget__.__stop__()
