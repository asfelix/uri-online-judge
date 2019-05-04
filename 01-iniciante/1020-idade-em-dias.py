"""
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a
 em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todos os anos com 365 dias e todos
 mêsesu com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12
 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com
 objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
"""
idade = int(input(''))

anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

print('{} ano(s)'.format(anos))
print('{:.0f} mes(es)'.format(meses))
print('{:.0f} dia(s)'.format(dias))
