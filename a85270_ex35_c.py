from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class TextoInvertido(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.input1 = TextInput(multiline=False,)  
        self.add_widget(self.input1)

        self.input2 = TextInput(multiline=False, readonly= True)
        self.add_widget(self.input2)
        self.input1.bind(text=self.texto)

        self.label = Label()
        self.add_widget(self.label)

    def texto(self, instance, value):
        texto1 = self.input1.text
        self.input2.text = texto1[::-1]  
        texto2 = self.input2.text
        if texto1 == texto2:
            self.label.text = "textos não inversos"
            self.label.color = (1, 0, 0, 1)  
        else:
            self.label.text = "textos inversos"
            self.label.color = (0, 1, 0, 1)  

class MyApp(App):
    def build(self):
        return TextoInvertido()

if __name__ == '__main__':
    MyApp().run()
