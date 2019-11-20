def soma(a, b):
    soma = a + b
    return 'SOMA = {}' .format(soma)


assert 'SOMA = 40' == soma(30, 10)
assert 'SOMA = -20' == soma(-30, 10)
assert 'SOMA = 0' == soma(0, 0)