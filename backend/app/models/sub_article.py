from ..utils.db import db

class SubArticle(db.Model):
    __tablename__ = 'sub_articles'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
