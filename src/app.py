from flask import Flask, jsonify,request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from alumnoDao import Alumno
#Convert indentation to Tabs
app = Flask(__name__)
@app.route('/alumnos/readAll', methods=['GET'])
def listar():
	try:
		rows = cx.readAll()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

@app.route('/alumnos/delete/<int:id>', methods=['DELETE'])
def eliminarAlumno(id):
	try:
		cx.idalumno=id
		resp = cx.delete()
		resp = jsonify('Alumno eliminado')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
   
@app.route('/alumnos/<int:id>')
def findById(id):
	try:
		cx.idalumno=id
		row = cx.read()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

@app.route('/alumnos/create', methods=['POST'])
def crear():
	try:
		_json = request.json
		cx.nombre = _json['nombre']
		cx.apellido = _json['apellido']
		if request.method == 'POST':
			resp = cx.create()
			resp = jsonify('alumno registrado')
			resp.status_code = 200
			return resp
	except Exception as e:
		print(e)

@app.route('/alumnos/update', methods=['PUT'])
def update():
	try:
		_json = request.json
		cx.idalumno = _json['id']
		cx.nombre = _json['nombre']
		cx.apellido = _json['apellido']
		if request.method == 'PUT':
			resp = cx.update()
			resp = jsonify('alumno modificado')
			resp.status_code = 200
			return resp
	except Exception as e:
		print(e)

if __name__=="__main__":
	cx = Alumno()
	app.run(host="0.0.0.0",port=5000, debug=True)