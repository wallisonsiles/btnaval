from datetime import datetime
import random

random.seed(datetime.now())


class Partida():
    def __init__(self):
        self.inicio = datetime.now()
        self.pontos = 0
        self.tabuleiro = Tabuleiro()
        self.pontoI = 0

    def jogar(self, x, y):
        if self.tabuleiro.matriz[x][y][2]:
            return False
        else:
            self.tabuleiro.destroi(x, y)
            if self.tabuleiro.matriz[x][y][0] != 'A':
                self.pontos += 1
                return True
    def pontoInimigo(self, ponto):
        self.pontoI = ponto


    def finaliza(self):
        if self.tabuleiro.fim():
            self.fim = datetime.now()
            return True


class Tabuleiro():
    def __init__(self):
        self.matriz = [[0 for x in range(14)] for x in range(14)]
        for j in range(14):
            for i in range(14):
                self.matriz[i][j] = ['A', 0, False] # A: POSICAO VAZIA, 0: DE ONDE VAI COMECAR, FALSE: O ESPACO ESTA VAZIO
        self.submarinos = 0
        self.destroyers = 0
        self.cruzadores = 0
        self.couracados = 0
        self.alocacao_automatica()

    def destroi(self, x, y):
        self.matriz[x][y][2] = True
        if self.matriz[x][y][0] != 'A':
            destruido = True
            for j in range(1, 13):
                for i in range(1, 13):
                    if self.matriz[i][j][0] == self.matriz[x][y][0] and self.matriz[i][j][1] == self.matriz[x][y][1]:
                        if self.matriz[i][j][2] == False:
                            destruido = False
            if destruido:
                c = self.matriz[x][y][0]
                if c == 'S':
                    self.submarinos -= 1
                elif c == 'D':
                    self.destroyers -= 1
                elif c == 'Cr':
                    self.cruzadores -= 1
                elif c == 'Co':
                    self.couracados -= 1

    def fim(self):
        return (self.submarinos + self.destroyers + self.cruzadores + self.couracados) == 0

    def posicao_disponivel(self, x, y):
        disponivel = True
        for j in range(-1, 2):
            for i in range(-1, 2):
                if self.matriz[x + i][y + j][0] != 'A':
                    disponivel = False
        return disponivel

    def aloca_submarino(self, pos):
        if self.posicao_disponivel(pos[0], pos[1]):
            self.submarinos += 1
            self.matriz[pos[0]][pos[1]] = ['S', self.submarinos, False]
            return True
        else:
            return False

    def aloca_destroyer(self, pos1, pos2):
        if self.posicao_disponivel(pos1[0], pos1[1]) and self.posicao_disponivel(pos2[0], pos2[1]):
            self.destroyers += 1
            self.matriz[pos1[0]][pos1[1]] = ['D', self.destroyers, False]
            self.matriz[pos2[0]][pos2[1]] = ['D', self.destroyers, False]
            return True
        else:
            return False

    def aloca_cruzador(self, pos1, pos2, pos3, pos4):
        if self.posicao_disponivel(pos1[0], pos1[1]) and self.posicao_disponivel(pos2[0],
                                                                                 pos2[1]) and self.posicao_disponivel(
                pos3[0], pos3[1]) and self.posicao_disponivel(pos4[0], pos4[1]):
            self.cruzadores += 1
            self.matriz[pos1[0]][pos1[1]] = ['Cr', self.cruzadores, False]
            self.matriz[pos2[0]][pos2[1]] = ['Cr', self.cruzadores, False]
            self.matriz[pos3[0]][pos3[1]] = ['Cr', self.cruzadores, False]
            self.matriz[pos4[0]][pos4[1]] = ['Cr', self.cruzadores, False]
            return True
        else:
            return False

    def aloca_couracado(self, pos1, pos2, pos3, pos4, pos5):
        if self.posicao_disponivel(pos1[0], pos1[1]) and self.posicao_disponivel(pos2[0],
                                                                                 pos2[1]) and self.posicao_disponivel(
                pos3[0], pos3[1]) and self.posicao_disponivel(pos4[0], pos4[1]) and self.posicao_disponivel(pos5[0],
                                                                                                            pos5[1]):
            self.couracados += 1
            self.matriz[pos1[0]][pos1[1]] = ['Co', self.couracados, False]
            self.matriz[pos2[0]][pos2[1]] = ['Co', self.couracados, False]
            self.matriz[pos3[0]][pos3[1]] = ['Co', self.couracados, False]
            self.matriz[pos4[0]][pos4[1]] = ['Co', self.couracados, False]
            self.matriz[pos5[0]][pos5[1]] = ['Co', self.couracados, False]
            return True
        else:
            return False

    def alocacao_automatica(self):
        # hidro
        off = [-1, 1]

        # couraçado
        while True:
            x = random.randint(5, 7)
            y = random.randint(5, 7)
            offx = random.randint(-1, 1)
            if offx == 0:
                offy = random.choice(off)
            else:
                offy = 0
            if self.aloca_couracado((x, y), (x + offx, y + offy), (x + 2 * offx, y + 2 * offy),
                                    (x + 3 * offx, y + 3 * offy), (x + 4 * offx, y + 4 * offy)):
                break

        # cruzador
        for i in range(2):
            while True:
                x = random.randint(4, 8)
                y = random.randint(4, 8)
                offx = random.randint(-1, 1)
                if offx == 0:
                    offy = random.choice(off)
                else:
                    offy = 0
                if self.aloca_cruzador((x, y), (x + offx, y + offy), (x + 2 * offx, y + 2 * offy),
                                       (x + 3 * offx, y + 3 * offy)):
                    break

        # destroyer
        for i in range(3):
            while True:
                x = random.randint(2, 7)
                y = random.randint(2, 7)
                offx = random.randint(-1, 1)
                if offx == 0:
                    offy = random.choice(off)
                else:
                    offy = 0
                if self.aloca_destroyer((x, y), (x + offx, y + offy)):
                    break

        # submarino
        for i in range(2):
            while True:
                x = random.randint(1, 12)
                y = random.randint(1, 12)
                if self.aloca_submarino((x, y)):
                    break