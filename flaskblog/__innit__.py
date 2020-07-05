from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a93kfialeofp0283ixmb7fj3kgyth27f'

from flaskblog import route