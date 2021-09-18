class NormalAnimY:
	"""This animates the Y AXIS of the widget given. speed param can be ex.1000 = 1 second or 100 = 1ms or 10 for smoother animation.
    
    Run anim when button is clicked.
	>>> import tkinter as tk
	>>> root = tk.Tk()
	>>> Label = NormalAnimY(tk.Label(bg="Black"),"down")
	>>> Button = tk.Button(command=Label.run)
	>>> Button.pack()
	>>> root.geometry("1080x600")
	>>> root.mainloop()

	"""
	normal_speed = 30
	y = 0
	def __init__(self,widget,direction,startAX=0,startAY=0,speed=normal_speed,stopAY=0):
		widget.place_configure(relx=startAX,rely=startAY)
		self.widget = widget

		self.__startAX = startAX
		self.__startAY = startAY
		self.__stopAY = stopAY
		self.__isrunning = False


		self.speed = speed 
		self.direction = direction.lower()
		self.isStop = False
        
 
		if self.__stopAY < self.__startAY and self.direction == "down":
			raise ValueError("'stopAY' argument must be greater than 'startAY' argument if your direction is down")
		elif self.__stopAY > self.__startAY and self.direction == "up":
			raise ValueError("'stopAY' argument must be less than 'startAY' argument if your direction is up")
		

	def __run__(self):
	    if self.isStop == False:
	        if self.direction == "up" or self.direction == "down":
	            if self.direction == "down" and self.__stopAY == 0:
	                self.__startAY += 0.005
	           
	            elif self.direction == "up" and self.__stopAY == 0:
	                self.__startAY -= 0.005

	            elif self.direction == "up" and self.__stopAY != 0:
	            	if self.__stopAY < self.__startAY:
	            		self.__startAY -= 0.005

	            elif self.direction == "down" and self.__stopAY != 0:
	            	if self.__stopAY > self.__startAY:
	            		self.__startAY += 0.005



	            else:
	                raise TypeError("direction must be up and down")
	    self.y = self.__startAY
	    self.widget.place_configure(relx=self.__startAX,rely=self.__startAY) 
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
	
	def changeDirection(self,direction):
		"""Change direction according to the param direction given."""
		direction = direction.lower()
		if direction == "up" or direction == "down":
			self.direction = direction
		else:
			raise TypeError("direction must be up and down")
	
    	
