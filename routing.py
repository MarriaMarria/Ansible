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

# welcome visitors
@app.route('/', methods=['GET'])
def test():
    return render_template('index.html')

# increment visitors +1
@app.route('/plus/', methods=['GET'])
def test_increment():
    cursor.execute("UPDATE testing SET ID = ID + 1")
    conn.commit()
    return "We got +1, jipiii!"

# show id 
@app.route('/id/', methods=['GET'])
def show_id(): 
    cursor.execute("SELECT ID FROM testing")
    conn.commit()
    result = cursor.fetchall()

    return str(result[0][0])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
