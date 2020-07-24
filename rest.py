from ner import NER
from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)
ner_model=NER("en_core_web_sm")

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/ner", methods=["GET","POST"])
def ner_request():
    if request.method == "POST":
        req = request.get_json()
        if(req["version"]==1):
            entity_mentions=ner_model.spacy_ner(req["content"])
            return jsonify({"entities": entity_mentions})
        else:
            return "The current version is not supported."
    elif request.method == "GET":
        return "Hello World from NER!"

if __name__ == '__main__':
    app.run()


#JSON
# {
#     "version": 1,
# 	"content": "Something to parse"
# }
#
# {
#     "version": 1,
# 	"content": [
# 		"String 1",
# 		"String 2"
# 	]
# }
