from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class TextoInvertido(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.input1 = TextInput(multiline=False)
        self.add_widget(self.input1)

        self.input2 = TextInput(multiline=False, readonly=True)
        self.add_widget(self.input2)
        self.input1.bind(text=self.texto)

    def texto(self, instance, value):
        self.input2.text = value[::-1]

class MyApp(App):
    def build(self):
        return TextoInvertido()

if __name__ == '__main__':
    MyApp().run()
