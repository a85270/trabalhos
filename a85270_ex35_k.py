from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class JogoAdivinhar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.numero_secreto = str(random.randint(1, 100))

        self.input_secreto = TextInput(multiline=False, password=True, text=self.numero_secreto)
        self.add_widget(self.input_secreto)

        self.input_utilizador = TextInput(multiline=False)
        self.add_widget(self.input_utilizador)

        self.label = Label(text="")
        self.add_widget(self.label)

        bt_adivinhar = Button(text="Adivinhar")
        bt_adivinhar.on_press = self.adivinhar  
        self.add_widget(bt_adivinhar)

    def adivinhar(self):
        palpite = self.input_utilizador.text
        if palpite.isdigit():
            palpite = int(palpite)
            if palpite < int(self.numero_secreto):
                self.label.text = "Ainda não foi desta. Tenta um valor maior"
            elif palpite > int(self.numero_secreto):
                self.label.text = "Ainda não foi desta. Tenta um valor menor"
            else:
                self.label.text = "Parabens!! Acertaste!! "
                self.input_secreto.password = False
        else:
            self.label.text = "Errado! colaca apenas números."

class MyApp(App):
    def build(self):
        return JogoAdivinhar()

if __name__ == '__main__':
    MyApp().run()
