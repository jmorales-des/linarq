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
		# Ventana siempre al frente
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		# Ventana siempre al centro
		#self.window.set_position(gtk.WIN_POS_CENTER)
		
		# Reloj en la ventana
		self.labelTime = gtk.Label()
		#self.window.add(self.label)
		#self.window.set_border_width(25)
		
		# Tamano de ventana
		self.window.fullscreen()
		
		# Botones en la ventana
		self.button1 =  gtk.Button("EXIT")
		self.button1.connect("clicked", self.destroy) 
		
		# Imagen de fondo
		def draw_pixbuf(widget, event):
        		path = 'main.jpg'
        		pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        		widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0, 15)

		# Para controlar los espacios por cajas
		self.box1 = gtk.HButtonBox()
		#self.box1.pack_start(self.button1)
		self.box1.pack_start(self.labelTime)
		self.box1.connect("expose-event", draw_pixbuf)
		self.window.add(self.box1)
				
		# Para controlar los espacios por posicion X,Y
		#fixed = gtk.Fixed()
		#fixed.put(self.button1, 20, 30)
		#fixed.put(self.labelTime, 300, 40)

		# Mostrar todo el contenido establecido con anterioridad
		self.window.show_all()
		self.window.connect('destroy', self.destroy)

	# Metodo para la actualizacion del reloj digital
	def update(self):
		textTime = time.strftime('%H:%M:%S')
		self.labelTime.set_markup('<span foreground="white" size="30000"><b> %s </b></span>' % textTime)
		return True  
			
	def main(self):
		gtk.main()

if __name__ == '__main__':
	base = Base()
	gtk.timeout_add(200, base.update)  #Cada 200 ms actualiza el label
	print("Open App")
	base.main()

