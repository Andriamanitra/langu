from itertools import groupby
import sqlite3


def get_sentence(ru_id: int) -> dict:
    with sqlite3.connect("sentences.db") as con:
        cur = con.cursor()
        cur.execute("SELECT txt FROM ru_sentences WHERE id = ?", (ru_id,))
        ru, = cur.fetchone()
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

def get_random_sentences(count: int) -> list[dict]:
    result = []
    if count < 1:
        # allowing negative counts would cause this to return
        # ALL sentences which would take a while :-)
        return result

    with sqlite3.connect("sentences.db") as con:
        cur = con.cursor()
        cur.execute("""
        SELECT ruid, rutxt, en_sentences.txt
        FROM 
          (SELECT id AS ruid, txt AS rutxt FROM ru_sentences ORDER BY RANDOM() LIMIT ?)
        INNER JOIN translations 
          ON ruid = translations.ru_id
        INNER JOIN en_sentences
          ON en_sentences.id = translations.en_id;
        """, (count,))
        for (ru_id, ru), grp in groupby(cur, lambda x: x[:2]):
            result.append({
                "ru_id": ru_id,
                "ru": ru.strip(),
                "en": [en.strip() for _ru_id, _ru, en in grp],
            })

    return result
