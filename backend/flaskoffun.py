from flask import Flask, request, jsonify
from flask_cors import CORS
import main

app = Flask(__name__)

CORS(app, origins=["http://localhost:5173",
     "http://172.17.0.2:5173"], supports_credentials=True)

players = {
    1: main.Player("First Guy", 1),
    2: main.Player("Second Man", 2)
}


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/player', methods=["POST"])
def newPlayer():
    data = request.get_json()
    name = data.get('name')
    id = int(data.get('id'))
    if id in players:
        return jsonify({
            "status": "FAILED, duplicate ID",
            "recieved": f"id: {id}, name: {name}"
        })
    newPlayer = main.Player(name, id)
    players[id] = newPlayer
    return jsonify({
        "status": "Success",
        "recieved": f"id: {id}, name: {name}"
    })


@app.route('/upgradeMine', methods=["POST"])
def upgradeMine():
    data = request.get_json()
    id = int(data.get('id'))
    mine = data.get('mine')
    idCheck(id)
    player = players.get(id)
    if mine.lower() == "m" or mine.lower() == "metal":
        success = player.metalMine.upgrade(player)
    if mine.lower() == "c" or mine.lower() == "crystal":
        success = player.crystalMine.upgrade(player)
    if success:
        return jsonify({
            "status": "Success",
            "recieved": f"Upgraded the {mine} mine for player {id}"
        })
    else:
        return jsonify({
            "status": "FAILED",
            "recieved": f"Player {id} did not have enough resources to upgrade the {mine} mine"
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
        if (not first):
            bigstring += ','
        bigstring += f"{{\"id\":{player.__str__()}}}"
        first = False
    bigstring += "]"
    return bigstring


def idCheck(playerID):
    if playerID not in players:
        return jsonify({
            "status": "FAILURE",
            "recieved": f"ID: {playerID} not found"
        })


if __name__ == '__main__':
    app.run()
