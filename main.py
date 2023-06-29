import random
import os
import copy
import getch
import math
# O Conclave Tenebroso: Zumbi Contra a Sombra do Império
# CT:ZCSI


def clear():
    if os.name == 'posix':  # unix
        os.system('clear')
    elif os.name == 'nt':  # win
        os.system('cls')


def menu(options, icons, functions, intro):
    current = 0
    while True:
        clear()
        print(
            "\033[33m♔\033[0m  O Conclave Tenebroso: Zumbi Contra a Sombra do Império  \033[33m♔\n\033[0m")
        print(intro)
        for i in range(len(options)):
            if i == current:
                print('☞ \033[47m\033[30m' + icons[i] +
                      "\033[47m\033[30m" + options[i] + "\033[0m")
            else:
                print('  ' + icons[i] + options[i] + "\033[0m")

        key = getch.getch()
        if key == '\n':
            return functions[current]()
        elif key == '\x1b':
            getch.getch()  # Skip the [
            arrow_key = getch.getch()
            if arrow_key == 'A' and current > 0:  # up
                current -= 1
            elif arrow_key == 'B' and current < len(options):  # down
                current += 1


def facil():
    return 32


def normal():
    return 16


def dificil():
    return 8


def tenebroso():
    return 4


def pequeno():
    return 8


def grande():
    return 32


def enorme():
    return 64


def monstruoso():
    return 128


def colossal():
    return 128


def mundo():
    return 128


dificuldade = menu([' facil', ' normal', ' dificil', ' tenebroso', "sair"],
                   ['\033[32m♟\033[0m', "\033[36m♜\033[0m",
                       "\033[33m♞\033[0m", "\033[31m☠\033[0m", ''],
                   [facil, normal, dificil, tenebroso, exit],
                   "Use as setas do teclado e enter para selecionar uma dificuldade:\n")

map_size = menu(['pequeno', 'normal', 'grande', "enorme", "monstruoso", "colossal", "mundo" "sair"],
                ['', '', '', '', '', '', '', '', ''],
                [pequeno, normal, grande, enorme,
                    monstruoso, colossal, mundo, exit],
                "Use as setas do teclado e enter para selecionar uma tamanho para o mapa:\n")


def maprint():
    clear()
    map = copy.deepcopy(emptymap)
    for i in range(1, len(creatures)):
        map[creatures[i]['x']][creatures[i]['y']] = pecas[creatures[i]['cor']][
            creatures[i]['type']]

    if creatures[0]['alive'] == True:
        map[creatures[0]['x']][creatures[0]['y']] = pecas[creatures[0]['cor']][
            creatures[0]['type']]
    else:
        map[creatures[0]["x"]][creatures[0]["y"]
                               ] = '\033[31m' + "☠" + "\033[0m"

    for x in range(map_size):
        for y in range(map_size):
            if map[x][y] == '♕':
                print('\033[33m' + map[x][y] + "\033[0m", end='')
            elif map[x][y] == '♖':
                print('\033[34m' + map[x][y] + "\033[0m", end='')
            elif map[x][y] == '♗':
                print('\033[35m' + map[x][y] + "\033[0m", end='')
            elif map[x][y] == '♘':
                print('\033[36m' + map[x][y] + "\033[0m", end='')
            elif map[x][y] == '♙':
                print('\033[34m' + map[x][y] + "\033[0m", end='')
            elif map[x][y] == '♟':
                print('\033[31m' + map[x][y] + "\033[0m", end='')
            else:
                print(map[x][y], end='')

        print("")


pecas = {
    "preto": {
        "rainha": "♛",
        "rei": "♚",
        "torre": "♜",
        "bispo": "♝",
        "cavalo": "♞",
        "peao": "♟"
    },
    "branco": {
        "rainha": "♕",
        "rei": "♔",
        "torre": "♖",
        "bispo": "♗",
        "cavalo": "♘",
        "peao": "♙"
    },
    "names": ["rainha", "rei", "torre", "bispo", "cavalo", "peao"]
}

ia = {}


def move(creature, position):
    for i in range(len(creatures)):
        if creatures[i]['x'] == position['x'] and creatures[i]['y'] == position['y']:
            if i == 0:
                creatures[0]['alive'] = False
            else:
                return False
    creature['x'] = position['x']
    creature['y'] = position['y']
    return True


def iapeao(creature):
    destiny = {}
    destiny['x'] = creature['x']
    destiny['y'] = creature['y']
    if creature['y'] > creatures[0]['y']:
        destiny['y'] -= 1
        move(creature, destiny)
    elif creature['y'] < creatures[0]['y']:
        destiny['y'] += 1
        move(creature, destiny)
    elif creature['x'] < creatures[0]['x']:
        destiny['x'] += 1
        move(creature, destiny)
    elif creature['x'] > creatures[0]['x']:
        destiny['x'] -= 1
        move(creature, destiny)


def iabispo(creature):
    destiny = {}
    destiny['x'] = creature['x']
    destiny['y'] = creature['y']

    if creature['y'] > creatures[0]['y'] and creature['x'] < creatures[0]['x']:
        destiny['y'] -= 1
        destiny['x'] += 1
        move(creature, destiny)

    elif creature['y'] > creatures[0]['y'] and creature['x'] > creatures[0]['x']:
        destiny['y'] -= 1
        destiny['x'] -= 1
        move(creature, destiny)

    elif creature['y'] < creatures[0]['y'] and creature['x'] < creatures[0]['x']:
        destiny['y'] += 1
        destiny['x'] += 1
        move(creature, destiny)

    elif creature['y'] < creatures[0]['y'] and creature['x'] > creatures[0]['x']:
        destiny['y'] += 1
        destiny['x'] -= 1
        move(creature, destiny)


def iatorre(creature):
    iapeao(creature)
    iapeao(creature)


def iacavalo(creature):
    iapeao(creature)
    iabispo(creature)


def iarei(creature):
    destiny = {}
    destiny['x'] = creature['x']
    destiny['y'] = creature['y']

    if creature['y'] > creatures[0]['y'] and creature['x'] < creatures[0]['x']:
        destiny['y'] -= 1
        destiny['x'] += 1
        move(creature, destiny)

    elif creature['y'] > creatures[0]['y'] and creature['x'] > creatures[0]['x']:
        destiny['y'] -= 1
        destiny['x'] -= 1
        move(creature, destiny)

    elif creature['y'] < creatures[0]['y'] and creature['x'] < creatures[0]['x']:
        destiny['y'] += 1
        destiny['x'] += 1
        move(creature, destiny)

    elif creature['y'] < creatures[0]['y'] and creature['x'] > creatures[0]['x']:
        destiny['y'] += 1
        destiny['x'] -= 1
        move(creature, destiny)

    elif creature['y'] > creatures[0]['y']:
        destiny['y'] -= 1
        move(creature, destiny)

    elif creature['y'] < creatures[0]['y']:
        destiny['y'] += 1
        move(creature, destiny)

    elif creature['x'] < creatures[0]['x']:
        destiny['x'] += 1
        move(creature, destiny)

    elif creature['x'] > creatures[0]['x']:
        destiny['x'] -= 1
        move(creature, destiny)


def iarainha(creature):
    iarei(creature)
    iarei(creature)


ia['peao'] = iapeao
ia['rei'] = iarei
ia['rainha'] = iarainha
ia['torre'] = iatorre
ia['bispo'] = iabispo
ia['cavalo'] = iapeao

creature_types = ["rainha", "rei"] + ["torre"] * 5 + \
    ["bispo"] * 20 + ["cavalo"] * 5 + ["peao"] * 20


def Creature(type, positionx, positiony, cor='branco'):
    map[positionx][positiony] = pecas[cor]
    return {
        'type': type,
        'cor': cor,
        'x': positionx,
        'y': positiony,
    }


map = [["." for _ in range(map_size)] for _ in range(map_size)]
emptymap = [["." for _ in range(map_size)] for _ in range(map_size)]
creatures = []

ry = random.randint(0, map_size-1)
rx = random.randint(0, map_size-1)

creatures.append(Creature('peao', rx, ry, "preto"))  # add the hero
creatures[0]['alive'] = True
for i in range(math.floor((map_size * map_size) / dificuldade)):
    ry = random.randint(0, map_size-1)
    rx = random.randint(0, map_size-1)
    if (map[rx][ry] == '.'):
        creatures.append(
            Creature(creature_types[random.randint(0, len(creature_types)-1)], rx, ry))
while True:
    maprint()
    char = getch.getch()
    if char == 'q' or char == 'Q':
        exit()
    elif char == '\x1b':
        getch.getch()  # Skip the [
        arrow_key = getch.getch()
        if arrow_key == 'A' and creatures[0]['x'] > 0:  # up
            for i in range(1, len(creatures)):
                if creatures[i]['x'] == creatures[0]['x'] - 1 and creatures[i][
                        'y'] == creatures[0]['y']:
                    creatures.remove(creatures[i])
                    break
            creatures[0]['x'] -= 1
        elif arrow_key == 'B' and creatures[0]['x'] < map_size - 1:  # down
            for i in range(1, len(creatures)):
                if creatures[i]['x'] == creatures[0]['x'] + 1 and creatures[i][
                        'y'] == creatures[0]['y']:
                    creatures.remove(creatures[i])
                    break
            creatures[0]['x'] += 1
        elif arrow_key == 'C' and creatures[0]['y'] < map_size - 1:  # right
            for i in range(1, len(creatures)):
                if creatures[i]['x'] == creatures[0]['x'] and creatures[i][
                        'y'] == creatures[0]['y'] + 1:
                    creatures.remove(creatures[i])
                    break
            creatures[0]['y'] += 1
        elif arrow_key == 'D' and creatures[0]['y'] > 0:  # left
            for i in range(1, len(creatures)):
                if creatures[i]['x'] == creatures[0]['x'] and creatures[i][
                        'y'] == creatures[0]['y'] - 1:
                    creatures.remove(creatures[i])
                    break
            creatures[0]['y'] -= 1
        for i in range(1, len(creatures)):
            ia[creatures[i]['type']](creatures[i])
            maprint()
            if not creatures[0]['alive']:
                maprint()
                break

        if not creatures[0]['alive']:
            print("\033[31m☠ Você fracassou! Zumbi está morto. ☠\033[0m")
            break
        elif len(creatures) == 1:
            print("\033[32m♚♛ Você venceu! Zumbi derrotou todos os fantasmas do imperio e pôde recuperar os bens roubados do seu povo. ♚♛\033[0m")
            break
