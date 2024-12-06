from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e3a5b73b8f91c90fbc6b8e5f1d44c7b2d9a3c9df9f8e7e68'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return True

    def     is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash('Email já está em uso.', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        flash('Credenciais inválidas.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/localizacao')
@login_required
def localizacao():
    return render_template('localizacao.html',name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso.', 'success')
    return redirect(url_for('login'))

CORS(app, resources={r"/update_location": {"origins": "http://localhost:8000"}})

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
    return jsonify({"status": "success"})

@app.route('/')
@login_required
def index():
    return render_template('index.html' ,name=current_user.username)



@socketio.on('connect')
def handle_connect():
    emit('all_locations', entregadores_location)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
