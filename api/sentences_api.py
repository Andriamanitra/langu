import flask
import db

app = flask.Flask(__name__)


@app.route("/sentence/<int:ru_id>")
def sentence(ru_id):
    sentence = db.get_sentence(ru_id)
    return flask.jsonify(sentence)


@app.route("/sentence/random")
def random_sentence():
    count = flask.request.args.get("count", default=1, type=int)
    if count > 100:
        return "You don't need that many sentences (max=100)", 400
    sentences = db.get_random_sentences(count)
    return flask.jsonify(sentences)


@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
