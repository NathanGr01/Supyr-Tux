#import logger

na = "Hallo ich bin ein Mensch, wie kein anderer."
print(na[len(na)])

class Parser():
	"""eine Klasse die alle Standarfeinstellungen enthält und um neue erweitert werden kann"""
	def __init__(self):
		self.name = ""
		self.window_width = 200
		self.window_height = 200
		self.fps = 30
		self.add_unknown = False
		self.debug = True
		self.dummy = ""
		
		self.setting_names = ["name", "window-width", "window-height", "fps", "debug", "dummy"]
		
		self.string_settings = ["name", "dummy"]
		self.int_settings = ["fps", "window_width", "window_height"]
		self.bool_settings = ["debug", "add_unknown"]
		
		self.new_settings = []
	
	def parse(filename):
		"""eine Methode die eine übergebene .config Datei einließt und überprüft"""
		
		data = open(filename, "r")
		data_list = data.readlines()
		
		#über jede Zeile wird iteriert
		for line in data_list:
			
			schon_etwas_geschrieben = False
			
			for i in range (0, len(line)-1):
				
				if line[i] == '#':
					break
				
				if line[i] != " ":
					schon_etwas_geschrieben = True
					
				if schon_etwas_geschrieben:
					
					j = i
					
					while line[j] != "=":
						j += 1
						if j == len(line):
							#Fehler
					
					#Fall1: ungültige Eingabe und add_unknown false
					if (line[i:j].strip() not in self.setting_names) and (self.add_unknown == False):
						#Fehler
					
					#Fall2: gültige Eingabe
					if (line[i:j].strip() in self.setting_names):
						
						valid_setting = line[i:j].strip()
						
						#Fall2.1: Schlüsselwort mit Stringtyp
						if (valid_setting in self.string_settings):
							for a in range (j+1, len(line)):
								if a == len(line):
									#Fehler
								elif line[a] == " ":
									continue
								elif line[a] == "\"":
									b = a
									while line[b] != "\"":
										b += 1
										if b == len(line):
											#Fehler
									if valid_setting == "name":
										self.name = line[a+1:b]
									if valid_setting == "dummy":
										self.dummy = line[a+1:b]
										
									i = b+1
									schon_etwas_geschrieben = False
									break
								else:
									#Fehler

						#Fall2.2: Schlüsselwort mit Integertyp
						if (valid_setting in self.int_settings):
							for a in range (j+1, len(line)):
								if a == len(line):
									#Fehler
								elif line[a] == " ":
									continue
								elif line[a].isdigit():
									b = a
									while line[b].isdigit():
										b += 1
									if valid_setting == "fps":
										self.fps = int(line[a:b])
									if valid_setting == "window_width":
										self.window_width = int(line[a:b])
									if valid_setting == "window_height":
										self.window_height = int(line[a:b])
									
									i = b+1
									schon_etwas_geschrieben = False
									break
								else:
									#Fehler
						
						#Fall2.3: Schlüsselwort mit Booltyp
						if (valid_setting in self.bool_settings):
							for a in range (j+1, len(line)):
								if a == len(line):
									#Fehler
								elif line[a] == " ":
									continue
								elif line[a] == "F":
									if a + 4 > len(line):
										#Fehler
									if !(line[a+1]=="a" and line[a+2]=="l" and line[a+3]=="s" and line[a+4]=="e"):
										#Fehler
									if valid_setting == "debug":
										self.debug = False
									if valid_setting == "add_unknown":
										self.add_unknown = False
									i = a+5
									schon_etwas_geschrieben = False
									break
								elif line[a] == "T":
									if a + 3 > len(line):
										#Fehler
									if !(line[a+1]=="r" and line[a+2]=="u" and line[a+3]=="e"):
										#Fehler
									if valid_setting == "debug":
										self.debug = True
									if valid_setting == "add_unknown":
										self.add_unknown = True
									i = a+4
									schon_etwas_geschrieben = False
									break
								else:
									#Fehler
					
					
				
