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

valor = input().split('.')
notas = int(valor[0])
moedas = int(valor[1])

print('NOTAS:')
notas100 = notas // 100
print('{} nota(s) de R$ 100.00'.format(notas100))

notas = notas - (notas100 * 100)
notas50 = notas // 50
print('{} nota(s) de R$ 50.00'.format(notas50))

notas = notas - (notas50 * 50)
notas20 = notas // 20
print('{} nota(s) de R$ 20.00'.format(notas20))

notas = notas - (notas20 * 20)
notas10 =  notas // 10
print('{} nota(s) de R$ 10.00'.format(notas10))

notas = notas - (notas10 * 10)
notas5 = notas // 5
print('{} nota(s) de R$ 5.00'.format(notas5))

notas = notas - (notas5 * 5)
notas2 = notas // 2
print('{} nota(s) de R$ 2.00'.format(notas2))

print('MOEDAS:')
moedas1 = notas - (notas2 * 2)
print('{} moeda(s) de R$ 1.00'.format(moedas1))

moedas50 = moedas // 50
print('{} moeda(s) de R$ 0.50'.format(moedas50))

moedas = moedas - (moedas50 * 50)
moedas25 = moedas // 25
print('{} moeda(s) de R$ 0.25'.format(moedas25))

moedas = moedas - (moedas25 * 25)
moedas10 = moedas // 10
print('{} moeda(s) de R$ 0.10'.format(moedas10))

moedas = moedas - (moedas10 * 10)
moedas5 = moedas // 5
print('{} moeda(s) de R$ 0.05'.format(moedas5))

moedas = moedas - (moedas5 * 5)
moedas1 = moedas // 1
print('{} moeda(s) de R$ 0.01'.format(moedas1))
