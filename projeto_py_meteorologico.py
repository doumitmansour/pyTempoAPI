import requests

cidade = input("Digite o nome da cidade: ")
chave_api = "492f966c9bd9970a1b20ab6d5dde32e8"
lang = "pt_br"

url = f"http://api.openweathermap.org/data/2.5/weather?&lang=pt_br&q={cidade}&appid={chave_api}&units=metric"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados["main"]["temp"]
    umidade = dados["main"]["humidity"]
    precipitacao = dados.get("rain", {}).get("1h", 0)
    velocidade_vento = dados["wind"]["speed"]
    direcao_vento = dados["wind"]["deg"]
    clima_atual = dados["weather"][0]["description"]
    
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade do ar: {umidade}%")
    print(f"Velocidade do vento: {velocidade_vento} m/s")
    print(f"Direção do vento: {direcao_vento}°")
    print(f"Clima atual: {clima_atual}")
    print(f"Chuva nas últimas 1 hora: {precipitacao} mm")
else:
    print("Não foi possível obter os dados meteorológicos.")