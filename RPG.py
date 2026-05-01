# Importando Biblioteca
import random

# Dado de Testes
def teste(acao, defesa):
    d20 = random.randint(1, 20)
    if acao.lower() == 'ataque' or acao.lower() == 'especial':
        if d20 > defesa:
            if arma == 'adaga':
                dano = random.randint(1, dado) + Agi
            else:
                dano = random.randint(1, dado) + For
    elif acao.lower() == 'cura':
        if d20 > 12:
            pv += 5

       
# Criação de personagem
input('Bem vindo ao **nome**, um RPG baseado no sistema "Ordem Paranormal". Clique enter para começar a criação de personagem.')
nome = input('Qual o seu nome? ')

while True:
    classe = input('Entre Ocultista (+PE), Combatente (+PV) e Especialista (Armas Táticas), qual é sua classe? ')
    classe = classe.lower()
    if classe == 'ocultista' or classe == 'combatente' or classe == 'especialista':
        break

Vig, For, Int, Agi, Pre = map(int, input('Agora é hora de distribuir seus 4 pontos de atributo entre Vigor (PV), Força (Dano), Intelecto (Dano Mágico), Agilidade (Dano Ágil) e Presença (PE) lembre-se que o máximo de cada atributo é 3. ').split())

while True:
    arma = input('Entre Adaga (Arma Ágil), Espada (Arma Comum) e Marreta (arma tática), qual é sua arma? ')
    arma = arma.lower()
    if arma == 'adaga':
        dado = 4
        break
    elif arma == 'espada':
        dado = 6
        break
    elif arma == 'marreta':
        if classe == 'especialista':
            dado = 8
            break
        else:
            print('Você não tem proficiência em armas táticas, não pode usar um martelo.')


