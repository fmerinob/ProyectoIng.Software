import datetime as fecha

class evento:
	def _init_(nombre, fecha, horaIni, horaFin, descripcion):
		self.nombre=nombre
		self.fecha=fecha
		self.horaIni=horaIni
		self.horaFin=horaFin
		self.descripcion=descripcion

class dia:
	def _init_(date):
		self.date=datetime(date).strftime("%x")
		self.eventos={}
		self.codEvento=date + 1001

	def addEvento(nombre, fecha, horaIni, horaFin, descripcion):
		self.eventos[self.codEvento]=evento(nombre, fecha, horaIni, horaFin, descripcion)
		self.codEvento+=1

	def modNomEvent(idEvent,nombre):
		evento(self.eventos[idEvent]).nombre=nombre

	def modDescEvent(idEvent,desc):
		evento(self.eventos[idEvent]).descripcion=desc

	def modHoraIniEvent(idEvent,hIni):
		evento(self.eventos[idEvent]).horaIni=hIni

	def modHoraFinEvent(idEvent,hFin):
		evento(self.eventos[idEvent]).horaFin=hFin

	def delEvent(idEvent):
		if idEvent in self.eventos:
			del self.eventos[idEvent]

class calendario:
	anio = 2019
	diasmes=[31,28,31,30,31,30,31,31,30,31,30,31]
	def _init_():
		self.dias={}
		while anio <=2020:
			for mes in range(12):
				for day in range(diames[mes]):
					if mes==1:
						if anio==2020 and day>28:
							day=31
						elif anio==2019 and day>27:
							day=31
						else:
							self.dias[datetime(anio,mes+1,day+1)]=dia(datetime(anio,mes+1,day+1))
					else:
						self.dias[datetime(anio,mes+1,day+1)]=dia(datetime(anio,mes+1,day+1))
			anio+=1
		