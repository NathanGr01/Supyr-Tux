import pygame



class Spieler():
	"""eine Klasse, die einen beliebig gesteuerten Spieler darstellt"""
	
	def __init__(self, bild_link, breite, höhe, screen):
		"""erstellt eine Graphik eines Spielers dessen Bild und Größe festgelegt werden kann"""
		
		self.bild = pygame.image.load(bild_link)
		self.rect = self.bild.get_rect()
		
		self.screen = screen
		
		self.rect.w = breite
		self.rect.h = höhe
		
		#Bewegungsflags
		self.moving_right = False
		self.moving_left = False
	
	def steuern(self):
		"""alle möglichen Eingaben werden abgefangen"""
		for event in pygame.event.get():
			
			#verlassen wird aufgerufen wenn das Spiel geschlossen wird
			if event.type == pygame.QUIT:
				verlassen()
			
			
			#steuern_m_T wird aufgerufen wenn Tasten betätigt werden
			elif event.type == pygame.KEYDOWN:
				steuern_mit_Tastatur(event)
			
			elif event.type == pygame.KEYUP:
				steuern_mit_Tastatur(event)
			
			
			#steuern_m_M wird aufgerufen wenn mit der Maus geklickt wird
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				steuern_mit_Maus(mouse_x, mouse_y)
	
	def steuern_mit_Tastatur(self, event):
		
	def steuern_mit_Maus (self, mouse_x, mouse_y)
