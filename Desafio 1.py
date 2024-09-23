def pertence_fibonnaci(num):
    fibonacci = [0 , 1] #Comecando a sequencia com 0 e 1
    while fibonacci[-1] < num:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)
    
    if num in fibonacci:
        return True, fibonacci
    else:
        return False, fibonacci

numero = int(input('Digite um numero:'))
resultado, sequencia = pertence_fibonnaci(numero)

if resultado:
    print(f'O número {numero} pertence a sequencia de fibonacci: {sequencia}')
else:
    print(f'O número {numero} não pertence a sequencia de fibonacci: {sequencia}')