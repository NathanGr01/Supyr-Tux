import time

class Logger():
	"""eine Klasse, die einen Logger zum Schreiben in Dateien darstellt"""
	
	def write_log(self, nachricht, wichtigkeit):
		"""fügt in eine .txt Datei eine formatierte Nachricht ein"""
		
		filename = "Logger_Bericht.log"
		
		with open (filename, "a") as f:
			f.write("[" + str(wichtigkeit) + "] " + nachricht + " [" + time.strftime("%d.%m.%Y %H:%M:%S") + "]\n")
