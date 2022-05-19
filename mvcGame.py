import random
from os import system

class Letters():
	"Mi Modelo"
	def __init__(self):
		self.letters = ("a","l","o","d","n","e")
		self.Enwords = ("load","land","lode","loden","done","london","alone","and","lane","all","add","none")
		self.Eswords = ("lana","ola","lado","leona","lodo","lona","nado","dedal","nodo","lana","dedo","ella",
			"ello","olla","dale")
		self.createdWord = 0

	def randomWord(self):
		"Devuelve una palabra aleatoria en cualquier idioma"
		word = random.choice(self.Enwords+self.Eswords)
		self.createdWord += 1
		return word

class View():
	def clear(self):
		system("cls")

class Menu(View):
	"Vista"
	def mainView(self):
		print("\n Menu Principal   ")
		return input(" Generar(1) Ver(2) Salir(3) ")
	
	def viewWords(self,numTotal):
		print("\nPalabras generadas en total (%s)"%(numTotal))
		

class Reader(View):
	"Vista"
	def __init__(self,language):
		self.language = language
	
	def pronounce(self,word):
		print("\nLector de %s dice:"%(self.language))
		print("(%s) palabra en %s "%(word,self.language))


class Game():
	"Controlador"
	def __init__(self):
		self.playing = False
		self.menu = Menu()
		self.words = Letters()
		self.enReader = Reader("inglés")
		self.esReader = Reader("castellano")

	def get_randomWord(self):
		"Se comunica con el Modelo"
		return self.words.randomWord()

	def showord(self):
		"Llama a la vista correspondiente de acuerdo al dato obtenido"
		word = self.get_randomWord()
		if word in self.words.Enwords:
			self.enReader.pronounce(word)
		else:
			self.esReader.pronounce(word)
		del(word)

	def start(self):
		self.playing = True
		self.__loopGame()

	def __loopGame(self):
		while self.playing == True:
			
			try:
				receive = self.menu.mainView()
				self.menu.clear()
				if receive == "1" or receive.lower() == "generar":
					self.showord()
				elif receive == "2" or receive.lower() == "ver":
					self.menu.viewWords(self.words.createdWord)
				elif receive == "3" or receive.lower() == "salir":
					self.quit() 
				self.__loopGame()
			except:
				self.quit()


	def quit(self):
		self.playing = False

game = Game()
game.start()

