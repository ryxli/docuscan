from flask import Flask
from flask_cors import CORS
import sys
from finder import get_phrases
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'
@app.route('/calc/<text>')
def do_it(text):
	text=text.replace("%20"," ")
	print(text,file=sys.stderr)
	return "\n".join(get_phrases(text))