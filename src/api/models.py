from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # gives error: sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) column "access_token" contains null values
    access_token = db.Column(db.String(80), unique=True, null=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.lastname,
            "username": self.username,
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }

# Allow CORS for all domains
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     return response
# if __name__ == '__main__':
#     app.run(debug=True)