import math as mt
import numpy as np
from numpy import random
import random
from numpy.core.numeric import indices


def Sorteia_praMIM_Percival(jogador1, jogador2, jogador3, jogador4, jogador5, jogador6, jogador7, jogador8, jogador9, jogador10):

    NomeDosIndividuos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nomeTotal = [jogador1, jogador2, jogador3, jogador4, jogador5, jogador6, jogador7, jogador8, jogador9, jogador10]
    a = random.sample(NomeDosIndividuos, 5)

    result = random.sample(NomeDosIndividuos, 5)

    n = 4
    m = 1
    b = NomeDosIndividuos
    # print(a)
    for l in range(4):
        anterior = a[l]
        for k in range(n):
            proximonum = a[l + m]
            if (a[l] != 0):
                anterior = a[l - m]

            if (a[l] == (proximonum) or a[l] == (anterior)):
                if ((a[l])):
                    a[l] += 1

            m += 1
        m = 1
        n -= 1
    for i in range(5):
        if (b.__contains__(a[i])):
            b.remove(a[i])
    print('Time 1:', a)
    print('team2: ', b)

    nomeTeam1 = []
    nomeaTeam2 = []

    for z in range(len(a)):
        nomeTeam1.append(nomeTotal[a[z] - 1])
        nomeaTeam2.append(nomeTotal[b[z] - 1])

    print("TIME AZUL: ", nomeTeam1)
    print("TIME NÃO AZUL: ", nomeaTeam2)
    return nomeTeam1, nomeaTeam2
    # print(result)
