class ease_in_sine:
	def __init__(self,startX,endX,direction,widget,speed=200):
		widget.place_configure(relx=startX)
		
		self.__widget = widget
		self.start = startX
		self.end = endX
		self.direction = direction.lower()
		self.speed = speed
        
		self.isStop = False
		self.__isrunning = False

		self.__add_x = 0.0005
		self.__to_addx = 0
	
		

		if self.direction == "forward":
			self.__add_x = 0.0005
		elif self.direction == "backwards":
			self.__add_x = 0.00005


		if self.start > self.end and self.direction == "forward":
			raise ValueError("'startX' must be less than 'endX' argument if your direction is forward.")
		elif self.start < self.end and self.direction == "backwards":
			raise ValueError("'startX' must be greater than 'endX' argument if your direction is backwards.")
	


	

        
	
        
		

	def __time__(self):
		
		distance = self.start - self.end
	
		if distance > -0.1 and self.direction == "forward":
			self.__add_x = 0.0011
			self.__add_x += self.__to_addx
		

		elif  distance < -0.1 and self.direction == "forward":
			self.__to_addx = 0.0003
			self.__add_x += self.__to_addx
	


		elif distance < 0.1 and self.direction == "backwards":
			self.__add_x = 0.0011
			self.__add_x += self.__to_addx


		elif distance > 0.1 and self.direction == "backwards":
			self.__to_addx = 0.0003
			self.__add_x += self.__to_addx



		
		
		

		self.__widget.after(self.speed,self.__time__)

	def __start__(self):
		if self.isStop == False:
			if self.start != self.end and self.direction == "forward":
				self.start += self.__add_x	
			elif self.start != self.end and self.direction == "backwards":
				self.start -= self.__add_x	



			if self.start > self.end and self.direction == "forward":
				
				self.__stop__()
			elif self.start < self.end and self.direction == "backwards":
				self.__stop__()




       
		self.__widget.place_configure(relx=self.start)
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










