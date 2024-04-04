from flask import Flask, jsonify, request
from marshmallow import Schema, fields
from sqlalchemy import text
from datetime import datetime

from endpoints.auth.register import register_bp
from endpoints.auth.login import login_bp

from endpoints.doctor.get_doctor import get_doctor_bp
from endpoints.doctor.get_doctor_id import get_doctor_id_bp
from endpoints.doctor.delete_doctor import delete_doctor_bp
from endpoints.doctor.update_doctor import update_doctor_bp

from endpoints.patient.post_patient import post_patient_bp
from endpoints.patient.update_patient import update_patient_bp
from endpoints.patient.delete_patient import delete_patient_bp
from endpoints.patient.get_patient import get_patient_bp



app = Flask(__name__)



app.register_blueprint(register_bp, url_prefix='/auth')
app.register_blueprint(login_bp, url_prefix='/auth')

app.register_blueprint(get_doctor_bp, url_prefix='/doctor')
app.register_blueprint(get_doctor_id_bp, url_prefix='/doctor')
app.register_blueprint(delete_doctor_bp, url_prefix='/doctor')
app.register_blueprint(update_doctor_bp, url_prefix='/doctor')

app.register_blueprint(post_patient_bp, url_prefix='/patient')
app.register_blueprint(get_patient_bp, url_prefix='/patient')
app.register_blueprint(update_patient_bp, url_prefix='/patient')
app.register_blueprint(delete_patient_bp, url_prefix='/patient')


@app.route('/', methods=['GET'])
def index():
    return 'Olá'

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=False)
