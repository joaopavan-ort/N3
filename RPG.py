# Importando Biblioteca
import random

# Dado de Testes
d20 = random.randint(1, 20)

# Criação de personagem
input('Bem vindo ao **nome**, um RPG baseado no sistema "Ordem Paranormal". Clique enter para começar a criação de personagem.')
nome = input('Qual o seu nome? ')

while True:
    classe = input('Entre Ocultista (+PE), Combatente (+PV) e Especialista (Armas Táticas), qual é sua classe? ')
    if classe.upper() == 'OCULTISTA' or classe.upper() == 'COMBATENTE' or classe.upper() == 'ESPECIALISTA':
        break

Vig, For, Int, Agi, Pre = map(int, input('Agora é hora de distribuir seus 4 pontos de atributo entre Vigor (PV), Força (Dano), Intelecto (Dano Mágico), Agilidade (Dano Ágil) e Presença (PE) lembre-se que o máximo de cada atributo é 3. ').split())

while True:
    arma = input('Entre Adaga (Arma Ágil), Espada (Arma Comum) e Martelo (arma tática), qual é sua arma? ')
    if arma.upper() == 'ADAGA' or arma.upper() == 'ESPADA' or arma.upper() == 'MARTELO':
        break


