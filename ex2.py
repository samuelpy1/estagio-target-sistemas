def fibonacci(numero):
    fib_seq = [0, 1] # começo do fibonacci
    while fib_seq[-1] < numero: # cria toda sequência até o numero desejado
        next_value = fib_seq[-1] + fib_seq[-2] # soma os ultimos 2 valores da lista
        fib_seq.append(next_value) # cria uma lista com os valores

    return fib_seq

def pertence_fibonacci(numero):
    fib_seq = fibonacci(numero)
    
    if numero in fib_seq:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))
