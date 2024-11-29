from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

class ContadorApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'

  
        self.label = Label(text="Contador")
        self.add_widget(self.label)

        self.input = TextInput(text="0", multiline=False, readonly=True)
        self.add_widget(self.input)

        botoes = BoxLayout(orientation='horizontal')

        self.checkbox = CheckBox()
        botoes.add_widget(self.checkbox)

    
        self.button = Button(text="Clique para incrementar ou decrementar")
        botoes.add_widget(self.button)
        self.button.on_press = self.atualizar_valor
        self.add_widget(botoes)

    def atualizar_valor(self):
        valor_atual = int(self.input.text)
        if self.checkbox.active:
            valor_atual += 1
        else:
            valor_atual -= 1
        self.input.text = str(valor_atual)

class MyApp(App):
    def build(self):
        return ContadorApp()

if __name__ == '__main__':
    MyApp().run()
