# Importando Biblioteca
import random
import time
import sys

# Funções
def reset():
    while True:
        rec = input('Gostaria de recomeçar? (S/N) ')
        if rec.upper() == 'S':
            print('Se prepare para começar tudo de novo')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.')
            print('')
            time.sleep(1.5)
            break
        elif rec.upper() == 'N':
            input('A sua aventura acabou, até a próxima...')
            sys.exit()
        else:
            print('Resposta inválida, responda S ou N!')

def check(pv, pvM, final):
    if pv <= 0 and pvM <= 0:
        time.sleep(1.5)
        print('Em um momento de pura adrenalina e emoção...')
        time.sleep(0.5)
        print(f'{nome} acerta o pescoço do {nomeM} com sua {arma}, decapitando o monstro!')
        time.sleep(1)
        print('Porém...')
        time.sleep(0.5)
        print(f'{nomeM} usou suas últimas forçar para deferir um golpe final...')
        print(f'{nome} não consegue esquivar a tempo e é morto pelo monstro, mas pelo menos você salvou a cidade, e pode descansar em paz.')
        print('Derrota')
        final = '---= FINAL: Honrado e Derrotado =---'
        reset()
    elif pv <= 0:
        time.sleep(1.5)
        print(f'Com um último ataque do {nomeM}, você sente suas forças se esvaindo.')
        print(fraseMM)
        print(fraseMM2)
        print('')
        print(final)
        reset()
        return False
    elif pvM <= 0:
        time.sleep(1.5)
        print('Em um momento de pura adrenalina e emoção...')
        time.sleep(0.5)
        print(f'{nome}, acerta o pescoço do {nomeM} com sua {arma}, decapitando o monstro!')
        print(fraseV)
        print(fraseV2)
        print(fraseV3)
        print('')
        return False
    else:
        return True

def monstro(pv):
        d20 = random.randint(1, 20)
        if d20 + 5 >= esq:
            dano = random.randint(1, dadoM) + 5
            pv -= dano
            print(f'O {nomeM} carregou o punho com seu elemento de conhecimento e te acertou com um soco, causando {dano} de dano!')
        else:
            print(f'O {nomeM} foi lento demais, {fraseM}, permitindo {nome} desviar do ataque! ')
        return pv

def ataque(pvM):
        d20 = random.randint(1, 20)
        if d20 + atrB >= defesa:
            dano = random.randint(1, dado) + Agi
            pvM -= dano
            if atrB == Agi:
                print(f'Você corta o {nomeM} rapidamente, causando {dano} de dano!')
            else:
                print(f'Você acerta o {nomeM} com força, causando {dano} de dano!')
        else:
            print(f'Seu golpe foi fraco demais, o {nomeM} resiste como se não fosse nada!')
        return pvM

def esquiva(esq, pvM):
    esq += 7
    print(f'{nome} foca em desviar dos golpes do {nomeM}, mas dessa forma não poderá atacar com tanta força...')
    d20 = random.randint(1, 20)
    if d20 + Agi - 2 >= defesa:
        if atrB == Agi:
            dano = random.randint(1, dado) + Agi
            pvM -= dano 
        else:
            dano = random.randint(1, dado - 2)
            pvM -= dano
        print(f'Você desvia com maestria dos golpes do {nomeM} e encontra uma abertura, você ataca rapidamente causando {dano} de dano!')
    else:
            print(f'Você realiza manobras evasivas, mas não encontra uma brecha para atacar o {nomeM}')
    time.sleep(1)
    return esq, pvM
'''
def cura(pv):
        pvc = random.randint(1, 8) + random.randint(1, 8) + 2
        pv += pvc
        print(f'Richard se aproxima e trata seus ferimentos antes que seja tarde, você recebe +{pvc}!')
        return pv
''' 
def especial(pe, pv, pvM):
    if classe == 'combatente':
        pe -= peCost
        if arma == 'adaga':
            dano = random.randint(1, dado) + Agi + 5
            pvM -= dano
            print(f'Você dilacera o {nomeM} com sua {arma} executando diversos cortes ágeis, causando {dano} de dano no inimigo!')
        else:
            dano = random.randint(1, dado) + For + 5
            pvM -= dano 
            print(f'Você acerta {nomeM} com sua {arma}, golpeando ele com toda sua força, causando {dano} de dano no inimigo!')
    
    elif classe == 'especialista':
        pe -= peCost
        if arma == 'adaga':
            dano = random.randint(1, dado) + Agi + random.randint(1, 6)
            pvM -= dano
        else:
            dano = random.randint(1, dado) + For + random.randint(1, 6)
            pvM -= dano
        print(f'Você usa sua manobras táticas para se esgueirar até o {nomeM} e atacá-lo com sua {arma}, causando {dano} de dano!')
    
    elif classe == 'ocultista':
        pe -= peCost
        dano = random.randint(1, 6) + random.randint (1, 6) + random.randint (1, 6)
        pvM -= dano
        print(f'Você invoca o paranormal, conjurando raios que atacam o {nomeM} de forma agressiva, causando {dano} de dano!')
        if random.randint(1, 20) + Int < 16:
            pv -= peCost
            print(f'O paranormal é selvagem e agressivo, ao conjurar o ritual ele te ataca antes de ser dominado, causando {peCost} de dano!')
    return pe, pv, pvM

def luta(combate, rodada, pv, pe, pvM, esq, final):
    while combate:
                print('Rodada:', rodada)
                print('PV:', pv, '            PV Inimigo:', pvM)
                print('PE:', pe)
                while True:
                    acao = input(f'Você irá "atacar" o {nomeM}, usar seu golpe "especial" ou "esquivar" e tentar fazer um contra-ataque? ')
                    if acao.lower() == 'atacar' or acao.lower() == 'especial' or acao.lower() == 'esquivar':
                        print('')
                        if acao.upper() == 'ATACAR':
                            pvM = ataque(pvM)
                        elif acao.upper() == 'ESPECIAL':
                            if pe < peCost:
                                print(f'Você não tem os PE necessários para usar seu especial! ({pe}/{peCost})')
                            else:
                                pe, pv, pvM = especial(pe, pv, pvM)
                        elif acao.upper() == 'ESQUIVAR':
                            esq, pvM = esquiva(esq, pvM) 

                        pv = monstro(pv)
                        if acao.lower() == 'esquivar':
                            esq -= 7
                        time.sleep(2)
                        rodada += 1
                        print('--------------------------------------')
                        combate = check(pv, pvM, final)
                        break

                    else:
                        print('Ação inválida, escolha atacar, especial ou esquivar')
    return pv, pe

# Criação de Personagem
while True:
    input('Bem vindo ao Ordem Salustial, um RPG baseado no sistema de RPG "Ordem Paranormal". Clique enter para começar a criação de personagem.')
    print('')
    criacao = True
    while criacao:
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
                break
            elif classe.upper() == 'C':
                classe = 'combatente'
                poder = 'punhos rápidos'
                pv = 32
                pe = 8
                peCost = 2
                break
            elif classe.upper() == 'E':
                classe = 'especialista'
                poder = 'instintos e habilidades táticas'
                pv = 25
                pe = 12
                peCost = 2
                break
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
            elif Vig < 0 or For < 0 or Int < 0 or Agi < 0:
                print('Valor inválido, algum de seus atributos não atende o mínimo de 0 pontos!')
            else:
                pv += 4 * Vig
                pe += 4 * Agi
                esq = 10 + Agi
                break

        while True:
            arma = input('Entre Adaga (Arma Ágil), Clava (Arma Simples) e Espada (Arma Tática), qual é sua arma? ')
            arma = arma.lower()
            if arma == 'adaga':
                atrB = Agi
                dado = 4
                break
            elif arma == 'clava':
                atrB = For
                dado = 6
                break
            elif arma == 'espada':
                if classe == 'especialista':
                    atrB = For
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
            rep = input('É assim que você irá começar sua jornada? (S/N) ')
            if rep.upper() == 'S':
                criacao = False
                break
            elif rep.upper() == 'N':
                break 
            else:
                print('Resposta inválida, responda S ou N!')

    print('')
    print('---= CAPÍTULO 1: RICHARD =---')                                                                                                                                         
    input(f'Você, um(a) {classe} até que bem reconhecido(a), recebe um alto sinal de elemento do Conhecimento de uma cidade próxima. Você se dirige em alta velocidade até lá e encontra um homem que acaba de se tornar um existido, um ser humano com nível de exposição ao Paranormal em 100%. (enter para continuar)')
    input('O existido continua repetindo o nome "Richard", e você não sabe porque. Você acessa uma enciclopédia de monstros que guarda em seu inventário e descobre que o existido fica sussurrando seu antigo nome repetidamente, na tentativa de ser reconhecido, lembrado. Por sorte, você descobre que o existido, só ataca aqueles que o atacam. (enter para continuar)')

    cap1 = True
    while cap1:
        dec1 = (input("Você tem que decidir entre atacá-lo ou esperar por uma chance de salvá-lo. O que você fará? (lutar ou esperar) "))
        if dec1  == 'lutar':
            print('Você decide lutar contra o existido antes de pensar em qualquer possiblidade, não consgue ver aquela criatura tão horrenda na sua frente. Você sente que está se tornando impiedoso, mas que está fazendo a coisa certa, você precisa restaurar a membrana!')
            print('')
            print('---= Combate =---')
            defesa = 13
            pvM = 36
            dadoM = 4
           
            nomeM = 'existido'
            fraseM = 'sussurrar o próprio nome o deixa sem fôlego'
            fraseM2 = 'Seus pecados rastejam pelas suas costas e deixam seu golpe mais lento'
            fraseMM = 'Você foi derrotado por um simples existido e se pergunta se realmente era forte'
            fraseMM2 = 'Talvez tenha sido azar, ou talvez você nunca deveria ter ido àquela cidade'
            fraseV = 'Você se sente satisfeito pelas suas ações, agora todos viverão em paz e tranquilos'
            fraseV2 = 'O povo em volta do incidente aplaude e alguns deles gritam "Bom trabalho!!"'
            fraseV3 = 'Mesmo assim, um leve sentimento cresce em você, o sentimento de que você perdeu algo...'
            final = '---= FINAL: Fraco Entre os Fracos =---'

            pv, pe = luta(True, 1, pv, pe, pvM, esq, final)

            cap1 = False
            if pv > 0:
                print('Vitória')
                input('---= CAPÍTULO 2: EM BREVE =---')
                reset()

        elif dec1 == 'esperar':
            print('')
            input('Você pensa um pouco no que você vai fazer para tentar ajudar o existido a existir. (enter para continuar)')
            input('Você vê uma senhora com uma vassoura prestes a atacar o existido e uma outra senhora tentando pará-la... (enter para continuar)')
            print('A senhora que está segurando a outra diz:')
            input('-Ele estava saindo da minha casa!! Quem é esse homem e porque eu estava comprando comida pra duas pessoas se eu moro sozinha?? (enter para continuar)')
            input('Você pensa na possibilidade da dona da casa ser mãe do existido. Você decide entrar na casa e procurar algo que faça a mãe lembrar do seu filho... (enter para continuar)')
            print('')
            dec2 = input('Dentro da moradia, você vê alguns itens que podem ser úteis para o seu objetivo: \n A "mesa" de jantar, com cadeiras, pratos, e comida o bastante para 2 pessoas, mas somente a mãe presente; \n Um "gato", que parece inquieto, procurando seu dono, ignorando a presença da senhora; \n Um "controle" de videogame desgastado, como se tivesse sido utilizado frequentemente por muito tempo, mas não parece que a senhora foi a usuária; \n Uma "foto" com apenas a imagem da mãe, ela parece estar segurando algo, mas é impossível identificar o que é; \n Qual você investiga? ')
            while True: 
                if dec2.lower() == 'mesa' or dec2.lower() == 'gato' or dec2.lower() == 'controle' or dec2.lower() == 'foto':
                    print('')
                    if dec2.lower() == 'mesa' or dec2.lower() == 'gato' or dec2.lower() == 'controle':
                        if dec2.lower() == 'mesa':
                            print(f'{nome} começa a investigar mesa, mas o existido percebe e fica muito irritado...')
                            time.sleep(1.5)
                            print('Ele solta um clarão, que te deixa tonto, o derrubando no chão...')
                            time.sleep(1.5)
                            print('Ele te espanca, sem dó nem piedade, até a morte, sem te dar chance de revidar...')
                            time.sleep(1.5)
                            print('Enquanto espera o seu fim, uma frase se repete em sua mente, é o existido falando com você por meio do elemento do conhecimento:')
                            time.sleep(1.5)
                            print('"ESSA COMIDA É MINHA!!!"')

                        elif dec2.lower() == 'gato':
                            print(f'{nome} se aproxima do gato estendendo a mão, oferecendo carinho, mas ao observar, o existido fica furioso...')
                            time.sleep(1.5)
                            print('Ele solta um clarão, que te deixa tonto, o derrubando no chão...')
                            time.sleep(1.5)
                            print('Ele te espanca, sem dó nem piedade, até a morte, sem te dar chance de revidar...')
                            time.sleep(1.5)
                            print('Enquanto espera o seu fim, uma frase se repete em sua mente, é o existido falando com você por meio do elemento do conhecimento:')
                            time.sleep(1.5)
                            print('"NÃO TOCA NO GARFIELD!!!"')

                        elif dec2.lower() == 'controle':
                            print(f'{nome} pega o controle, tentando observar mais claramente, mas ao avistá-lo, o existido fica enraivecido...')
                            time.sleep(1.5)
                            print('Ele solta um clarão, que te deixa tonto, o derrubando no chão...')
                            time.sleep(1.5)
                            print('Ele te espanca, sem dó nem piedade, até a morte, sem te dar chance de revidar...')
                            time.sleep(1.5)
                            print('Enquanto espera o seu fim, uma frase se repete em sua mente, é o existido falando com você por meio do elemento do conhecimento:')
                            time.sleep(1.5)
                            print('"NÃO OUSE DELETAR MEU SAVE!!!"')
                        print('')
                        time.sleep(2)
                        print('Derrota')
                        final = '---= FINAL: Espancado e Fracassado =---'
                        print(final)
                        reset()
                    else:
                        print('Ao ver a foto, a senhora começa a chorar...')
                        time.sleep(1.5)
                        print('"Richard", ela diz, enquanto começa a aparecer um bebê na foto, no colo da mãe.')
                        time.sleep(1.5)
                        print('Quando você olha para o existido, todo o elemento paranormal de conhecimento começa a ser rejeitado pelo seu corpo e sai voando pelo céu.')
                        time.sleep(1.5)
                        print('No lugar do existido, aparece um homem. Richard havia voltado a existir!')
                        print('')
                        time.sleep(2)
                        print('Vitória')
                        print('---= CAPÍTULO 2: EM BREVE =---')
                        reset()
                    cap1 = False
                    break
                else:
                    print('Não tem isso na casa!!!')
                    dec2 = input('Qual você investiga? (Mesa, Gato, Controle ou Foto) ')
        else:
            print(f'{dec1} não é uma decisão válida!')
