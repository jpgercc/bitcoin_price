import requests

def obter_preco_bitcoin():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro na requisição:", response.status_code)
        return None

    data = response.json()
    
    try:
        preco_brl = data['bitcoin']['brl']
        return preco_brl
    except KeyError:
        print("Erro ao obter dados.")
        return None

# Testando a função
preco = obter_preco_bitcoin()
if preco:
    print(f"O preço mais recente do Bitcoin é: R$ {preco:,.2f}")
