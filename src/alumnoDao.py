import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Alumno:
	idalumno = 0
	nombre = ""
	apellido = ""

	def readAll(self):
		try:
			conexion = cx.conecta()
			cursor = conexion.cursor(pymysql.cursors.DictCursor)
			cursor.callproc('sp_listar_alumno')
			rows = cursor.fetchall()
			return rows
		except Exception as e:
			print(e)
		finally: 
			cursor.close()
			conexion.close()
	def delete(self):
		try:
			conexion = cx.conecta()
			cursor = conexion.cursor()
			cursor.callproc("sp_eliminar_alumno", [self.idalumno,])
			conexion.commit()
			return 1
		except Exception as e:
			print(e)
		finally:
			cursor.close() 
			conexion.close()    
	def read(self):
		try:
			conexion = cx.conecta()
			cursor = conexion.cursor(pymysql.cursors.DictCursor)
			cursor.callproc("sp_listar_alumno_id", [self.idalumno,])
			row = cursor.fetchall()
			return row
		except Exception as e:
			print(e)
		finally: 
			cursor.close()
			conexion.close()

	def create(self):
		try:
			_nombre = self.nombre
			_apellido = self.apellido
			data = [ _nombre, _apellido]
			conexion = cx.conecta()
			cursor = conexion.cursor(pymysql.cursors.DictCursor)
			cursor.callproc("sp_create_alumno",data)
			conexion.commit()
			return 1
		except Exception as e:
			print(e)
		finally: 
			cursor.close()
			conexion.close()

	def update(self):
		try:
			_id = self.idalumno
			_nombre = self.nombre
			_apellido = self.apellido
			data = [ _id, _nombre, _apellido]
			conexion = cx.conecta()
			cursor = conexion.cursor(pymysql.cursors.DictCursor)
			cursor.callproc("sp_editar_alumno",data)
			conexion.commit()
			return 1
		except Exception as e:
			print(e)
		finally: 
			cursor.close()
			conexion.close()