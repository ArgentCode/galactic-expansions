from flask import Flask, request, jsonify
from flask_cors import CORS
import main

app = Flask(__name__)

CORS(app, origins=["http://localhost:5173", "http://172.17.0.2:5173"], supports_credentials=True)

players = {
    1: main.Player("First Guy", 1),
    2: main.Player("Second Man", 2)
}

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/player', methods = ["POST"])
def newPlayer():
    # name = request.form.get("name")
    # id = request.form.get("id", type=int)
    data = request.get_json()
    name = data.get('name')
    id = int(data.get('id'))
    newPlayer = main.Player(name, id)
    players[id] = newPlayer
    return jsonify({
        "status": "success",
        "recieved": f"id: {id}, name: {name}"
    })

@app.route('/status')
def status():
    playerId = request.headers.get('player', type=int)
    player = players.get(playerId)
    if player is None:
        return f"could not find player: {playerId}"
    main.tick(player)
    return main.status(player)

@app.route('/dump')
def dump():
    bigstring = "["
    first = True
    for player in players:
        if(not first):
            bigstring += ','
        bigstring += f"{{\"id\":{player.__str__()}}}"
        first = False
    bigstring += "]"
    return bigstring


if __name__ == '__main__':
    app.run()