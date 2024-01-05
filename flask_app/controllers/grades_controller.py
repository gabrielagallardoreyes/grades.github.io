from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.users import User
from flask_app.models.grades import Grade

@app.route('/new/grade')
def new_grade():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    return render_template('new.html')

@app.route('/create/grade', methods=['POST'])
def create_grade():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')

    #validar la calificación
    if not Grade.validate_grade(request.form):
        return redirect('/new/grade')
    
    #Guardar la calificación
    Grade.save(request.form)

    return redirect('/dashboard')

@app.route('/edit/grade/<int:id>')
def edit_grade(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #buscar la instancia de Grade que corresponde al ID
    diccionario = {"id": id}
    grade = Grade.get_by_id(diccionario)

    return render_template('edit.html', grade = grade)

@app.route('/update/grade', methods=['POST'])
def update_grade():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')

    #validar que el formulario sea correcto
    if not Grade.validate_grade(request.form):
        return redirect('/edit/grade/' + request.form['id'])

    #Actualizar el registro
    Grade.update(request.form)
    return redirect ('/dashboard')

@app.route('/delete/grade/<int:id>')
def delete_grade(id):
    if 'user_id' not in session:
    #Verificar que el usuario haya iniciado sesión
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #borrar 
    form = {"id": id}
    Grade.delete(form)
    return redirect('/dashboard')
