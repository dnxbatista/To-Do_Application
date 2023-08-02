from flask import Flask, render_template, jsonify, request , redirect, url_for
import json

app = Flask(__name__, template_folder="templates")

toDoList = []

@app.route("/")
def home():
    return render_template("index.html", itens=toDoList)

@app.route("/add", methods=["POST"])
def add():
    todoItem = request.form["item-input-name"]
    if(len(todoItem) <= 1): return redirect(url_for("home"))
    toDoList.append({"item": todoItem})
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete(index):
    del toDoList[index]
    return redirect(url_for("home"))

@app.route("/api/itens")
def itens_list():
    return jsonify(toDoList)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)