# Importando Biblioteca
import random
import time
import sys

# Funções
def morte():
    while True:
        rec = input('Gostaria de recomeçar? (S/N) ')
        if rec.upper() == 'S':
            print('Se prepare para começar tudo de novo')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.')
            print('')
            time.sleep(2.5)
            stop = False
            break #the code
        elif rec.upper() == 'N':
            print('A sua aventura acabou')
            sys.exit()
        else:
            print('Resposta inválida, responda sim ou não!')

def check():
    if pv <= 0:
        print('')
        print(f'Com um último ataque do {nomeM}, você sente suas forças se esvaindo.')
        print(fraseMM)
        print(fraseMM2)
        print('')
        print(final)
        morte()
        return False
    elif pvM <= 0:
        print(f'Com um último ataque, você finalmente derrota o {nomeM}')
        print(fraseV)
        print(fraseV2)
        print(fraseV3)
        print('')
        return False
    else:
        return True

def monstro(pvF):
        d20 = random.randint(1, 20)
        if d20 + 5 >= esq:
            dano = random.randint(1, dadoM) + 5
            pvF -= dano
            print(f'O {nomeM} carregou sua energia de conhecimento e te acertou com um soco, causando {dano} de dano!')
        else:
            print(f'O {nomeM} foi lento demais, {fraseM}, abrindo a brecha para desviar! ')
        return pvF

def teste(pvF, peF, pvMF):
    if acao.lower() == 'atacar':
        d20 = random.randint(1, 20)
        if arma == 'adaga':
            if d20 + Agi >= defesa:
                dano = random.randint(1, dado) + Agi
                pvMF -= dano
                print(f'Você corta o {nomeM} rapidamente, causando {dano} de dano!')
            else:
                print(f'Seu golpe foi fraco demais, o {nomeM} resiste como se não fosse nada!')
        else:
            if d20 + For >= defesa:
                dano = random.randint(1, dado) + For
                pvMF -= dano
                print(f'Você acerta o {nomeM} com força, causando {dano} de dano!')
            else:
                print(f'Seu golpe foi fraco demais, o {nomeM} resiste como se não fosse nada!')


    elif acao.lower() == 'cura':
            pvc = random.randint(1, 8) + random.randint(1, 8) + 2
            pvF += pvc
            print(f'Richard se aproxima e trata seus ferimentos antes que seja tarde, você recebe +{pvc}!')
            
            
    elif acao.lower() == 'especial':
        if classe == 'combatente':
            peF -= peCost
            if arma == 'adaga':
                dano = random.randint(1, dado) + Agi + 5
                pvMF -= dano
                print(f'Você dilacera o {nomeM} com sua {arma} executando diversos cortes ágeis, causando {dano} de dano no inimigo!')
            else:
                dano = random.randint(1, dado) + For + 5
                pvMF -= dano 
                print(f'Você acerta {nomeM} com sua {arma}, golpeando ele com toda sua força, causando {dano} de dano no inimigo!')
        elif classe == 'especialista':
            peF -= peCost
            if arma == 'adaga':
                dano = random.randint(1, dado) + Agi + random.randint(1, 6)
                pvMF -= dano
            else:
                dano = random.randint(1, dado) + For + random.randint(1, 6)
                pvMF -= dano
            print(f'Você usa sua manobras táticas para se esgueirar até o {nomeM} e atacá-lo com sua {arma}, causando {dano} de dano!')
        elif classe == 'ocultista':
            peF -= peCost
            dano = random.randint(1, 6) + random.randint (1, 6) + random.randint (1, 6)
            pvMF -= dano
            print(f'Você invoca o paranormal, conjurando raios que atacam o {nomeM} de forma agressiva, causando {dano} de dano!')
            if random.randint(1, 20) + Int < 16:
                pvF -= peCost
                print(f'O paranormal é selvagem e agressivo, ao conjurar o ritual ele te ataca antes de ser dominado, causando {peCost} de dano!')
    return pvF, peF, pvMF


# Criação de Personagem
while True:
    input('Bem vindo ao Ordem Salustial, um RPG baseado no sistema "Ordem Paranormal". Clique enter para começar a criação de personagem.')
    print('')  
    stop = True
    while stop:
        print('---= Criação de Personagem =---')
        nome = input('Qual o seu nome? ')
        nome = nome.capitalize()

        while True: 
            classe = input('Entre Ocultista (+PE), Combatente (+PV) e Especialista (Armas Táticas), qual é sua classe? (O/C/E) ')
            if classe.upper() == 'O':
                classe = 'ocultista'
                poder = 'rituais'
                pv = 18
                pe = 16
                peCost = 2
                break #the code
            elif classe.upper() == 'C':
                classe = 'combatente'
                poder = 'punhos rápidos'
                pv = 32
                pe = 8
                peCost = 2
                break #the code
            elif classe.upper() == 'E':
                classe = 'especialista'
                poder = 'instintos e habilidades táticas'
                pv = 25
                pe = 12
                peCost = 2
                break #the code
            else:
                print(f'{classe} não é uma classe válida!')

        while True:
            print('Agora é hora de distribuir seus 7 pontos de atributo entre Vigor (PV), Força (Dano), ' \
            'Intelecto (Dano Mágico), Agilidade (PE + Esquiva), lembre-se que o máximo de cada atributo é 3:')
            time.sleep(0.5)
            Vig = int(input('Vig: '))
            For = int(input('For: '))
            Int = int(input('Int: '))
            Agi = int(input('Agi: '))
            
            soma = Vig + For + Int + Agi
            if soma > 7:
                print('Valores inválidos, seus status excedem o limite de 7 pontos de atributos!')
            elif soma < 7:
                print(f'Valor inválido, ainda existem {7 - soma} pontos a serem distribuidos!')
            elif Vig > 3 or For > 3 or Int > 3 or Agi > 3:
                print('Valor inválido, algum de seus atributos excede o máximo de 3 pontos por atributo!')
            else:
                pv += 4 * Vig
                pe += 4 * Agi
                esq = 10 + Agi
                break #the code

        while True:
            arma = input('Entre Adaga (Arma Ágil), Clava (Arma Simples) e Espada (Arma Tática), qual é sua arma? ')
            arma = arma.lower()
            if arma == 'adaga':
                dado = 4
                break #the code
            elif arma == 'clava':
                dado = 6
                break #the code
            elif arma == 'espada':
                if classe == 'especialista':
                    dado = 8
                    break #the code
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
            rep = input('É assim que você irá começar sua jornada? (S/N) ')
            if rep.upper() == 'S':
                stop = False
                break #the code
            elif rep.upper() == 'N':
                break #the code 
            else:
                print('Resposta inválida, responda S ou N!')


    print('')
    print('---= CAPÍTULO 1: RICHARD =---')                                                                                                                                         
    print(f'Você, um(a) {classe} até que bem reconhecido(a), recebe um alto sinal de elemento do Conhecimento de uma cidade próxima. Você se dirige em alta velocidade até lá e encontra um homem que acaba de se tornar um existido, um homem com nível de exposição ao Paranormal em 100%. O existido continua repetindo o nome "Richard", e você não sabe porque. Você acessa uma enciclopédia de monstros que guarda em seu inventário e descobre que o existido fica sussurando seu antigo nome repetidamente, na tentativa de ser reconhecido, lembrado. Por sorte, você descobre que o existido, só ataca aqueles que o atacam.')
    print()
    time.sleep(1)

    cap1 = True
    while cap1:
        dec1 = (input("Você tem que decidir entre atacá-lo ou esperar por uma chance de salvá-lo. O que você fará? (lutar ou esperar) "))
        if dec1  == 'lutar':
            print('Você decide lutar contra o existido antes de pensar em qualquer possiblidade, não consgue ver aquela criatura tão horrenda na sua frente. Você sente que está se tornando impiedoso, mas que está fazendo a coisa certa!')
            print('')
            print('---= Combate =---')
            combate = True
            round = 1
            defesa = 13
            pvM = 36
            dadoM = 4
            nomeM = 'existido'
            fraseM = 'susurrar o próprio nome o deixa sem fôlego'
            fraseM2 = 'Seus pecados rastejam pelas suas costas e deixam seu golpe mais lento'
            fraseMM = 'Você foi derrotado por um simples existido e se pergunta se realmente era forte'
            fraseMM2 = 'Talvez foi um golpe de azar e você nunca deveria ter ido para aquela cidade'
            fraseV = 'Você se sente satisfeito pelas suas ações, agora todos viverão em paz e tranquilos'
            fraseV2 = 'O povo em volta do incidente aplaude e alguns deles gritam "Bom trabalho!!"'
            fraseV3 = 'Mesmo assim, um leve sentimento cresce em você, o sentimento de que você perdeu algo...'
            
            final = '---= FINAL: Fraco entre os fracos =---'

            while combate:
                print('Rodada:', round)
                print('PV:', pv, '            PV Inimigo:', pvM )
                print('PE:', pe)
                while True:
                    acao = input(f'Você irá "atacar" o {nomeM} ou usar seu golpe "especial"? ')
                    if acao.upper() == 'ESPECIAL' and pe < peCost:
                        print(f'Você não tem os PE necessários para usar seu especial! ({pe}/{peCost})')
                    elif acao.lower() == 'atacar' or acao.lower() == 'especial':
                        print('')
                        pv, pe, pvM = teste(pv, pe, pvM)
                        pv = monstro(pv)
                        time.sleep(2)
                        round += 1
                        print('--------------------------------------')
                        combate = check()
                        break #the code
                    else:
                        print('Ação inválida, escolha atacar ou especial')


        elif dec1 == 'esperar':
            print('Você pensa um pouco no que você vai fazer para tentar ajudar o existido a existir')
            print('Você vê uma senhora com uma vassoura prestes a atacar o existido e uma outra senhora tentando pará-la')
            print('A senhora que está segurando a outra diz:')
            print('-Ele estava saindo da minha casa!! Quem é esse homem e porque eu estava comprando comida pra duas pessoas se eu moro sozinha??')
            print('Você pensa na possibilidade da dona da casa ser mãe do existido. Você decide entrar na casa e procurar alguma coisa que faça a mãe lembrar do seu filho')
            while True:
                dec2 = input('O que você pega? (Gato, foto, cadeiras ou controle) ')
                if dec2.lower() == 'gato' or dec2.lower() == 'cadeiras' or dec2.lower() == 'controle':
                    print('"O que que isso importa agora??", diz a mãe em desespero')
                    print('O existido, já bravo, te dá um ataque por trás e te joga no chão')
                    print('Ele te espanca até a morte sem te dar chance de revidar')
                    print('---= FINAL: Espancado e fracassado =---')
                    cap1 = False
                    morte()
                    break #the code
                elif dec2.lower() == 'foto':  
                    print('Na foto a mãe parece estar segurando um bebê, mas não há nenhum bebê')
                    print('Ao ver a foto, a mãe começa a chorar')
                    print('"Richard", ela diz, enquanto começa a aparecer um bebê na foto.')
                    print('Quando você olha para o existido, toda a energia paranormal de conhecimento começa a ser rejeitada pelo seu corpo e sai voando pelo céu.')
                    print('No lugar do existido, aparece um homem. Richard havia voltado a existir!')
                    print('')
                    print('---= CAPÍTULO 2: EM BREVE =---')
                    cap1 = False
                    break #the code
                else:
                    print('Não tem isso na casa!!')
        else:
            print(f'{dec1} não é uma decisão válida!')
            