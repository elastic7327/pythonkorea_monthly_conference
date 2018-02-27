
from flask import Flask

from flask_jwt import JWT, jwt_required, current_identity

from src.models.user import User
from src.database import ENGINE, session, init_db

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'super-secret'
# app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
# app.config['JWT_AUTH_USERNAME_KEY'] = 'username'
# app.config['JWT_AUTH_PASSWORD_KEY'] = 'password'

def authenticate(username, password):
    user = session.query(
                User
            ).filter(
                User.username==username
            ).filter(
                User.password==password
            ).one()

    return user

def identity(payload):
    user_id = payload['identity']
    user = session.query(User).get(user_id)
    return user.id

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def hello_jwt():
    return 'jwt!'

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

if __name__ == '__main__':
    app.run()
