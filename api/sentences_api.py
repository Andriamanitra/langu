import flask
import sqlite3


app = flask.Flask(__name__)


def sentence_from_db(ru_id: int | None = None):
    with sqlite3.connect("sentences.db") as con:
        cur = con.cursor()
        if ru_id:
            cur.execute("SELECT txt FROM ru_sentences WHERE id = ?", (ru_id,))
            ru, = cur.fetchone()
        else:
            cur.execute("SELECT id, txt FROM ru_sentences ORDER BY RANDOM() LIMIT 1")
            ru_id, ru = cur.fetchone()
        cur.execute("""
            SELECT txt
            FROM translations
                INNER JOIN en_sentences
                ON id = en_id
            WHERE ru_id = ?
            """, (ru_id,))
        en_sentences = [x.strip() for (x,) in cur.fetchall()]
    return {
        "ru_id": ru_id,
        "ru": ru.strip(),
        "en": en_sentences
    }


@app.route("/sentence/<int:ru_id>")
def sentence(ru_id):
    return sentence_from_db(ru_id)


@app.route("/sentence/random")
def random_sentence():
    return sentence_from_db()


@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
