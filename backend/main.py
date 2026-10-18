import datetime as dt
import json
import time
from database import SessionLocal
from flask import Flask, jsonify, request
from models import Buildings, Player, Worlds


def create_new_player(session, empire_name: str) -> Player:
    new_player = Player(
        empire_name=empire_name,
        tech_espionage=0,
        tech_computer=0,
        tech_energy=0,
        tech_weapon=0,
        tech_armor=0,
        tech_shielding=0,
        tech_combustion=0,
        tech_impulse=0,
        tech_hyperspace=0,
        tech_laser=0,
        tech_ion=0,
        tech_plasma=0,
        last_tick=dt.datetime.now()
    )

    session.add(new_player)
    session.flush()

    new_world = create_new_world(session, new_player.player_id)

    return new_player


def create_new_world(session, player_id: int) -> Worlds:
    new_world = Worlds(
        player_id=player_id,
        metal=1000,
        crystal=750,
        deuterium=0,
        energy=0
    )

    session.add(new_world)
    session.flush()
    initial_buildings = [
        Buildings(
            world_id=new_world.world_id, building_type="metal_mine", level=0
        ),
        Buildings(
            world_id=new_world.world_id, building_type="crystal_mine", level=0
        ),
        Buildings(
            world_id=new_world.world_id, building_type="solar_plant", level=0
        ),
    ]
    session.add_all(initial_buildings)
    session.flush()

    return new_world


def get_player_status(player: Player) -> json:
    json_status = jsonify({
        "empire_name": player.empire_name,
        "research": {
            "tech espionage": player.tech_espionage,
            "tech computer": player.tech_computer,
            "tech energy": player.tech_energy,
            "tech weapon": player.tech_weapon,
            "tech armor": player.tech_armor,
            "tech shielding": player.tech_shielding,
            "tech combustion": player.tech_combustion,
            "tech impulse": player.tech_impulse,
            "tech hyperspace": player.tech_hyperspace,
            "tech laser": player.tech_laser,
            "tech ion": player.tech_ion,
            "tech plasma": player.tech_plasma,
        },
        "worlds": [
            {
                "world_name": w.world_name,
                "world_id": w.world_id,
                "metal": w.metal,
                "crystal": w.crystal,
                "deuterium": w.deuterium,
                "energy": w.energy,
            }
            for w in player.worlds
        ],
    })
    return json_status


def get_world_status(world: Worlds) -> json:

    json_status = jsonify({
        "world name": world.world_name,
        "world id": world.world_id,
        "resources": [
            {
                "metal": world.metal,
                "crystal": world.crystal,
                "deuterium": world.deuterium,
                "energy": world.energy,
            }
        ],
        "buildings": [
            {
                "building_type": b.building_type, "level": b.level
            }
            for b in world.buildings
        ],
    })
    return json_status
