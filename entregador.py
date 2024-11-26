import requests

ENTREGADOR_ID = "entregador_1"  # Defina um identificador único para cada entregador
SERVER_URL = "http://localhost:5000/update_location"

# Função para simular ou obter a localização do entregador
def obter_localizacao():
    # Para uma simulação, vamos variar levemente a localização a cada envio
    latitude = -23.5505 + random.uniform(-0.0005, 0.0005)  # Coordenadas próximas a São Paulo
    longitude = -46.6333 + random.uniform(-0.0005, 0.0005)
    return latitude, longitude

# Função para enviar a localização para o servidor
def enviar_localizacao():
    latitude, longitude = obter_localizacao()
    data = {
        "id": ENTREGADOR_ID,
        "latitude": latitude,
        "longitude": longitude
    }
    try:
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print(f"Localização enviada com sucesso: {data}")
        else:
            print(f"Erro ao enviar localização: {response.status_code}")
    except requests.RequestException as e:
        print(f"Erro de conexão com o servidor: {e}")


