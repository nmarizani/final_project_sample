from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# Route to trigger notifications
@app.route('/notify', methods=['POST'])
def notify():
    message = request.json.get('message')
    socketio.emit('notification', {'message': message}, broadcast=True)
    return jsonify(success=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/recycling_tracker')
def recycling_tracker():
    return render_template('recycling_tracker.html')

@app.route('/services_management')
def services_management():
    return render_template('services_management.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/login')
def login():
    # Logic for handling login
    return render_template('login.html')

if __name__ == '__main__':
    socketio.run(debug=True)
