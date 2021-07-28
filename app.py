from flask import Flask, render_template
app = Flask(__name__)

player = "勇者"

# メニュー, /, メニューを表示
@app.route("/")
def menu():
    return render_template("menu.html", player = player)

# あるく, /walk, 荒野を歩いていた。
@app.route("/walk")
def walk():
    message = player + "は荒野を歩いていた。"
    return render_template("action.html", player = player, message = message)

# たたかう, /attack, モンスターと戦った。
@app.route("/attack")
def attack():
    message = player + "はモンスターと戦った。"
    return render_template("action.html", player = player, message = message)

## この下に「/say_hello」というパスで「Hello Flask」と表示する
@app.route("/say_hello")
def hello():
    message = "Hello Flask"
    return render_template("action.html", player = player, message = message)
