def area_total(raio):
    pi = 3.14159
    area = pi * (raio ** 2)

    return 'A={:.4f}'.format(area)


assert 'A=12.5664' == area_total(2.00)
assert 'A=31819.3103' == area_total(100.64)
assert 'A=70685.7750' == area_total(150.00)
