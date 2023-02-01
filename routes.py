from bottle import request, response
from bottle import post, get, put, delete
import json, sys

from comparison_model import similarity

@post('/compare')
def compare_handler():
    try: 
        data = request.json
    except:
        raise ValueError
    
    if data is None:
        raise ValueError

    result = similarity(data["sentences1"],data["sentences2"])

    response.headers['Content-Type'] = 'application/json'
    return json.dumps(list_to_dict(result))

def list_to_dict(result):
    list = []
    for sentence1, sentence2, score in result:
        entry = {
            "sentence1": sentence1,
            "sentence2": sentence2,
            "score": score
        }
        
        list.append(entry)
    
    return list