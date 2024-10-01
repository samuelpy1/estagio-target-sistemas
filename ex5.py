def inverter_string(s):
    string_invertida = ""
    i = len(s) - 1
    
    while i >= 0:
        #adiciona cada caractere à string invertida
        string_invertida += s[i]
        i -= 1
        
    return string_invertida

entrada_usuario = input("Digite uma string para inverter:")
resultado = inverter_string(entrada_usuario)
print(f"String original: {entrada_usuario}")
print(f"String invertida: {resultado}")