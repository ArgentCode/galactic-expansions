BUILDING_CONFIGS = {
    "metal_mine": {
        "base_production": 30,
        "multiplier": 1.25,
        "energy_consumption": 10,
        "energy_mod": 1.1,
        "metal_cost": 150,
        "crystal_cost": 0,
        "deuterium_cost": 0,
        "upgrade_time": 30
    },
    "crystal_mine": {
        "base_production": 25,
        "multiplier": 1.2,
        "energy_consumption": 12,
        "energy_mod": 1.2,
        "metal_cost": 200,
        "crystal_cost": 100,
        "deuterium_cost": 0,
        "upgrade_time": 30
    },
    "deuterium_mine": {
        "base_production": 20,
        "multiplier": 1.15,
        "energy_consumption": 15,
        "energy_mod": 1.25,
        "metal_cost": 300,
        "crystal_cost": 150,
        "deuterium_cost": 0,
        "upgrade_time": 30
    },
    "solar_plant": {
        "base_production": 0,
        "multiplier": 0,
        "energy_consumption": -50, # wait, but then we need to flip the signs again
        "energy_mod": 1.75,
        "metal_cost": 150,
        "crystal_cost": 75,
        "deuterium_cost": 0,
        "upgrade_time": 30
    },
    "robotics_facility": {
        "base_production": 0,
        "multiplier": 0.95, # how much faster should building stuff be?
        "energy_consumption": 25,
        "energy_mod": 1.1,
        "metal_cost": 500,
        "crystal_cost": 250,
        "deuterium_cost": 125,
        "upgrade_time": 30
    },
    "research_lab": {
        "base_production": 0,
        "multiplier": 0.75, # how much faster should researching stuff be?
        "energy_consumption": 25,
        "energy_mod": 1.1,
        "metal_cost": 650,
        "crystal_cost": 225,
        "deuterium_cost": 200,
        "upgrade_time": 30
    },
    "shipyard": {
        "base_production": 0,
        "multiplier": 0,
        "energy_consumption": 25,
        "energy_mod": 1.1,
        "metal_cost": 500,
        "crystal_cost": 250,
        "deuterium_cost": 125,
        "upgrade_time": 30
    }
}