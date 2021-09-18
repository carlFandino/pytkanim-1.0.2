from .. import EaseInSineX

styles = ["easeinsine"]
class AnimateX:
    """
    >>> import tkinter
    >>> root = tkinter.Tk()
    >>> Label = AnimateX(0,0.5,'forward',tkinter.Label(bg='Black'))
    >>> Label.run()
    >>> root.geometry("800x600")
    >>> root.mainloop()

    """
    def __init__(self,startX,endX,direction,widget,style,speed=200):
        if style == "":
            print("Please provide easing function.\n")

        style = style.lower()


        if style in styles:
            if style == "easeinsine":
                self.__widget__ = EaseInSineX(startX,endX,direction,widget,speed)
        else:
            raise AttributeError(f"No easing function called {style}.")


    def run(self):
        """ Start animating """
        self.__widget__.__run__()

    def stop(self):
        """Stops the animation"""
        self.__widget__.__stop__()
