class ease_in_sine:
	def __init__(self,startY,endY,direction,widget,speed=200):
		widget.place_configure(relx=startY)
		
		self.__widget = widget
		self.start = startY
		self.end = endY
		self.direction = direction.lower()
		self.speed = speed
        
		self.isStop = False
		self.__isrunning = False

		self.__add_y = 0.0005
		self.__to_addy = 0
	
		if self.start > self.end and self.direction == "down":
			raise ValueError("'startY' must be less than 'endY' argument if your direction is down.")
		elif self.start < self.end and self.direction == "up":
			raise ValueError("'startY' must be greater than 'endY' argument if your direction is down.")


		if self.direction == "down":
			self.__add_y = 0.0005
		elif self.direction == "up":
			self.__add_y = 0.00005


		

	def __time__(self):
		
		distance = self.start - self.end
	
		if distance > -0.1 and self.direction == "down":
			self.__add_y = 0.0011
			self.__add_y += self.__to_addy
		

		elif  distance < -0.1 and self.direction == "down":
			self.__to_addy = 0.0003
			self.__add_y += self.__to_addy
	


		elif distance < 0.1 and self.direction == "up":
			self.__add_y = 0.0011
			self.__add_y += self.__to_addy


		elif distance > 0.1 and self.direction == "up":
			self.__to_addy = 0.0003
			self.__add_y += self.__to_addy



		
		
		

		self.__widget.after(self.speed,self.__time__)

	def __start__(self):
		if self.isStop == False:
			if self.start != self.end and self.direction == "down":
				self.start += self.__add_y	
			elif self.start != self.end and self.direction == "up":
				self.start -= self.__add_y	



			if self.start > self.end and self.direction == "down":
				
				self.__stop__()
			elif self.start < self.end and self.direction == "up":
				self.__stop__()




       
		self.__widget.place_configure(rely=self.start)
		self.__widget.after(10,self.__start__)


	def __stop__(self):
		self.isStop = True

		
	def __run__(self):
		if self.__isrunning == False:
            
			self.__isrunning = True
			
			self.__start__()
			self.__time__()
		else:
			pass










