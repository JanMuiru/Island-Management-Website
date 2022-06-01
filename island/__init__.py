from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5


app = Flask(__name__, static_url_path='/static' )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///island.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='some very complex stuff mahn'
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)

from island import routes
