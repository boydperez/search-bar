import os
from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "some secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

db = SQLAlchemy(app)


class User(db.Model):
    """
    User model.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<User '{self.username}'>"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getdata')
def get_data():
    user = request.args.get('username')

    if user:
        user_objects = User.query.filter(User.username.startswith(user)).all()
        users = {'usernames': [user.username for user in user_objects]}
        return jsonify(users) 
    else:
        users = {'usernames': 'NO_ARGS'}
        return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
