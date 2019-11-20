def produto(a, b):
    prod = a * b
    return 'PROD = {}' .format(prod)


assert 'PROD = 27' == produto(3, 9)
assert 'PROD = -300' == produto(-30, 10)
assert 'PROD = 0' == produto(0, 9)