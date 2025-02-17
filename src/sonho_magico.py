class SonhoMagico:
    def __init__(self, cor, poder_especial):
        self.cor = cor
        self.poder_especial = poder_especial
        self.nivel_magia = 1
    
    def aumentar_magia(self):
        self.nivel_magia += 1
        print(f'Nível de magia aumentou para {self.nivel_magia}!')
    
    def brilhar(self):
        print(f'O sonho {self.cor} está brilhando com {self.poder_especial}!')
    
    def compartilhar(self):
        print(f'Compartilhando o poder de {self.poder_especial} com outros sonhos!')


class SonhoAventura(SonhoMagico):
    def __init__(self, cor, poder_especial, local_aventura):
        super().__init__(cor, poder_especial)
        self.local_aventura = local_aventura
    
    def explorar(self):
        print(f'Explorando {self.local_aventura} com {self.poder_especial}!')
    
    def criar_missao(self):
        print(f'Nova missão criada em {self.local_aventura}!')