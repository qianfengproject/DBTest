from flask import Blueprint, request

from App.ext import db
from App.models import Cat

blue = Blueprint('blue',__name__)
def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'O(∩_∩)O哈哈~'

#添加：
@blue.route('/add/')
def add():
    cat = Cat()
    cat.name = 'Tom猫'
    db.session.add(cat)
    db.session.commit()
    return "添加成功"


@blue.route('/updata/')
def updata():
    id = request.args.get('id')
    name = request.args.get('name')

    cat = Cat.query.get(id)
    cat.name = name
    db.session.add(cat)
    db.session.commit()
    return 'updata success !'
#删除
@blue.route('/drop/')
def drop():
    db.drop_all()
    return '删除成功'

# 查询
@blue.route('findall')
def findall():
    cats = Cat.query.all()
    for cat in cats:
        print(cat.name)
    return '查询成功'
