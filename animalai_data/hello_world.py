from flask import Flask

app = Flask(__name__)

@app.route('/')
def dello_world():
	return 'Hello World'