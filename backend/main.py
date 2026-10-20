import datetime as dt
import json
import time
from database import SessionLocal
from flask import Flask, jsonify, request
from models import Buildings, Player, Worlds
from config import *


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
    current_time = dt.datetime.now()
    initial_buildings = [
        Buildings(
            world_id=new_world.world_id, building_type="metal_mine", level=1, completion_time=current_time
        ),
        Buildings(
            world_id=new_world.world_id, building_type="crystal_mine", level=0, completion_time=None
        ),
        Buildings(
            world_id=new_world.world_id, building_type="deuterium_mine", level=0, completion_time=None
        ),
        Buildings(
            world_id=new_world.world_id, building_type="solar_plant", level=1, completion_time=current_time
        ),
    ]
    session.add_all(initial_buildings)
    session.flush()

    return new_world


def get_player_status(current_tick: dt.datetime, player: Player) -> json:
    player_tick(current_tick, player)
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


def get_world_status(current_tick: dt.datetime, player: Player, world: Worlds) -> json:
    player_tick(current_tick, player)
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


def player_tick(current_tick: dt.datetime, player: Player) -> None:
    """
    So my idea to handle tick functions is basically to grab all of the events inside a player's scope,
    then put them in a sorted array. From there I will pop the event, run the calculations for resources
    and anything else between last_tick and the popped event, then update the needed building/research/fleet
    then continue until the array ends. 
    This has the benefit of saving us from a never endingly complex series of if statements to check for
    every possible event change imaginable.
    """

    print("Starting event queue")
    event_queue = []
    for world in player.worlds:
        for building in world.buildings:
            if (building.completion_time is not None
                    and building.completion_time > player.last_tick
                    and building.completion_time < current_tick):
                event_queue.append({
                    "timestamp": building.completion_time,
                    "type": "building_upgrade",
                    "target": building,
                    "world": world,
                })

    event_queue.sort(key=lambda x: x["timestamp"])

    event_queue.append({
        "timestamp": current_tick,
        "type": "current_tick",
        "target": None,
        "world": None,
    })

    print("looping event queue")
    for event in event_queue:
        # calculate resources, then do the upgrade.
        resource_tick(event["timestamp"], player)


def resource_tick(current_tick: dt.datetime, player: Player) -> None:
    print("Starting resource tick")
    time_delta = (current_tick - player.last_tick).total_seconds()
    for world in player.worlds:
        metal_production = 0
        crystal_production = 0
        deuterium_production = 0
        for building in world.buildings:
            if building.building_type == "metal_mine" and building.level > 0:
                config = MINE_CONFIGS['metal_mine']

                production = (
                    config["base_production"]
                    * building.level
                    * (config["multiplier"] ** building.level)
                ) * time_delta
                metal_production += production

            elif building.building_type == "crystal_mine" and building.level > 0:
                config = MINE_CONFIGS['crystal_mine']

                production = (
                    config["base_production"]
                    * building.level
                    * (config["multiplier"] ** building.level)
                ) * time_delta
                crystal_production += production

            elif building.building_type == "deuterium_mine" and building.level > 0:
                config = MINE_CONFIGS['deuterium_mine']

                production = (
                    config["base_production"]
                    * building.level
                    * (config["multiplier"] ** building.level)
                ) * time_delta
                deuterium_production += production
        if world.energy < 0:
            metal_production *= 0.25
            crystal_production *= 0.25
            deuterium_production *= 0.25

        world.metal += metal_production
        world.crystal += crystal_production
        world.deuterium += deuterium_production
