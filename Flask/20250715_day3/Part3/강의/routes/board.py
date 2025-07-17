from flask import request, jsonify
from flask_restful import Blueprint
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description = 'Operations on boards', url_prefix='/boards')

@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
        for board in boards:
            print('id',board.id)
            print('title',board.title)
            print('content',board.content)
            print('user_id',board.user_id)
            print('author',board.author)