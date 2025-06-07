
from flask import Flask
from models import db
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def home():
    return "<h1>eShop is running with external models!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
