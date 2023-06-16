FROM python:3.11
WORKDIR /app

# gunicorn prepends SCRIPT_NAME to the paths, so we can GET
# http://localhost:8000/langu/api/sentence/random instead of
# http://localhost:8000/sentence/random
ENV SCRIPT_NAME=/langu/api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY sentences.db *.py /app/

CMD gunicorn sentences_api:app --bind 0.0.0.0:8000
