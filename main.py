import youtube_dl
import tkinter
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
# # os.getcwd()  # serve a restituire il percorso dello script
#
# # class Toplevel():
# # 	pass
# #
# # finestra = tkinter.Toplevel()
#
# class penillo():
# 	def pene(self, pippo):
# 		print(self)
# 	var = 2
# def ciaone(nome):
# 	print('ciao', nome)
#
# pennello = penillo()
#
#
# # pennello.pene() # non va perché passa alla funzione se stesso come argomento
# # pennello1.pene
#
# pennello.pene('1')
# pennello.pene('2')
# print(pennello.var)
#
# # ciaone() # non va!
# ciaone('Giacomo')
#
# #ciaone('Giacomo', 'Francesco')

# cazzo = StringVar(self)
# cazzo.set('dcdfdfd')
# print(cazzo.get())  # printa dcdfdfd
dizionario = {'titolo': 'url'}
dizionario['titolo'] = 'url'

class = [title, href, [class, title, href, [class, title, href]]]

class Principe(tkinter.Tk):  # prende la classe tkinter.Tk e ne fa una kopia che poi potremo usare
	url = str()

	def __init__(self, parent): # la classe va inizializzata
		tkinter.Tk.__init__(self, parent)
#		self.parent = parent  # prende l'argomento parent dalla funzione init e lo salva in self.parent
		self.initialize()

	def initialize(self):
		self.geometry('930x580')  # Imposto larghezza e altezza
		self.resizable(False, False)  # Rendo impossibile il resize in larghezza e in altezza
		self.config(background='#282c34')
		self.istruz = tkinter.Label(self, background='#282c34', font='Courier 11 bold', foreground='white', text="Write below the title of the song you wish to download from YouTube")
		self.istruz.pack(anchor='w', side='top')
		self.nomino = tkinter.Entry(self, background='#2C323C', foreground='white', width=90, font='Courier 11 bold')
		self.nomino.pack(ipady=5, pady=5, padx=10, anchor='n', side='left')
		self.sercino = tkinter.Button(self, command=self.search_video, background='#2C323C',
		activeforeground='#9aa2b1', foreground='white', font='Courier 11 bold',
		activebackground='#0b0c0e', text='Search', relief='groove'
		)
		self.sercino.pack(side='left', anchor='n', pady=5, padx=16, ipady=1, ipadx=10)

	def search_video(self):
		self.url = self.nomino.get()
		self.query = urllib.request.quote(self.url)
		self.response = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + self.query)
		self.html = self.response.read()
		self.soup = BeautifulSoup(self.html)

		for vid in self.soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
			print('https://www.youtube.com' + vid['href'])
			print(vid['title'])


if __name__ == "__main__":
	feritoia = Principe(None)  # chiama la funzione __init__ in Principe, per cui self sarà finestra, passando None come parent
	feritoia.title('Leech')
	feritoia.mainloop()
