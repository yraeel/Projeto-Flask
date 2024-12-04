from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = 'Israel Machado'
    return render_template('index.html', nome=nome)


@app.route('/contato')
def contato():
    return render_template('contato.html')