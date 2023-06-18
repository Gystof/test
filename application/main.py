from dotenv import load_dotenv
load_dotenv('../config.env')


from flask import Flask
from backend import backend



app = Flask(__name__)
app.config['SECRET_KEY'] = 'database_secret_key'
app.register_blueprint(
    backend,
    url_prefix='/admin'
)


@app.route('/')
@app.route('/index')
def index():
    return '<h1>Home</h1>'


if __name__ == '__main__':
    app.run(port=5001, debug=True)