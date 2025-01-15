from ..utils.db import db

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    law_id = db.Column(db.Integer, db.ForeignKey('laws.id'), nullable=False)

    # 關聯條文細項
    sub_articles = db.relationship('SubArticle', backref='article', cascade="all, delete-orphan")
