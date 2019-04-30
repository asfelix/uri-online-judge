"""
Faça um programa que leia três valores e apresente o maior dos três valores
 lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

￼MaiorAB = (a + b + abs(a - b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um
 segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior valor seguido por um espaço e a mensagem "é o maior".
"""

line = input().split(' ')
A, B, C = int(line[0]), int(line[1]), int(line[2])

maiorAB = (A + B + abs(A - B)) / 2
maior = (maiorAB + C + abs(maiorAB - C)) / 2

print('{:.0f} é o maior' .format(maior))

'''
https://www.geeksforgeeks.org/abs-in-python/

The abs() function is used to return the absolute value of a number.

The abs() takes only one argument, a number whose absolute value is to be
 returned. The argument can be an integer, a floating point number or a complex
  number.

    * If the argument is an integer or floating point number, abs() returns the
     absolute value in integer or float.
    * In case of complex number, abs() returns only the magnitude part and that
     can also be a floating point number.
'''

# floating point number
float = -54.26
print('Absolute value of integer is:', abs(float))

# An integer
int = -94
print('Absolute value of float is:', abs(int))

# A complex number
complex = (3 - 4j)
print('Absolute value or Magnitude of complex is:', abs(complex))
