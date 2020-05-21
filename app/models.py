from datetime import datetime
from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	surname = db.Column(db.String(64), index=True)
# 	sect = db.Column(db.String(10), index=True)
# 	email = db.Column(db.String(120), index=True, unique=True)
# 	password_hash = db.Column(db.String(128))
# 	leav = db.relationship('Leave', backref='req', lazy=True)

# class Leave(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
# 	days_av = db.Column(db.Integer, index=True)
# 	days_req = db.Column(db.Integer)
# 	date_req = db.Column(db.String(10), index=True, unique=True)
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))