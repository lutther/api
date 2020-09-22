from flask import render_template, url_for, request, redirect, jsonify, send_file
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
	usr = User(name=cont['pack'], title=cont['title'], text=cont['text'])
	db.session.add(usr)
	db.session.commit()
	return jsonify(cont)

@app.route('/d/<name>', methods=['GET'])
def dd(name):
	upload = 'static/' + name
	return send_file(upload, as_attachment=True)

@app.route('/view')
def v():
	view = User.query.all()
	return render_template('view.html', view=view)