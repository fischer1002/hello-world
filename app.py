# import Flask class 
from flask import Flask

# create app, which is a Flask instance
app = Flask(__name__)

# create index method
@app.route("/")
def index():
    return "Hello World!"

# run flask app
if __name__ == "__main__":
    app.run()
