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

print('NOTAS:')
n100 = valor // 100
print('{:.0f} nota(s) de R$ 100.00'.format(n100))

valor = valor - (n100 * 100)
n50 = valor // 50
print('{:.0f} nota(s) de R$ 50.00'.format(n50))

valor = valor - (n50 * 50)
n20 = valor // 20
print('{:.0f} nota(s) de R$ 20.00'.format(n20))

valor = valor - (n20 * 20)
n10 = valor // 10
print('{:.0f} nota(s) de R$ 10.00'.format(n10))

valor = valor - (n10 * 10)
n5 = valor // 5
print('{:.0f} nota(s) de R$ 5.00'.format(n5))

valor = valor - (n5 * 5)
n2 = valor // 2
print('{:.0f} nota(s) de R$ 2.00'.format(n2))

print('MOEDAS:')
valor = valor - (n2 * 2)
m1 = valor // 1
print('{:.0f} moeda(s) de R$ 1.00'.format(m1))

valor = valor - (m1 * 1)
m50 = valor // .5
print('{:.0f} moeda(s) de R$ 0.50'.format(m50))

valor = valor - (m50 * .5)
m25 = valor // .25
print('{:.0f} moeda(s) de R$ 0.25'.format(m25))

valor = valor - (m25 * .25)
m10 = valor // .1
print('{:.0f} moeda(s) de R$ 0.10'.format(m10))

valor = valor - (m10 * .10)
m5 = valor // .05
print('{:.0f} moeda(s) de R$ 0.05'.format(m5))

valor = valor - (m5 * .05)
m01 = valor // .01
print('{:.0f} moeda(s) de R$ 0.01'.format(m01))
