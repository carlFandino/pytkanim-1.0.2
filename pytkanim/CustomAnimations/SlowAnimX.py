class SlowAnimX:
	"""This animates the X AXIS of the widget given,But it's in slow motion. speed param is to speed up a bit the widget
    >>> import tkinter as tk
    >>> 
    >>> root = tk.Tk()
    >>> Label = SlowAnimX(tk.Label(bg="black"),"forward")
    >>> Label.run()
    >>> root.mainloop()

	"""
	normal_speed = 1
	def __init__(self,widget,direction,startAX=0,startAY=0,speed=normal_speed):
		widget.place_configure(relx=startAX,rely=startAY)
		self.widget = widget
		self.__startAX = startAX
		self.__startAY = startAY
		
		self.direction = direction.lower()
		self.speed = speed
		self.isStop = False
		self.__isrunning = False
	def __run__(self):
		
		if self.speed == 0:
			self.speed = 1
		if self.isStop == False:
			if self.direction == "forward" or self.direction == "backwards":
				if self.speed <= 10 and self.speed >= 0:

					if self.direction == "forward":
						self.__startAX += 0.0007*self.speed
					elif self.direction == "backwards":
						self.__startAX -= 0.0007*self.speed
				elif self.speed > 10:
					raise ValueError("Too much speed. 1-10 is required")
				elif self.speed < 0:
					raise ValueError("Too slow. 1-10 is required")
			   
			else:
				raise TypeError("direction must be forward and backwards")

		self.widget.place_configure(relx=self.__startAX,rely=self.__startAY) 
		self.widget.after(10,self.__run__)

	def run(self):
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
	
	def changeDirection(self,direction):
		"""Change direction according to the param direction given."""
		direction = direction.lower()
		if direction == "forward" or direction == "backwards":
			self.direction = direction
		else:
			raise TypeError("direction must be forward and backwards")
