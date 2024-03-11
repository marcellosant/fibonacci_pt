def fibonacci(quant):
    fibonacci_numeros = [0, 1]

    while fibonacci_numeros[-1] < quant:
        prox_numero = fibonacci_numeros[-1] + fibonacci_numeros[-2]
        fibonacci_numeros.append(prox_numero)

    if quant in fibonacci_numeros:
        return True
    else:
        return False

numero = int(input("Digite um número para identificar se pertence à sequência de Fibonacci: "))

if fibonacci(numero):
    print(f"O número {numero} está presente na sequência de Fibonacci.")
else:
    print(f"O número {numero} não está presente na sequência de Fibonacci.")
