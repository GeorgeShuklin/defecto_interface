from flask import render_template, request
from database import defects_base
from app import app
import json


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/all', methods=['POST'])
def all():
    defect_database = defects_base.DefectsBase('database\defects_base.db')
    plane_list = defect_database.all()
    defect_database.close()
    return json.dumps(plane_list)

@app.route('/report', methods=['POST'])
def report():
    data = request.get_json()
    defect_database = defects_base.DefectsBase('database\defects_base.db')
    defect_database.report('reports', data['name'], data['serial'])
    defect_database.close()
    return ''