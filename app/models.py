from datetime import datetime
from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	title = db.Column(db.String(64), index=True)
	text = db.Column(db.String(10), index=True)
	