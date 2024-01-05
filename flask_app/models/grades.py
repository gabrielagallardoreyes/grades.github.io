from flask_app.config.mysqlconnection import connectToMySQL #conexión con base de datos
from flask import flash #flash es el encargado de mandar mensajes/errores
from datetime import datetime #manipular fechas y saber la fecha actual
import re

class Grade:

    def __init__(self, data):
        self.id = data['id']
        self.student = data['student']
        self.date = data['date']
        self.stack = data['stack']
        self.grade = data['grade']
        self.belt = data['belt']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #JOIN
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    @staticmethod 
    def validate_grade(form):
        is_valid = True

        if form['student'] == '':
            flash('Alumno no puede ser vacío', 'grades')
            is_valid = False
        
        if form['grade'] == ''or not re.match(r'^\d+(.\d+)?$', form['grade']):
            flash('Ingresa una calificación', 'grades')
            is_valid = False
        
        else:
            if float(form['grade']) < 1 or float(form['grade']) > 10:
                flash('Calificación debe ser entre 1 y 10', 'grades')
                is_valid = False
        
        if form['date'] == '':
            flash('Ingrese una fecha', 'grades')
            is_valid = False
        else:
            fecha_examen = datetime.strptime(form['date'], '%Y-%m-%d') #estoy transformando el texto fecha en formato de fecha
            hoy = datetime.now() #me da la fecha de hoy
            if hoy < fecha_examen:
                flash('La fecha no puede ser en el futuro', 'grades')
                is_valid = False
        return is_valid

    @classmethod
    def save(cls, form):
        query = "INSERT INTO grades (student, stack, date, grade, belt, user_id) VALUES (%(student)s, %(stack)s, %(date)s, %(grade)s, %(belt)s, %(user_id)s)"
        result = connectToMySQL('esquema_belt_reviewer').query_db(query, form)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT grades.*, users.first_name, users.last_name FROM grades JOIN users ON user_id = users.id"
        results = connectToMySQL('esquema_belt_reviewer').query_db(query) #lista de diccionarios
        grades = []
        for grade in results:
            grades.append(cls(grade)) #1.- cls(grade) crea la instancia en base al diccionario 2. grades.append() agrego la instancia a la lista
        
        return grades
    
    @classmethod
    def get_by_id(cls, form):
        #form = {"id":1}
        query = "SELECT grades.*, users.first_name, users.last_name FROM grades JOIN users ON user_id = users.id WHERE grades.id = %(id)s"
        result = connectToMySQL('esquema_belt_reviewer').query_db(query, form)
        grade = cls(result[0])
        return grade
    
    @classmethod
    def update(cls, form):
        query = "UPDATE grades SET student = %(student)s, stack = %(stack)s, date = %(date)s, grade = %(grade)s, belt = %(belt)s WHERE id = %(id)s"
        result = connectToMySQL('esquema_belt_reviewer').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls, form):
        query = "DELETE FROM grades WHERE  id= %(id)s"
        result = connectToMySQL('esquema_belt_reviewer').query_db(query, form)
        return result