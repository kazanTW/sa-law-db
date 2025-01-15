from ..utils.db import db

class Amendment(db.Model):
    __tablename__ = 'amendments'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    law_id = db.Column(db.Integer, db.ForeignKey('laws.id'), nullable=False)

    # 法規關聯
    law = db.relationship('Law', backref='amendments')
