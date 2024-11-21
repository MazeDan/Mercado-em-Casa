![Logo do Projeto](logo.png)

# Sistema de Rastreamento de Localização em Tempo Real

## Descrição

Este projeto é um sistema de rastreamento de localização em tempo real para entregadores. Ele inclui:

-   **Servidor Flask com SocketIO**: para gerenciar a recepção e a emissão das atualizações de localização.
-   **Scripts de Simulação de Entregadores**: dois scripts Python que simulam entregadores enviando suas localizações periodicamente ao servidor.

O objetivo é fornecer uma solução que possa rastrear múltiplos entregadores em tempo real e transmitir essas atualizações aos clientes conectados via WebSockets.


## Estrutura do Projeto

1.  **Servidor Flask com SocketIO** (`app.py`)
    
    -   Gerencia a recepção de atualizações de localização.
    -   Emite essas atualizações para todos os clientes conectados.
    -   Mantém um dicionário de localizações em tempo real dos entregadores.
2.  **Scripts de Simulação de Entregadores** (`entregador_1.py`, `entregador_2.py`)
    
    -   Simulam o envio de localizações dos entregadores.
    -   Enviam periodicamente dados ao servidor Flask para atualização.

## Instalação

1.  **Clone o repositório**:
    
    bash
    
    Copiar código
    
    `git clone https://github.com/seu-usuario/projeto-rastreamento
    cd projeto-rastreamento` 
    
2.  **Crie e ative um ambiente virtual**:
    
    bash
    
    Copiar código
    
    `python -m venv env
    source env/bin/activate  # Para sistemas Unix
    env\Scripts\activate  # Para Windows` 
    
3.  **Instale as dependências**:
    
    bash
    
    Copiar código
    
    `pip install -r requirements.txt` 
    
    O arquivo `requirements.txt` deve conter:
    
    Copiar código
    
    `Flask
    Flask-SocketIO
    requests` 
    

## Execução

1.  **Inicie o servidor Flask**:
    
    bash
    
    Copiar código
    
    `python app.py` 
    
2.  **Inicie os scripts de simulação de entregadores**:
    
    -   Em janelas separadas do terminal:
    
    bash
    
    Copiar código
    
    `python entregador_1.py`

## O que foi Feito


|Feito                |AÇÃO | AUTOR
|----------------|-------------------------------|-------------------------------|
|🟢|Desenvolvimento da Logo    |  DANIEL SANTANA
|🟢|Desenvolvimento do servidor SocketIO    |            DANIEL SANTANA
|🟢|   Desenvolvimento do receptor do entregador| DANIEL SANTANA
|🔴|Front-end da Pagina|
|🔴|Desenvolvimento do sistema de login|
|🔴|Conexão do sistema de login com o receptor do entregador|

