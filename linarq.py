#!/usr/bin/env python
from Tkinter import *
import time
import pygtk
import gtk
import pango

# La clase Base contendra los atributos por defecto de nuestra interfaz
class Base: 

	# Establece que al cerrar la ventana se detenga el script python
	def destroy(self, widget, data=None):
		gtk.main_quit()
		print("Close App")
	
	# Establece los parametros de configuracion de la ventana y la muestra
	def __init__(self):
	#	tk.Tk.__init__(self)
		# Ventana siempre al frente
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		# Ventana siempre al centro
		#self.window.set_position(gtk.WIN_POS_CENTER)
		
		# Reloj en la ventana
		self.labelTime = gtk.Label()
		#self.window.add(self.label)
		#self.window.set_border_width(25)
		
		# Tamano de ventana
		#self.window.fullscreen()
		self.window.set_size_request(800,480)		

		# Imagen de fondo
		def draw_pixbuf(widget, event):
        		path = 'logolinar.png'
        		pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        		widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0, 15)

		def togglebutton1(widget, data=None):
			if widget.get_active():
				print("Hola")
			else:
				print("Chao")

		def togglebutton2(widget, data=None):
			if widget.get_active():
				print("Hola")
			else:
				print("Chao")


		# Para controlar los espacios por cajas
		#self.box1 = gtk.HBox()
		#self.box1.pack_start(self.button1)
		#self.box1.pack_start(self.labelTime)
		#self.box1.connect("expose-event", draw_pixbuf)
		#self.window.add(self.box1)

		# images are of an up and down button
	        # pick GIF images you have in the working directory or give full path
        	#self.image_up = tk.PhotoImage(file='luzon.png')
        	#self.image_down = tk.PhotoImage(file='luzoff.png')
        	#self.images = it.cycle([self.image_down, self.image_up])
        	#self.button2 = tk.Button(self, image=self.image_up, command=self.toggle)
        	#self.button2.pack()
    		
		# Botones en la ventana
		image2 = gtk.Image()
		image2.set_from_file("luzon2.png")
		image2.set_size_request(100,100)
		image2.show()

		self.button1 = gtk.ToggleButton()
		self.button1.add(image2)
		self.button1.connect("toggled", togglebutton1) 

		
		# Boton 2 
		image3 = gtk.Image()
		image3.set_from_file("tomaon2.png")
		image3.set_size_request(100,100)
		image3.show()

		self.button2 = gtk.ToggleButton()
		self.button2.add(image3)
		self.button2.connect("toggled", togglebutton2) 
		
		
		# Para controlar los espacios por posicion X,Y
		fixed = gtk.Fixed()
		fixed.put(self.button1, 450, 30)
		fixed.put(self.button2, 580, 30)
		fixed.put(self.labelTime, 430, 360)
		fixed.connect("expose-event", draw_pixbuf)
		self.window.add(fixed)

		# Mostrar todo el contenido establecido con anterioridad
		self.window.show_all()
		self.window.connect('destroy', self.destroy)
	

	# Metodo para la actualizacion del reloj digital
	def update(self):
		textTime = time.strftime('%I:%M:%S %p')
		#textTime = time.strftime('%H:%M:%S')
		self.labelTime.set_markup('<span foreground="#191919" size="30000"><b> %s </b></span>' % textTime)
		return True  
			
	def main(self):
		gtk.main()
		

if __name__ == '__main__':
	base = Base()
	gtk.timeout_add(200, base.update)  #Cada 200 ms actualiza el label
	print("Open App")
	base.main()

