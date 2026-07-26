from flask import Flask, request, jsonify
import main

app = Flask(__name__)

players = {
    1: main.Player("First Guy", 1)
}

@app.route('/')
def hello_world():
    return "hello world"

# TODO add post route for /players, creates a new player, appends to players array
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
    bigstring = ""
    for player in players:
        bigstring += player.__str__()
    return bigstring

if __name__ == '__main__':
    app.run()