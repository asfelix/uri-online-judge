def media(a, b):
    """Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal."""
    media = ((3.5 * a) + (7.5 * b)) / 11

    return 'MEDIA = {:.5f}' .format(media)


assert 'MEDIA = 6.43182' == media(5.0, 7.1)
assert 'MEDIA = 4.84091' == media(0.0, 7.1)
assert 'MEDIA = 10.00000' == media(10.0, 10.0)
