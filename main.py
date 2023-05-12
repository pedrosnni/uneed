from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
