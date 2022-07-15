# Langu

## Instructions to run

### Running the API

1. `cd api`
1. get some sentences ([from tatoeba](https://tatoeba.org/en/downloads))
1. use `tsv_to_db.py` to put them into sqlite database
1. `pip install -r requirements.txt`
1. `gunicorn sentences_api:app`

### Developing the front end

1. `cd langu`
1. `npm install`
1. `npm run dev`
