#!/usr/bin/env python3

# from flask import Flask, jsonify, make_response
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# from models import db, User, Review, Game

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# @app.route('/')
# def index():
#     return "Index for Game/Review/User API"


# @app.route('/games')
# def games():

#     games = []
#     for game in Game.query.all():
#         game_dict = {
#             "title" : game.title,
#             "genre" : game.genre,
#             "platform" : game.platform,
#             "price" : game.price,
#         }
#         games.append(game_dict)

#     response = make_response(
#         jsonify(games),
#         200,
#         {"Content-Type" : "application/json"}
#     )

#     return response


# @app.route('/games/<int:id>')
# def game_by_id(id):
#     game = Game.query.filter(Game.id == id).first()

#     game_dict = game.to_dict()
#     # {
#     #     "title": game.title,
#     #     "genre": game.genre,
#     #     "platform": game.platform,
#     #     "price": game.price,
#     # }

#     response = make_response(
#         jsonify(game_dict),
#         200
#     )
#     response.headers["Content-Type"] = "application/json"

#     return response

# # @app.route('/example')
# # def sandbox():

# #     games = []
# #     for game in Game.query.order_by(Game.title).all():
# #         game_dict = {
# #             "title" : game.title,
# #             "genre" : game.genre,
# #             "platform" : game.platform,
# #             "price" : game.price,
# #         }
# #         games.append(game_dict)
    
# #     response = make_response(
# #         jsonify(games),
# #         200
# #     )

# #     return response


# # @app.route('/example2')
# # def sandbox2():
# #     games = []

# #     for game in Game.query.limit(10).all():
# #         game_dict = {
# #             "title" : game.title,
# #             "genre" : game.genre,
# #             "platform" : game.platform,
# #             "price" : game.price,
# #         }
# #         games.append(game_dict)

# #         response = make_response(
# #             jsonify(games),
# #             200
# #         )
# #         return response





# if __name__ == '__main__':
#     app.run(port=5555, debug=True)



from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"

@app.route('/games')
def games():

    games = []
    for game in Game.query.all():
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        games.append(game_dict)

    response = make_response(
        games,
        200
    )

    return response

@app.route('/games/<int:id>')
def game_by_id(id):
    game = Game.query.filter(Game.id == id).first()

    game_dict = game.to_dict()

    response = make_response(
        game_dict,
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)