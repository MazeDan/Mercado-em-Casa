from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/update_location": {"origins": "http://localhost:8000"}}) #Specify the allowed origin

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

    # Emitindo a localização para os clientes via SocketIO
    socketio.emit('location_update', {
        "id": entregador_id,
        "latitude": data['latitude'],
        "longitude": data['longitude']
    })

    return jsonify({"status": "success"})

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test')
def test():
    return render_template('test.html', nome='Entregador')

@socketio.on('connect')
def handle_connect():
    emit('all_locations', entregadores_location)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
