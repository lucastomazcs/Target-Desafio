texto = input('Digite uma String:')

texto_normal = texto.lower()

contagem_a = texto_normal.count('a')

if contagem_a > 0:
    print(f'A letra a está presente {contagem_a} vezes na string.')
else:
    print('A letra a não está presente na string.')