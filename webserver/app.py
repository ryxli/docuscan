from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import uuid
from finder import get_phrases

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

DOCUMENTS = []

@app.route('/documents', methods=['GET', 'POST'])
def all_docs():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        DOCUMENTS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'size': post_data.get('size'),
            'base64': post_data.get('base64'),
            'file': post_data.get('file')
        })
        response_object['message'] = 'Document Added'
    else:
        response_object['documents'] = DOCUMENTS
    return jsonify(response_object)

@app.route('/documents/<doc_id>', methods=['DELETE'])
def single_doc(doc_id):
    response_object = {'status': 'success'}
    if request.method == 'DELETE':
        remove_doc(doc_id)
        response_object['message'] = 'Doc removed'
    return jsonify(response_object)

def remove_doc(doc_id):
    for doc in DOCUMENTS:
        if doc['id'] == doc_id:
            DOCUMENTS.remove(book)
            return True
        return False

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/calc/<text>')
def do_it(text):
	text=text.replace("%20"," ")
	print(text,file=sys.stderr)
	return "\n".join(get_phrases(text))

if __name__ == '__main__':
    app.run()
