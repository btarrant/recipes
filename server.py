from flask_app import Flask


app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
