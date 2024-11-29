from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TrocaTexto(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        boxlayout = BoxLayout()
        boxlayout.orientation = "vertical"

        self.input1 = TextInput(multiline=False)
        self.add_widget(self.input1)

        self.input2 = TextInput(multiline=False)
        self.add_widget(self.input2)

        bt_troca = Button(text="Trocar")
        bt_troca.on_press = self.trocar_texto
        self.add_widget(bt_troca)


    def trocar_texto(self):
        troca = self.input1.text
        self.input1.text = self.input2.text
        self.input2.text = troca

class MyApp(App):
    def build(self):
        return TrocaTexto()

if __name__ == '__main__':
    MyApp().run()
