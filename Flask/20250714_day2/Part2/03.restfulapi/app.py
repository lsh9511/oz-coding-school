from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

items = [] # DB의 대체 역할

class Item(Resource) : 
    # 특정 아이템 조희
    def get(self, name):
        for item in items :
            if item['name'] == name :
                return item
        return {'message' : 'Item not found'}, 404
    # 특정 아이템 생성
    def post(self, name):
        for item in items : 
            if item['name'] == name :
                return {'message' : 'Item already exists'}, 400
        data = request.get_json()
        
        new_item = {'name' : data['name'], 'price' : data['price']}
        items.append(new_item)

        return new_item, 201
    # 아이템 업데이트
    def put(self, name):
        pass
    # 아이템 삭제
    def delete(self):
        pass
