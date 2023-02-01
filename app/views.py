from flask import render_template, request
from app import app
import json

@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/all', methods=['GET'])
def all():
    list = {
        'name': ['самолет', 'самолет', 'вертолет', 'самолет'],
        'serial': ['643623', '68533', '832257', '6863232']
    }
    '''list = DefectsBase.all()'''
    return json.dumps(list)

@app.route('/report', methods=['POST'])
def report():
    data = request.get_json()
    print('Отчет для', data['name'], '#', data['serial'])
    return ''