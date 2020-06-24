from flask import render_template, url_for, request, redirect, jsonify
from app import app, db
from app.models import User
from app.forms import RegForm, ReqLeave

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegForm()
	if form.validate_on_submit():
		return redirect(url_for('index'))
	return render_template('register.html', form=form)

@app.route('/api', methods=['POST'])
def create():
	cont = request.json
	usr = User(name=cont['name'], surname=cont['surname'])
	db.session.add(usr)
	db.session.commit()
	return jsonify(cont)
