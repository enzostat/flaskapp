from flask import Blueprint, render_template, request
from models.index import db
from bson.objectid import ObjectId

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/', methods=('POST'))
def index():
    