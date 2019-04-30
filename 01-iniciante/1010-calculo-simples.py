'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o
 valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o
  valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3
 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando
 de deixar um espaço após os dois pontos e um espaço após o "R$". O valor
  deverá ser apresentado com 2 casas após o ponto.
'''

line_1 = input().split(' ')
line_2 = input().split(' ')
id_1, qtd_1, value_1 = int(line_1[0]), float(line_1[1]), float(line_1[2])
id_2, qtd_2, value_2 = int(line_2[0]), float(line_2[1]), float(line_2[2])

total = (qtd_1 * value_1) + (qtd_2 * value_2)

print('VALOR A PAGAR: R$ {:.2f}' .format(total))
