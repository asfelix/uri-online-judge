'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer
 no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4
  casas decimais após a vírgula, segundo a fórmula:

Distancia =￼ square((x2 - x1) ** 2) + (y2 - y1) ** 2))

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois
 valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de
  ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas
 após o ponto decimal.
'''

from math import sqrt

line1 = input().split(' ')
line2 = input().split(' ')

p1 = float(line1[0]), float(line1[1])
p2 = float(line2[0]), float(line2[1])

distancia: float = sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))

print('{:.4f}' .format(distancia))
