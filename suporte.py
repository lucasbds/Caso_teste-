class Suporte:
    def __init__(self, nome, chamado_aberto=0):
        self.nome = nome
        self.chamado_aberto = chamado_aberto

    def abrir_chamado(self):
        self.chamado_aberto += 1

    def fechar_chamado(self):
        self.chamado_aberto -= 1
