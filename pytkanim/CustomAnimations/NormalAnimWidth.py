class NormalAnimWidth:
	"""This animates the WIDTH of the widget given. speed param can be ex.1000 = 1 second or 100 = 1ms or 10 for smoother animation.
    
    Run anim when button is clicked.
	>>> import tkinter as tk
    >>> 
    >>> root = tk.Tk()
    >>> Label = NormalAnimWidth(tk.Label(bg="black"),speed=20)
    >>> #Label.place(relx=0.5,rely=0.5)
    >>> Label.run()
    >>> root.geometry("800x600")
    >>> root.mainloop()

	"""
	normal_speed = 100
	width = 0
	def __init__(self,widget,startW=0,startH=0,speed=normal_speed):
		widget.configure(width=startW,height=startH)
		self.widget = widget
		self.__startW = startW
		self.__startH = startH
		self.speed = speed 
		
		self.isStop = False
		self.__isrunning = False
		self.place()


	def __run__(self):
	    if self.isStop == False:
	    	self.__startW += 1

	    self.width = self.__startW
	    self.widget.configure(width=self.__startW,height=self.__startH) 
	    self.widget.after(self.speed,self.__run__)
	

	def run(self):
		"""Start animating"""
		if self.__isrunning == False:
			self.__isrunning = True
			self.__run__()
		else:
			pass

	def stop(self):
		"""Stops the animation."""
		self.isStop = True

	def continueAnim(self):
		"""Continue animation from animating."""
		self.isStop = False
	def place(self,relx=0,rely=0):
		self.widget.place_configure(relx=relx,rely=rely)
	
	
    	
