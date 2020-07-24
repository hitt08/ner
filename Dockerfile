FROM tiangolo/uwsgi-nginx-flask:latest

COPY . /ner/
WORKDIR /ner/
RUN pip install spacy \
 && python3 -m spacy download en_core_web_sm \
 && python3 -m spacy download en_core_web_md \
 && python3 -m spacy download en_core_web_lg
CMD ["python3", "rest.py"]