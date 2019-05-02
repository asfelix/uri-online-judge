"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule
 o menor número de nota(s) e moeda(s) possíveis no qual o valor pode ser decomposto. As nota(s) consideradas são de 100, 50,
 20, 10, 5, 2. As moeda(s) possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de nota(s)
 necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de nota(s) e moeda(s) necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
"""

valor = float(input())

n100 = valor // 100
n50 = (valor % 100) // 50
n20 = (valor - ((n100 * 100) + (n50 * 50))) // 20
n10 = ((valor - ((n100 * 100) + (n50 * 50))) % 20) // 10
n5 = (((valor - ((n100 * 100) + (n50 * 50))) % 20) % 10) // 5
n2 = ((((valor - ((n100 * 100) + (n50 * 50))) % 20) % 10) % 5) // 2
m1 = (((((valor - ((n100 * 100) + (n50 * 50))) % 20) % 10) % 5) % 2) // 1
m50 = (((((valor - ((n100 * 100) + (n50 * 50))) % 20) % 10) % 5) % 1) // .5
m25 = ((((((valor - ((n100 * 100) + (n50 * 50))) % 20) % 10) % 5) % 1) % .5) // .25
m10 = (((((((valor - ((n100 * 100) + (n50 * 50))) % 20) % 10) % 5) % 1) % .5) % .25) // .1
m05 = ((((((((valor - ((n100 * 100) + (n50 * 50))) % 20) % 10) % 5) % 1) % .5) % .25) % .1) // .05
m01 = (((((((((valor - ((n100 * 100) + (n50 * 50))) % 20) % 10) % 5) % 1) % .5) % .25) % .1) % .05) // .01

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(n100))
print('{:.0f} nota(s) de R$ 50.00'.format(n50))
print('{:.0f} nota(s) de R$ 20.00'.format(n20))
print('{:.0f} nota(s) de R$ 10.00'.format(n10))
print('{:.0f} nota(s) de R$ 5.00'.format(n5))
print('{:.0f} nota(s) de R$ 2.00'.format(n2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(m1))
print('{:.0f} moeda(s) de R$ 0.50'.format(m50))
print('{:.0f} moeda(s) de R$ 0.25'.format(m25))
print('{:.0f} moeda(s) de R$ 0.10'.format(m10))
print('{:.0f} moeda(s) de R$ 0.05'.format(m05))
print('{:.0f} moeda(s) de R$ 0.01'.format(m01))
