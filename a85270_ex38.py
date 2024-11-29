from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class jogo_galo(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'


        self.status = Label(text='Joga o jogador:   X', halign='center', valign='middle', size_hint=(1, 0.1))
        self.resultado_label = Label(text='Pontuação:           X - 0          O - 0', halign='center', valign='middle', size_hint=(1, 0.1))
        self.add_widget(self.status)
        self.add_widget(self.resultado_label)


        self.tabuleiro_layout = GridLayout(cols=3)
        self.tabuleiro = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = Button(font_size=65)
                self.tabuleiro[i][j].bind(on_release=self.clicar)
                self.tabuleiro_layout.add_widget(self.tabuleiro[i][j])
        self.add_widget(self.tabuleiro_layout)


        self.control_layout = BoxLayout(size_hint=(1, 0.1))
        self.reinicia_button = Button(text='Reiniciar', on_release=self.reinicia)
        self.sair_button = Button(text='Sair', on_release=self.sair)
        self.control_layout.add_widget(self.reinicia_button)
        self.control_layout.add_widget(self.sair_button)
        self.add_widget(self.control_layout)


        self.jogador = 'X'
        self.resultado = {'X': 0, 'O': 0}

    def clicar(self, button):
        if button.text == '':
            button.text = self.jogador
            button.disabled = True
            vencedor= self.verifica_vencedor()
            if vencedor:
                self.status.text = f'Jogador {vencedor} ganhou!'
                self.resultado[vencedor] += 1
                self.resultado_label.text = f'Pontuação: X - {self.resultado["X"]}, O - {self.resultado["O"]}'
                self.reiniciar_tabuleiro()
            else:
                self.jogador = 'O' if self.jogador == 'X' else 'X'
                self.status.text = f'Vez do jogador: {self.jogador}'

    def verifica_vencedor(self):
        for i in range(3):
            if self.tabuleiro[i][0].text == self.tabuleiro[i][1].text == self.tabuleiro[i][2].text != '':
                return self.tabuleiro[i][0].text
        for i in range(3):
            if self.tabuleiro[0][i].text == self.tabuleiro[1][i].text == self.tabuleiro[2][i].text != '':
                return self.tabuleiro[0][i].text
        if self.tabuleiro[0][0].text == self.tabuleiro[1][1].text == self.tabuleiro[2][2].text != '':
            return self.tabuleiro[0][0].text
        if self.tabuleiro[0][2].text == self.tabuleiro[1][1].text == self.tabuleiro[2][0].text != '':
            return self.tabuleiro[0][2].text
        return None

    def reiniciar_tabuleiro(self):
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j].text = ''
                self.tabuleiro[i][j].disabled = False

    def reinicia(self):
        self.reiniciar_tabuleiro()
        self.jogador = 'X'
        self.status.text = f'Vez do jogador: {self.jogador}'

    def sair(self):
        App.get_running_app().stop()

class MyApp(App):

    def build(self):
        return jogo_galo()

if __name__ == '__main__':
    MyApp().run()
