from flask import Flask, request, render_template, redirect

app = Flask(__name__)

pessoa = dict(nome="Gustavo", idade=100)

@app.route("/")
def index():
    return redirect("/read/")

@app.route("/read/")
def read():
    return render_template("index.html", pessoa=pessoa)

if __name__ == "__main__":
    app.run(debug=True)