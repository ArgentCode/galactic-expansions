import time
from database import SessionLocal
from flask import Flask, jsonify, request
from models import Buildings, Player, Worlds
from main import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/player/status', methods=['GET'])
def player_status():
    session = SessionLocal()
    player_id = request.headers.get('player-id', type=int)
    try:
        if not player_id:
            return jsonify({"error": "Missing player_id header"}), 400

        player = session.query(Player).filter_by(player_id=player_id).first()
        if not player:
            return jsonify({"error": "Player not found"}), 404

        current_time = int(time.time())
        # player_tick(player)
        json_status = get_player_status(player)
        # TODO: Tick the player
        session.commit()  # 5. Return success JSON
        return (json_status, 200)

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()


@app.route('/world/status', methods=['GET'])
def world_status():
    session = SessionLocal()
    player_id = request.headers.get('player-id', type=int)
    world_id = request.headers.get('world-id', type=int)
    try:
        if not player_id or not world_id:
            return jsonify({"error": "Missing player-id or world-id header"}), 400

        world = session.query(Worlds).filter_by(
            player_id=player_id, world_id=world_id).first()
        if not world:
            return jsonify({"error": "World not found"}), 404

        current_time = int(time.time())
        # player_tick(player)
        json_status = get_world_status(world)
        # TODO: Tick the player
        session.commit()  # 5. Return success JSON
        return (json_status, 200)

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()


@app.route('/player/create', methods=["POST"])
def new_player():
    session = SessionLocal()
    data = request.get_json()
    empire_name = data.get('name')
    try:
        # Check if the empire name is already taken
        existing_player = session.query(Player).filter_by(
            empire_name=empire_name).first()
        if existing_player:
            return jsonify({"error": "Empire name is already taken"}), 400

        new_player = create_new_player(session, empire_name)
        session.add(new_player)
        session.commit()

        return (
            jsonify(
                {
                    "success": True,
                    "message": f"Empire '{empire_name}' created successfully!",
                    "player_id": new_player.player_id,
                }
            ),
            201,
        )

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()


@app.route('/player/remove', methods=["DELETE"])
def remove_player():
    session = SessionLocal()
    player_id = request.headers.get('player-id', type=int)
    admin_id = request.headers.get('admin-id', type=int)

    try:
        if not player_id or not admin_id:
            return jsonify({"error": "Missing player-id or admin-id header"}), 400
        player = session.query(Player).filter_by(player_id=player_id).first()
        if not player:
            return jsonify({"error": "Player not found"}), 404
        if admin_id != 123:
            return jsonify({"error": "Access Denied"}), 403
        empire_name = player.empire_name

        session.delete(player)
        session.commit()
        return (
            jsonify(
                {
                    "success": True,
                    "message": (
                        f"Empire '{empire_name}' (ID: {player_id}) and all"
                        " associated worlds/buildings have been obliterated from the records. They shall never be heard from again."
                    ),
                }
            ),
            200,
        )

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()
