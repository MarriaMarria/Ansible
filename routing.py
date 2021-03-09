from flask import Flask, render_template
from connection_db import *
# standart logging configuration for flask
from logging.config import dictConfig
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
# logging end

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/test/', methods=['GET'])
def test_increment():
    result = conn.increment()
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)


#      sudo -u postgres psql postgres     apres==> \password postgres    apres tu met me mot de passe ==> \q     pour sortir
# [3:04 PM]
# et apres    sudo service postgresql restart