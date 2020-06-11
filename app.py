from flask import Flask, render_template
from utils import main

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('results.html')


if __name__ == '__main__':
    main()
    app.run(debug=True)
