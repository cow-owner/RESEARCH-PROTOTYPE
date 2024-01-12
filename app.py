from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database
db = SQLAlchemy(app)

class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now(), nullable=False)

@app.route('/')
def index():
    qr_code_data = QRCode.query.order_by(QRCode.timestamp.desc()).first()
    return render_template('index.html', qr_code_data=qr_code_data)

@app.route('/qr-data', methods=['POST'])
def receive_qr_data():
    qr_code_data = request.json.get('qrCodeData')
    new_qr_data = QRCode(data=qr_code_data)
    db.session.add(new_qr_data)
    db.session.commit()
    print(f"Received QR Code Data: {qr_code_data}")
    return {'status': 'success'}

if __name__ == '__main__':
    local_ip = socket.gethostbyname(socket.gethostname())
    print(f"Server running at http://{local_ip}:5000/")

    with app.app_context():
        db.create_all()  # Create the database tables

    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)

# run the server with "waitress-serve --host=0.0.0.0 --port=5000 app:app"
# downloading modules:
# py -m pip install Flask
# py -m pip install Flask-CORS
# py -m pip install waitress
# py -m pip install pip install Flask-SQLAlchemy
