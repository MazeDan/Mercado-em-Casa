from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

entregadores_location = {}

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    entregador_id = data['id']
    entregadores_location[entregador_id] = {
        "latitude": data['latitude'],
        "longitude": data['longitude']
    }

    socketio.emit('location_update', {
        "id": entregador_id,
        "latitude": data['latitude'],
        "longitude": data['longitude']
    })

@socketio.on('connect')
def handle_connect():
    emit('all_locations', entregadores_location)

if __name__ == '__main__':
