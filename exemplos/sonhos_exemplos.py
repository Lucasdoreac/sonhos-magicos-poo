from src.sonho_magico import SonhoMagico, SonhoAventura

# Criando diferentes tipos de sonhos mágicos
sonho_voador = SonhoMagico('azul', 'voar alto')
sonho_voador.brilhar()
sonho_voador.aumentar_magia()
sonho_voador.compartilhar()

# Criando uma aventura mágica
aventura_floresta = SonhoAventura('verde', 'falar com animais', 'Floresta Encantada')
aventura_floresta.explorar()
aventura_floresta.criar_missao()
aventura_floresta.brilhar()  # Herda métodos da classe pai

# Criando múltiplos sonhos para uma história
sonho_musical = SonhoMagico('dourado', 'criar melodias')
sonho_artista = SonhoMagico('roxo', 'pintar o céu')

# Fazendo os sonhos interagirem
sonho_musical.brilhar()
sonho_artista.aumentar_magia()
sonho_musical.compartilhar()
sonho_artista.compartilhar()

# Exemplo de uma pequena história com os sonhos
print("\nUma História Mágica:")
print("-------------------")
print(f"Era uma vez um sonho {sonho_musical.cor} que adorava {sonho_musical.poder_especial}...")
print(f"Ele encontrou um sonho {sonho_artista.cor} que podia {sonho_artista.poder_especial}...")
print("Juntos, eles criaram uma sinfonia de cores no céu!")