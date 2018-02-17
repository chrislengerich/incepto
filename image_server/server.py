from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

# TODO: Add security (shared secret key)

# POST an image.
@app.route('/image', methods=['POST'])
def image():
    print request.files
    print request
    if 'image' in request.files:
        file = request.files['image']
        file_path = 'static/recent.jpg'
        file.save(file_path)
        return jsonify({'path': 'recent.jpg'})
    else:
        return jsonify({'path': ''})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
