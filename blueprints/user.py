from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from models.index import db
from bson.objectid import ObjectId

user_blueprint = Blueprint('characters', __name__, url_prefix='/characters')

@character_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        user = list(db.users.find())
        print(characters, len(characters))
        return render_template('users/index.html', users=user)
    elif request.method == 'POST':
        name = request.form['name']
        print('You typed the name:', name)
        langs = [x.strip() for x in request.form['languages'].split(',')]
        db.users.insert_one({
            'name': request.form['name'],
            'image': request.form['image'],
            'languages': langs,
            'birthday': date,
            'bio': request.form['bio']
        })
        return redirect('/characters')
