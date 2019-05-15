import pygame
from abc import ABC


from logger import Logger


class Game_Core(ABC):
	"""eine Klasse, die die Grundfunktionen eines 2D-Spiels darstellt"""
	
	def __init__(self, name, color):
		"""erstellt einen farbigen Screen mit fester Größe"""
		super().__init__()
		
		onInit()
		
		self.logger = Logger()
		
		self.screen = pygame.display.set_mode((1920, 1000))
		
		self.pygame.display.set_caption = name
		
		self.bg_color = color

	
	def update(self):
		onUpdate()
		
	
	def render(self):
		onRender()
	
	def run(self):
		init()
		while flag:
			update()
			render()
			sleep()
