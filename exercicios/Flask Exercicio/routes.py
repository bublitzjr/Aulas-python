from flask import Flask, request, render_template, redirect

app = Flask(__name__)

pessoa = dict(nome="Jeff", idade=22)

@app.route("/")
def index():    
    return redirect("/read/")

@app.route("/read/")
def read():
    return render_template("index.html", pessoa=dict(pessoa))

if __name__ == "__main__":
    app.run(debug=True)