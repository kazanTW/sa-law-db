from flask_restful import Resource, reqparse
from ..models.law import Law
from ..utils.db import db

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Name cannot be blank.")
parser.add_argument('department', type=str, required=True, help="Department cannot be blank.")
parser.add_argument('last_amended', type=str, required=True, help="Last amended date cannot be blank.")

class LawResource(Resource):
    def get(self):
        laws = Law.query.all()
        return [{
            'id': law.id,
            'name': law.name,
            'department': law.department,
            'last_amended': law.last_amended
        } for law in laws], 200

    def post(self):
        args = parser.parse_args()
        new_law = Law(
            name=args['name'],
            department=args['department'],
            last_amended=args['last_amended']
        )
        db.session.add(new_law)
        db.session.commit()
        return {'message': 'Law added successfully'}, 201
