#int INDICE = 13, SOMA = 0, K = 0; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
#logicamente, executariamos até chegar no k 12 já que K < indice (13) faria com que K = 12 sejá o ultimo a ser checado
#como o valor é somado DEPOIS da adição do K + 1, fariamos 12 iterações com a ultima tendo o valor de K = 13.
#resultando no valor de 91(78 + 13).
#para testar em Python:
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1 
    SOMA = SOMA + K

print(SOMA)
