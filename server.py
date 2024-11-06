from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Dicionário para armazenar a localização de cada entregador pelo ID
entregadores_location = {}

# Rota para o entregador enviar sua localização
@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    entregador_id = data['id']
    
    # Atualiza a localização do entregador específico
    entregadores_location[entregador_id] = {
        "latitude": data['latitude'],
        "longitude": data['longitude']
    }
    
    # Envia a localização atualizada do entregador específico para os clientes
    socketio.emit('location_update', {
        "id": entregador_id,
        "latitude": data['latitude'],
        "longitude": data['longitude']
    })
    return {"status": "success"}

# Endpoint WebSocket para o cliente se conectar
@socketio.on('connect')
def handle_connect():
    # Envia a localização de todos os entregadores ao cliente que acabou de se conectar
    emit('all_locations', entregadores_location)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
