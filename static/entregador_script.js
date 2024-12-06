// Função para simular a obtenção da localização
function obterLocalizacao() {
    const latitude = -23.5505 + (Math.random() - 0.5) / 1000;  // Coordenadas próximas a São Paulo
    const longitude = -46.6333 + (Math.random() - 0.5) / 1000;
    return { latitude, longitude };
}

// Enviar a localização do entregador ao servidor
async function enviarLocalizacao() {
    const { latitude, longitude } = obterLocalizacao();
    const data = {
        id: "entregador_1", // Aqui você pode definir o ID único para o entregador
        latitude,
        longitude
    };

    try {
        const response = await fetch("/update_location", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            document.getElementById('status').textContent = 'Localização enviada com sucesso!';
        } else {
            document.getElementById('status').textContent = `Erro: ${response.status}`;
        }
    } catch (error) {
        document.getElementById('status').textContent = `Erro de conexão: ${error.message}`;
    }
}

// Adicionar o evento de clique ao botão
document.getElementById("sendLocationButton").addEventListener("click", enviarLocalizacao);
