from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engin = create_engine("postgresql://admin:admin@postgres:5432/mydb")

Base = declarative_base()

class Word(Base):
	__tablename__ = 'word'
	id = Column(Integer,primary_key=True)
	word = Column(String(100))

Base.metadata.create_all(engin)

Session = sessionmaker(bind=engin)
session = Session()

@app.route('/api', methods=['POST','GET'])
def index_flask():
	data = session.query(Word).all()
	print("data")
	return render_template('index_flask.html', data=data)

@app.route('/word', methods=['POST'])
def word():
	word = request.form['word']
	print(word)
	input_word = Word(word=word)
	session.add(input_word)
	session.commit()
	return redirect(url_for('index_flask'))

@app.route('/reset', methods=['POST'])
def reset():
	session.query(Word).delete()
	return redirect(url_for('index_flask'))


if __name__ == '__main__':
	app.run(host = "0.0.0.0", port = 5000)