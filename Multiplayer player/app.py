from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Priya@260903'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Create a User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            return 'Username already exists!'
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('home'))
    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        return 'Invalid credentials!'
    return render_template('login.html')

# Home Route (Game page)
@app.route('/home')
@login_required
def home():
    return render_template('home.html')

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# SocketIO Events
players = {}

@socketio.on('join_game')
def handle_join_game(data):
    player = current_user.username
    if len(players) == 0:
        players['player1'] = player
        join_room('game_room')
        emit('game_started', {'player': player}, room='game_room')
    elif len(players) == 1:
        players['player2'] = player
        join_room('game_room')
        emit('game_started', {'player': player}, room='game_room')
        # Notify both players that the game has started
        emit('game_start', room='game_room')
    else:
        emit('game_full', room=current_user.username)

@socketio.on('make_move')
def handle_move(data):
    move = data['move']
    player = current_user.username
    opponent = 'player1' if player == 'player2' else 'player2'
    emit('update_board', {'move': move, 'player': player}, room='game_room')

@socketio.on('disconnect')
def handle_disconnect():
    player = current_user.username
    if player in players:
        del players[player]
    print(f"{player} disconnected.")
    emit('player_left', {'player': player}, room='game_room')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Now inside the app context
    socketio.run(app, debug=True)
