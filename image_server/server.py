from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request, Response
from functools import wraps
from flask_socketio import SocketIO
import socketio
import time

app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)

# Simple security: pre-shared key.
API_KEY = "b09c4de1043f8ad0815d"

def check_auth(key):
    print key
    return key == API_KEY

def authenticate():
    """Sends 401 response"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper API key', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not 'key' in request.args or not check_auth(request.args['key']):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# POST an image.
@app.route('/image', methods=['POST'])
@requires_auth
def image():
    if 'image' in request.files:
        file = request.files['image']
        file_path = 'static/recent.jpg'
        file.save(file_path)
        socketio.emit('new_image', {}, broadcast=True)
        return jsonify({'path': 'recent.jpg'})
    else:
        return jsonify({'path': ''})

@app.route('/')
@requires_auth
def index():
    if 'key' not in request.args and request.args['key'] != API_KEY:
        return render_template('')
    return render_template('index.html', cache_key=time.time())

if __name__ == '__main__':
    socketio.run(app)
