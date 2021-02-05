import platform
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

def dosyaAc():
	pencere.filename =  filedialog.askopenfilename(title = "Dosya Aç",filetypes = (("Metin Dosyaları","*.txt"),("Tüm Dosyalar","*.*"),
																	("Zengin Metin Dosyaları","*.rtf"),
																	("Python Dosyaları","*.py"),
																	("html Dosyaları","*.html"),
																	("Javascript Dosyaları","*.js"),
																	("Php Dosyaları","*.php")))
	if pencere.filename=="":
		pencere.filename=None
	else:
		pencere.title(os.path.basename(pencere.filename) + " - Not Defteri")
		metinKutu.delete(1.0,END) 

		dosya = open(pencere.filename,"r") 
		metinKutu.insert(1.0,dosya.read()) 
		dosya.close()

def yeniDosya():
	pencere.title("İsimsiz - Not Defteri")
	metinKutu.delete(1.0,END)
	pencere.filename=None
	

def dosyaKaydet():
	if pencere.filename == None:
		pencere.filename = filedialog.asksaveasfilename(initialfile='isimsiz.txt', defaultextension=".txt", 
										filetypes=[("Tüm Dosyalar","*.*"), 
										("Metin Dosyaları","*.txt"),
										("Zengin Metin Dosyaları","*.rtf"),
										("Python Dosyaları","*.py"),
										("html Dosyaları","*.html"),
										("Javascript Dosyaları","*.js"),
										("Php Dosyaları","*.php")]) 

		if pencere.filename == "":
			pencere.filename = None
		
		else:
			dosya = open(pencere.filename,"w") 
			dosya.write(metinKutu.get(1.0,END)) 
			dosya.close() 
			 
			pencere.title(os.path.basename(pencere.filename) + " - Not Defteri")
			
	else: 
		dosya = open(pencere.filename,"w") 
		dosya.write(metinKutu.get(1.0,END)) 
		dosya.close() 

def yapistir():
	metinKutu.event_generate('<Control-v>')
	
def kes():
	metinKutu.event_generate('<Control-x>')
	
def kopyala():
	metinKutu.event_generate('<Control-c>')

def kalinYaz():
	metinKutu.tag_add("kln", "sel.first", "sel.last")

def egikYaz():
	metinKutu.tag_add("egk", "sel.first", "sel.last")
	
def hakkinda():
	messagebox.showinfo("Not Defteri","Dios not defteri")
def seç():
        metinKutusu.event_generate('<Control-a>')

pencere=Tk()
pencere.geometry("500x300")
pencere.title("İsimsiz - Not Defteri")
pencere.filename=None

menu=Menu(pencere)
pencere.config(menu=menu)

dosyaMenu = Menu(menu)
menu.add_cascade(label="Dosya", menu=dosyaMenu)
dosyaMenu.add_command(label="Yeni", command=yeniDosya)
dosyaMenu.add_command(label="Aç...", command=dosyaAc)
dosyaMenu.add_command(label="Kaydet", command=dosyaKaydet)
dosyaMenu.add_separator()
dosyaMenu.add_command(label="Kapat", command=pencere.quit)

duzenMenu=Menu(menu)
menu.add_cascade(label="Düzen", menu=duzenMenu)
duzenMenu.add_command(label="Kes", command=kes)
duzenMenu.add_command(label="Kopyala", command=kopyala)
duzenMenu.add_command(label="Yapıştır", command=yapistir)
duzenMenu.add_separator()
duzenMenu.add_command(label="Kalın", command=kalinYaz)
duzenMenu.add_command(label="Eğik", command=egikYaz)
duzenMenu.add_command(label="seç", command=seç)
yardimMenu = Menu(menu)
menu.add_cascade(label="Yardım", menu=yardimMenu)
yardimMenu.add_command(label="Hakkında", command=hakkinda)

yataySb=Scrollbar(pencere, orient=HORIZONTAL)
yataySb.pack(side=BOTTOM, fill= X)

dikeySb=Scrollbar(pencere, orient=VERTICAL)
dikeySb.pack( side = RIGHT, fill = Y )

metinKutu=Text(pencere, width=500, height=300,wrap=NONE, xscrollcommand=yataySb.set, yscrollcommand = dikeySb.set)
metinKutu.config(insertofftime=600, insertontime=1000, insertwidth=5, selectbackground="darkgray", font="Arial 10")
metinKutu.tag_config("kln", font="Arial 10 bold")
metinKutu.tag_config("egk", font="Arial 10 italic")
metinKutu.pack()

dikeySb.config( command=metinKutu.yview)
yataySb.config(command=metinKutu.xview)

pencere.mainloop()

