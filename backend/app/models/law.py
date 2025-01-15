from ..utils.db import db

class Law(db.Model):
    __tablename__ = 'laws'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    last_amended = db.Column(db.DateTime, nullable=False)

    # 關聯條文
    articles = db.relationship('Article', backref='law', cascade="all, delete-orphan")
