# insert tsv data (as downloaded from https://tatoeba.org/en/downloads)
# into sqlite database file sentences.db

import sqlite3


CREATE_RU_SENTENCES_TABLE = """
CREATE TABLE IF NOT EXISTS ru_sentences(
    id integer primary key,
    txt varchar
)
"""

CREATE_EN_SENTENCES_TABLE = """
CREATE TABLE IF NOT EXISTS en_sentences(
    id integer primary key,
    txt varchar
)
"""

CREATE_TRANSLATIONS_TABLE = """
CREATE TABLE IF NOT EXISTS translations(
    ru_id INTEGER REFERENCES ru_sentences(id),
    en_id INTEGER REFERENCES en_sentences(id)
)
"""


def lines(fname: str):
    with open(fname, "r") as f:
        for line in f:
            ru_id, ru, en_id, en = line.split("\t")
            # print(f"{ru_id!r}\n\n{ru!r}\n\n{en_id!r}\n\n{en!r}\n\n")
            yield int(ru_id), ru, int(en_id), en


def main():
    with sqlite3.connect("sentences.db") as con:
        con.execute(CREATE_RU_SENTENCES_TABLE)
        con.execute(CREATE_EN_SENTENCES_TABLE)
        con.execute(CREATE_TRANSLATIONS_TABLE)
        for ru_id, ru, en_id, en in lines("sentence_pairs_2022-07-14.tsv"):
            con.execute("INSERT OR IGNORE INTO en_sentences VALUES (?, ?)", (en_id, en))
            con.execute("INSERT OR IGNORE INTO ru_sentences VALUES (?, ?)", (ru_id, ru))
            con.execute("INSERT OR IGNORE INTO translations VALUES (?, ?)", (ru_id, en_id))


if __name__ == "__main__":
    main()
