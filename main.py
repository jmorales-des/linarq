from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

import time 	


class RelojSimple(Label):
    
    def update(self, *args):
        self.text = time.asctime()

class DatosUsuario(GridLayout):

    def __init__(self, **kwargs):
        Window.borderless = True
        super(DatosUsuario, self).__init__(**kwargs)
        self.rows = 3
        relojSimple = RelojSimple()
        Clock.schedule_interval(relojSimple.update, 1)
        boton = Button(text='Exit',size_hint=(None, None))
        boton.bind(on_press=exit)
        self.add_widget(relojSimple)
        self.add_widget(boton)
        self.add_widget(Label(text='Nombre'))
        self.nombre = TextInput(multiline=False)
        self.add_widget(self.nombre)
        self.add_widget(Label(text='Cedula'))
        self.cedula = TextInput(multiline=False)
        self.add_widget(self.cedula)


class MyApp(App):

    def build(self):
        return DatosUsuario()


if __name__ == '__main__':
    MyApp().run()
