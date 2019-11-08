'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

CODIGO  ESPECIFICAÇÃO       PREÇO
1       Cachorro Quente     R$ 4.00
2       X-Salada            R$ 4.50
3       X-Bacon             R$ 5.00
4       Torrada simples     R$ 2.00
5       Refrigerante        R$ 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
3 2                 Total: R$ 10.00
4 3                 Total: R$ 6.00
2 3                 Total: R$ 13.50
'''
descricao = input().split()
prod_cod = int(descricao[0])
prod_qtd = float(descricao[1])

if prod_cod == 1:
    prod = {'produto': 'Cachorro Quente', 'valor': 4}
    pedido = prod_qtd * prod['valor']
    print('Total: R$ {:.2f}'.format(pedido))
elif prod_cod == 2:
    prod = {'produto': 'X-Salada', 'valor': 4.5}
    pedido = prod_qtd * prod['valor']
    print('Total: R$ {:.2f}'.format(pedido))
elif prod_cod == 3:
    prod = {'produto': 'X-Bacon', 'valor': 5}
    pedido = prod_qtd * prod['valor']
    print('Total: R$ {:.2f}'.format(pedido))
elif prod_cod == 4:
    prod = {'produto': 'Torrada simples', 'valor': 2}
    pedido = prod_qtd * prod['valor']
    print('Total: R$ {:.2f}'.format(pedido))
elif prod_cod == 5:
    prod = {'produto': 'Refrigerante', 'valor': 1.5}
    pedido = prod_qtd * prod['valor']
    print('Total: R$ {:.2f}'.format(pedido))
else:
    print('pedido invalido')

produtos = [{'cod': 1, 'produto': 'Cachorro Quente', 'valor': 4}, {'cod': 2, 'produto': 'X-Salada', 'valor': 4.5},
            {'cod': 3, 'produto': 'X-Bacon', 'valor': 5}, {'cod': 4, 'produto': 'Torrada simples', 'valor': 2},
            {'cod': 5, 'produto': 'Refrigerante', 'valor': 1.5}]
