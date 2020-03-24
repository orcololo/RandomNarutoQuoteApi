from flask import Flask
from flask_restful import Resource, Api
from quotes import randomNarutoQuote

app = Flask(__name__)
api = Api(app)


class quoteNaruto(Resource):
    def get(self):
        return randomNarutoQuote.getQuote()


api.add_resource(quoteNaruto, '/')
if __name__ == '__main__':
    app.run()x''
