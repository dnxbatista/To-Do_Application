from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

toDoList = [
    {
        'item': 'Buy Food!'
    },
]

@app.route("/")
def home():
    return render_template("index.html",itens=toDoList)

@app.route("/", methods=["post"])
def form_post():
    text = request.form["item-input-name"]
    return text

@app.route("/api/itens")
def itens_list():
    return jsonify(toDoList)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)