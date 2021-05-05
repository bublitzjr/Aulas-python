from flask import Flask, request, render_template, redirect
from controllers import orders

import json

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)