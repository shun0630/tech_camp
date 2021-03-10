from flask import Flask
import random


app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello world'

@app.route('/random')
def random_num():
	return str(random.randint(1,100))


if __name__ == '__main__':
	app.run(host='0.0.0.0' , port=5000)