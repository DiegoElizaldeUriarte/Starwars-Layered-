import os
from flask import Flask, jsonify
import businessLogic

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def list_movies():
    movies = businessLogic.get_movies()
    return jsonify(movies)


@app.route("/characters/<int:movie_id>", methods=['GET'])
def list_characters(movie_id):
    characters = businessLogic.get_characters(movie_id)
    return jsonify(characters)


if __name__ == "__main__":
    app.run()
