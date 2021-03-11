from flask import Flask
import random 

app = Flask(__name__)

@app.route('/api')
def index():
	return str(random.randint(1,100))

if __name__ == '__main__':
	app.run(host = "0.0.0.0", port = 5000)