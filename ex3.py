import json

def calcular_faturamento(faturamento_mensal):
    #filtra os dias com faturamento e ignora dias com faturamento igual a 0
    faturamento_valido = [dia['valor'] for dia in faturamento_mensal if dia['valor'] > 0]
   
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    dias_acima_da_media = sum(1 for dia in faturamento_valido if dia > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

#função para carregar o JSON do arquivo
def carregar_dados_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

caminho_arquivo = 'dados.json'
faturamento_mensal = carregar_dados_arquivo(caminho_arquivo)
menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(faturamento_mensal)

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
