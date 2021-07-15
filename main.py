from bisect import bisect_left

'''Utilizamos a medida de tempo em minutos.'''

'''Ambos, a heuristica e a arvore já estão com todos os pesos convertidos para tempo(minutos).'''

heuristica = {
    'E1': [['E1', 0.0], ['E2', 15.0], ['E3', 27.75], ['E4', 37.2], ['E5', 54.5],
           ['E6', 58.1], ['E7', 53.6],
           ['E8', 38.1], ['E9', 26.4], ['E10', 13.6], ['E11', 25.0],
           ['E12', 40.9], ['E13', 41.4],
           ['E14', 44.7]],

    'E2': [['E1', 15.0], ['E2', 0.0], ['E3', 12.75], ['E4', 22.2], ['E5', 39.9],
           ['E6', 43.6], ['E7', 39.1],
           ['E8', 25.9], ['E9', 15.0], ['E10', 5.25], ['E11', 23.25], ['E12', 31.3],
           ['E13', 28.6], ['E14', 32.7]],

    'E3': [['E1', 27.7], ['E2', 12.75], ['E3', 0.0], ['E4', 9.45], ['E5', 27.2],
           ['E6', 30.9], ['E7', 26.4],
           ['E8', 20.4], ['E9', 14.1], ['E10', 15.4], ['E11', 29.25],
           ['E12', 28.6], ['E13', 18.15],
           ['E14', 25.2]],

    'E4': [['E1', 37.2], ['E2', 22.2], ['E3', 9.45], ['E4', 0.0], ['E5', 18.0], ['E6', 21.5],
           ['E7', 17.25], ['E8', 18.6], ['E9', 18.9],
           ['E10', 25.0], ['E11', 35.4], ['E12', 27.9], ['E13', 15.9],
           ['E14', 23.1]],

    'E5': [['E1', 54.5], ['E2', 39.9], ['E3', 27.2], ['E4', 18.0],
           ['E5', 0.0], ['E6', 4.5], ['E7', 3.5],
           ['E8', 29.0], ['E9', 34.9], ['E10', 42.3], ['E11', 51.3], ['E12', 37.2],
           ['E13', 21.75], ['E14', 26.8]],

    'E6': [['E1', 58.1], ['E2', 43.6], ['E3', 30.9],
           ['E4', 21.5],
           ['E5', 4.5], ['E6', 0.0], ['E7', 4.9], ['E8', 33.45], ['E9', 38.55], ['E10', 45.45],
           ['E11', 55.0],
           ['E12', 41.4], ['E13', 22.8], ['E14', 27.2]],

    'E7': [['E1', 53.6], ['E2', 39.1], ['E3', 26.4], ['E4', 17.25],
           ['E5', 3.5],
           ['E6', 4.9], ['E7', 0.0], ['E8', 30.0], ['E9', 34.5], ['E10', 40.95],
           ['E11', 51.3], ['E12', 38.55], ['E13', 18.6],
           ['E14', 23.4]],

    'E8': [['E1', 38.1], ['E2', 25.9], ['E3', 20.4], ['E4', 18.6], ['E5', 29.0], ['E6', 33.4],
           ['E7', 30.0], ['E8', 0.0], ['E9', 12.2],
           ['E10', 30.4], ['E11', 24.1], ['E12', 9.6], ['E13', 34.05],
           ['E14', 41.4]],

    'E9': [['E1', 26.4], ['E2', 15.0], ['E3', 14.1], ['E4', 18.9], ['E5', 34.95],
           ['E6', 38.55], ['E7', 34.5], ['E8', 12.2],
           ['E9', 0.0], ['E10', 20.25], ['E11', 16.7], ['E12', 16.35], ['E13', 31.8],
           ['E14', 39.9]],

    'E10': [['E1', 13.6], ['E2', 5.25], ['E3', 15.4], ['E4', 25.0],
            ['E5', 42.3], ['E6', 45.45], ['E7', 40.95],
            ['E8', 30.4], ['E9', 20.25], ['E10', 0.0], ['E11', 26.4], ['E12', 36.3],
            ['E13', 28.0], ['E14', 31.8]],

    'E11': [['E1', 25.0], ['E2', 23.25], ['E3', 29.25], ['E4', 35.4],
            ['E5', 51.3], ['E6', 55.0],
            ['E7', 51.3], ['E8', 24.1], ['E9', 16.7],
            ['E10', 26.4], ['E11', 0.0], ['E12', 21.2],
            ['E13', 47.25], ['E14', 53.25]],

    'E12': [['E1', 40.95], ['E2', 31.3], ['E3', 28.6], ['E4', 27.9],
            ['E5', 37.2], ['E6', 41.4], ['E7', 38.55],
            ['E8', 9.6], ['E9', 16.35], ['E10', 36.3], ['E11', 21.2], ['E12', 0.0],
            ['E13', 43.1], ['E14', 50.4]],

    'E13': [['E1', 41.4], ['E2', 28.6], ['E3', 18.15], ['E4', 15.9], ['E5', 21.75],
            ['E6', 22.8], ['E7', 18.6], ['E8', 34.05],
            ['E9', 31.8], ['E10', 28.0], ['E11', 47.25], ['E12', 43.1], ['E13', 0.0],
            ['E14', 7.65]],

    'E14': [['E1', 44.7], ['E2', 32.7], ['E3', 24.9], ['E4', 23.1], ['E5', 26.8],
            ['E6', 27.2], ['E7', 23.4],
            ['E8', 41.4], ['E9', 39.9], ['E10', 31.8], ['E11', 53.2],
            ['E12', 50.4], ['E13', 7.65], ['E14', 0.0]]

}

arvore = {'E1': [['E2', 15.0, 'b']],
          'E2': [['E1', 15.0, 'b'], ['E3', 12.7, 'b'], ['E9', 15.0, 'y'], ['E10', 5.25, 'y']],
          'E3': [['E2', 12.7, 'b'], ['E4', 9.4, 'b'], ['E9', 14.1, 'r'], ['E13', 28.0, 'r']],
          'E4': [['E3', 9.4, 'b'], ['E5', 19.5, 'b'], ['E8', 22.9, 'g'], ['E13', 19.2, 'g']],
          'E5': [['E4', 19.5, 'b'], ['E6', 4.5, 'b'], ['E7', 3.5, 'y'], ['E8', 45.0, 'y']],
          'E6': [['E5', 4.5, 'b']],
          'E7': [['E5', 3.5, 'y']],
          'E8': [['E4', 22.9, 'g'], ['E5', 45.0, 'y'], ['E9', 14.3, 'y'], ['E12', 9.6, 'g']],
          'E9': [['E2', 15.0, 'y'], ['E3', 14.1, 'r'], ['E8', 14.3, 'y'], ['E11', 18.3, 'r']],
          'E10': [['E2', 5.25, 'y']],
          'E11': [['E9', 18.3, 'r']],
          'E12': [['E8', 9.6, 'g']],
          'E13': [['E14', 7.65, 'g'], ['E3', 28.0, 'r'], ['E4', 19.2, 'g']],
          'E14': [['E13', 7.65, 'g']]}


'''Para a geração das tabelas de horário de cada linha, foi utilizado um for percorrendo no intervalo em minutos de cada
linha'''
blue_line = [240, 255, 270, 285, 300, 315, 330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 495, 510, 525, 540,
             555, 570, 585, 600, 615, 630, 645, 660, 675, 690, 705, 720, 735, 750, 765, 780, 795, 810, 825, 840, 855,
             870, 885, 900, 915, 930, 945, 960, 975, 990, 1005, 1020, 1035, 1050, 1065, 1080, 1095, 1110, 1125, 1140,
             1155, 1170, 1185, 1200, 1215, 1230, 1245, 1260, 1275, 1290, 1305, 1320, 1335, 1350, 1365, 1380, 1395, 1410,
             1425] #15 em 15 minutos

yellow_line = [240, 247, 254, 261, 268, 275, 282, 289, 296, 303, 310, 317, 324, 331, 338, 345, 352, 359, 366, 373, 380,
               387, 394, 401, 408, 415, 422, 429, 436, 443, 450, 457, 464, 471, 478, 485, 492, 499, 506, 513, 520, 527,
               534, 541, 548, 555, 562, 569, 576, 583, 590, 597, 604, 611, 618, 625, 632, 639, 646, 653, 660, 667, 674,
               681, 688, 695, 702, 709, 716, 723, 730, 737, 744, 751, 758, 765, 772, 779, 786, 793, 800, 807, 814, 821,
               828, 835, 842, 849, 856, 863, 870, 877, 884, 891, 898, 905, 912, 919, 926, 933, 940, 947, 954, 961, 968,
               975, 982, 989, 996, 1003, 1010, 1017, 1024, 1031, 1038, 1045, 1052, 1059, 1066, 1073, 1080, 1087, 1094,
               1101, 1108, 1115, 1122, 1129, 1136, 1143, 1150, 1157, 1164, 1171, 1178, 1185, 1192, 1199, 1206, 1213,
               1220, 1227, 1234, 1241, 1248, 1255, 1262, 1269, 1276, 1283, 1290, 1297, 1304, 1311, 1318, 1325, 1332,
               1339, 1346, 1353, 1360, 1367, 1374, 1381, 1388, 1395, 1402, 1409, 1416, 1423, 1430, 1437] #7 em 7 minutos

red_line = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440,
            450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,
            660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860,
            870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060,
            1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240,
            1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420,
            1430] #10 em 10 minutos

green_line = [240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640,
              660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020, 1040,
              1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1320, 1340, 1360, 1380,
              1400, 1420] #20 em 20 minutos

estacoes = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', ' E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14']


def closest(line, _minute):   # Retorna, das listas de linhas, o horario (em minutos) do próximo trem que ira sair.
    pos = bisect_left(line, _minute)

    if pos == 0:
        return line[0]
    if pos == len(line):
        return line[-1]
    after = line[pos]
    return after


'''Verifica em qual linha o metrô está e acrescenta ao peso o tempo restante para a chegada do próximo trem'''
def which_line(color, fn_node):
    if color == 'b':
        return closest(blue_line, fn_node)
    elif color == 'y':
        return closest(yellow_line, fn_node)
    elif color == 'r':
        return closest(red_line, fn_node)
    else:
        return closest(green_line, fn_node)


'''Converte a hora no formato HH:MM para minutos.'''
def time_to_minute(string):
    hours, minute = string.split(':')
    return int(hours) * 60 + int(minute)


'''Converte minutos para hora no formato HH:MM.'''
def minute_to_time(minute):
    return '{:02d}:{:02d}'.format(*divmod(minute, 60))


'''Algoritmo de busca A*.'''
def AStarSearch(start, end, minutes):
    cost = {start: minutes}
    global arvore, heuristica
    closed = []  # closed nodes
    opened = [[start, minutes]]  # Nós abertos
    colors = {}

    '''Encontra os nós visitados'''

    while True:
        fn = [i[1] for i in opened]  # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # Nó atual
        closed.append(opened[chosen_index])

        del opened[chosen_index]

        if closed[-1][0] == end:  # Para o loop se o Nó final for encontrado
            break

        for item in arvore[node]:
            transshipment = 0
            fn_node = which_line(item[2], cost[node])

            if len(colors) == 0:   # Verifica se há ou não baldeação.
                colors[node] = ''
            elif node not in colors:
                colors[node] = item[2]
            else:
                if colors[node] != '' and colors[node] != item[2]:
                    transshipment += 4

            if item[0] in [closed_item[0] for closed_item in closed]:
                continue

            cost.update({item[0]: cost[node] + item[1]})  # Adiciona o nó ao dicionario de custo.

            fn_node += heuristica[item[0]][int(end.split('E')[1]) - 1][1] + item[1] + transshipment  # Calcula o Peso do nó em analise.

            temp = [item[0], fn_node]
            opened.append(temp)  # armazena o f(n) do nó atual na lista opened.

    #Encontra a sequência ótima
    trace_node = end  # nó de rastreamento ideal.
    optimal_sequence = [end]  # sequência de nós ótima
    for i in range(len(closed) - 2, -1, -1):

        check_node = closed[i][0]  # nó atual

        if trace_node in [children[0] for children in arvore[check_node]]:
            children_costs = [temp[1] for temp in arvore[check_node]]
            children_nodes = [temp[0] for temp in arvore[check_node]]

            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()  # reverte a sequencia ótima

    return closed, optimal_sequence


if __name__ == '__main__':

    _start = input('Estação de Partida: (Ex: E1, E12, E5, ...)\n').upper()

    while _start not in estacoes:
        print('=' * 50 + '\nInsira uma estação válida!\n' + '=' * 50)
        _start = input('Estação de Partida: (Ex: E1, E12, E5, ...)\n').upper()

    _end = input('Destino: (Ex: E1, E12, E5, ...)\n').upper()

    while _end not in estacoes:
        print('=' * 50 + '\nInsira uma estação válida!\n' + '=' * 50)
        _end = input('Destino: (Ex: E1, E12, E5, ...)\n').upper()

    _time = input('Horas: (HH:MM)\n')

    while ':' not in _time:
        print('=' * 50 + '\nInsira as horas corretamente!\n' + '=' * 50)
        _time = input('Horas: (HH:MM)\n')

    _minutes = time_to_minute(_time)

    arrival, optimal_nodes = AStarSearch(_start, _end, _minutes)

    print('\n|  CBTU Informa  |')
    print('Hora de Chegada: ' + minute_to_time(int(arrival[-1][1])))
    print('Duração: ' + minute_to_time(int(arrival[-1][1]) - _minutes))
    print('Rota mais rápida: ' + ' → '.join(optimal_nodes))
