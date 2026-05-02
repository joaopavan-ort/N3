# Importando Biblioteca
import random
import time
import sys

# Funções
def morte():
    while True:
        rec = input('Gostaria de recomeçar?')
        if rec.lower() == 'sim':
            print('Se prepare para começar tudo de novo')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(2.5)
            stop = False
        elif rec.lower() == 'não':
            print('A sua aventura acabou')
            sys.exit()
        else:
            print('Resposta inválida, responda sim ou não!')

def monstro():
        d20 = random.randint(1, 20)
        if d20 + 5 >= esq:
            dano = random.randint(1, dadoM) + 5
            pv -= dano
        else:
            print(f'O {nomeM} foi lento demais, {fraseM} ')


def teste():
    if acao.lower() == 'ataque':
        d20 = random.randint(1, 20)
        if arma == 'adaga':
            if d20 + Agi >= defesa:
                dano = random.randint(1, dado) + Agi
                pvm -= dano
            else:
                print(f'Seu golpe foi fraco demais, o {nomeM} resiste como se não fosse nada!')
        else:
            if d20 + For >= defesa:
                dano = random.randint(1, dado) + For
                pvm -= dano
            else:
                print(f' o inimigo esquivou!')
    elif acao.lower() == 'cura':
            pv += random.randint(1, 8) + random.randint(1, 8) + 2
    elif acao.lower() == 'especial':
        if classe == 'combatente':
            pe -= 2 
            if arma == 'adaga':
                dano = random.randint(1, dado) + Agi + 5
                pvm -= dano
            else:
                dano = random.randint(1, dado) + For + 5
                pvm -= dano 
        elif classe == 'especialista':
            pe -= 1
            if arma == 'adaga':
                dano = random.randint(1, dado) + Agi + random.randint(1, 6)
                pvm -= dano
            else:
                dano = random.randint(1, dado) + For + random.randint(1, 6)
                pvm -= dano
        elif classe == 'ocultista':
            pe -= 1
            dano = random.randint(1, 6) + random.randint (1, 6) + random.randint (1, 6)
            if random.randint(1, 20) + Agi < 16:
                pv -= 1


# Criação de Personagem
while True:
    input('Bem vindo ao **Ordem Salustial**, um RPG baseado no sistema "Ordem Paranormal". Clique enter para começar a criação de personagem.')
    print('')  
    stop = True
    while stop:
        print('---= Criação de Personagem =---')
        nome = input('Qual o seu nome? ')
        nome = nome.capitalize()

        while True: 
            classe = input('Entre Ocultista (+PE), Combatente (+PV) e Especialista (Armas Táticas), qual é sua classe? ')
            classe = classe.lower()
            if classe == 'ocultista':
                poder = 'rituais'
                pv = 18
                pe = 16
                break
            elif classe == 'combatente':
                poder = 'punhos rápidos'
                pv = 32
                pe = 8
                break
            elif classe == 'especialista':
                poder = 'instintos e habilidades táticas'
                pv = 25
                pe = 12
                break
            else:
                print(f'{classe} não é uma classe válida!')

        while True:
            Vig, For, Int, Agi = map(int, input('Agora é hora de distribuir seus 7 pontos de atributo entre Vigor (PV), ' \
            'Força (Dano), Intelecto (Dano Mágico), Agilidade (PE + Esquiva), lembre-se que o máximo de cada atributo é 3. ').split())
            soma = Vig + For + Int + Agi
            if soma > 7:
                print('Valores inválidos, seus status excedem o limite de 7 pontos de atributos!')
            elif soma < 7:
                print(f'Valor inválido, ainda existem {7 - soma} pontos a serem distribuidos!')
            elif Vig > 3 or For > 3 or Int > 3 or Agi > 3:
                print('Valor inválido, algum de seus atributos excede o máximo de 3 pontos por atributo!')
            else:
                pv += 4 * Vig
                pe = 4 * Agi
                esq = 10 + Agi
                break

        while True:
            arma = input('Entre Adaga (Arma Ágil), Clava (Arma Simples) e Espada (Arma Tática), qual é sua arma? ')
            arma = arma.lower()
            if arma == 'adaga':
                dado = 4
                break
            elif arma == 'clava':
                dado = 6
                break
            elif arma == 'espada':
                if classe == 'especialista':
                    dado = 8
                    break
                else:
                    print('Você não tem proficiência em armas táticas, não pode usar uma espada.')
            else:
                print(f'{arma} não é uma arma válida!')

        print('')
        print('---= Sua Ficha =---')
        print(f'{nome}, um(a) {classe} que luta com seus {poder} e sua {arma} implacável!')
        print('PV:', pv)
        print('PE:', pe)
        print('Esquiva:', esq)

        while True:
            rep = input('É assim que você irá começar sua jornada? ')
            if rep.lower() == 'sim':
                stop = False
                break
            elif rep.lower() == 'não':
                break 
            else:
                print('Resposta inválida, responda sim ou não!')


    print('')
    print('---= CAPÍTULO 1: RICHARD =---')                                                                                                                                         
    print(f'Você, um(a) {classe} até que bem reconhecido(a), recebe um alto sinal de elemento do Conhecimento de uma cidade próxima. Você se dirige em alta velocidade até lá e encontra um homem que acaba de se tornar um existido, um homem que foi exposto a 100% do Paranormal. O existido continua repetindo o nome "Richard", e você não sabe porque. Você acessa uma enciclopédia de monstros que guarda com você. Você descobre que o existido fica repetindo seu antigo nome na tentativa de ser reconhecido, lembrado. Por sorte, você descobre que o existido só ataca aqueles que os atacam.')
    dec1 = (input("Você tem que decidir entre atacá-lo ou esperar por uma chance de salvá-lo. O que você fará(atacar ou esperar)?"))

    while True:
        if dec1  == 'atacar':
            print('')
            print(f'Você decide atacar o existido antes de pensar em qualquer coisa, não consgue ver aquela coisa tão horrenda na sua frente. Você sente que está ficando impiedoso, mas que está fazendo a coisa certa')
            print('')
            print('---= Combate =---')
            defesa = 13
            pvm = 36
            dadoM = 4
            nomeM = 'existido'
            fraseM = 'susurrar o próprio nome o deixa sem fôlego...'
            fraseM2 = 'Seus pecados rastejam pelas suas costas e deixam seu golpe mais lento'
            

            while True:
                acao = input('atacar ou especial')
                if acao.lower() == 'atacar' or acao.lower() == 'especial':
                    teste()
                    monstro()
                    break
                else:
                    print('Ação inválida, escolha atacar ou especial')

            if pv <= 0:
                print('Você foi derrotado.')
                morte()
            elif pvm <= 0:
                print('Você mata o existido')
            else:
                print('Você resiste, PV:', pv)


        elif dec1 == 'esperar':
            print('Você pensa um pouco no que você vai fazer para tentar ajudar o existido a existir')
            print('Você vê uma senhora com uma vassoura prestes a atacar o existido e uma outra senhora tentando pará-la')
            print('A senhora que está segurando a outra diz:')
            print('-Ele estava saindo da minha casa!! Quem é esse homem e porque eu estava comprando comida pra duas pessoas se eu moro sozinha??')
            print('Você pensa na possibilidade da dona da casa ser mãe do existido. Você decide entrar na casa e procurar alguma coisa que faça a mãe lembrar do seu filho')
            while True:
                dec2 = input('O que você pega(Gato, foto, cadeiras ou controle)')
                if dec2.lower() == 'gato' or dec2.lower() == 'cadeiras' or dec2.lower() == 'controle':
                    print('"O que que isso importa agora??", diz a mãe em desespero')
                    print('O existido, já bravo, te dá um ataque por trás e te joga no chão')
                    print('Ele te espanca até a morte sem te dar chance de revidar')
                    print('FINAL: Espancado e fracassado')
                    morte()
                    break
                elif dec2.lower() == 'foto':  
                    print('Na foto a mãe parece estar segurando um bebê, mas não há nenhum bebê')
                    print('Ao ver a foto, a mãe começa a chorar')
                    print('"Richard", ela diz, enquanto começa a aparecer um bebê na foto.')
                    print('Quando você olha para o existido, toda a energia de conhecimento começa a ser rejeitada pelo corpo do existido e sai voando pelo céu')
                    print('No lugar do existido, aparece um homem. Richard havia voltado a existir')
                    break
                else:
                    print('Não tem isso na casa!!')
            break
        else:
            print(f'{dec1} não é uma decisão válida!')
    print('---= CAPÍTULO 2: EM BREVE =---')
    break
    

