import datetime as dt
import json

def tick(player):
    now = dt.datetime.now()
    lastTick = player.lastTick
    timeDelta = now - lastTick
    player.lastTick = now
    energy_bad = player.energy < 0
    minutes = timeDelta.total_seconds()
    # metal
    # if mine is in normal conditions, update materials. Else, upgrade mine and calculate the
    # old and new rates
    # LastUpgradeTime is when the most recent upgrade finishes (Can be future, now, or past)

    if player.SolarPlant.lastUpgradeTime < lastTick and player.SolarPlant.upgrading:
        player.SolarPlant.upgradeFinalise(player)

    if player.metalMine.lastUpgradeTime < lastTick or player.metalMine.lastUpgradeTime > now:
        player.metal += apply_resource(minutes, player.metalMine, energy_bad)
    else:
        oldRateTime = player.metalMine.lastUpgradeTime - lastTick
        minutes = oldRateTime.total_seconds()
        player.metal += apply_resource(minutes, player.metalMine, energy_bad)
        player.metalMine.upgradeFinalise(player)
        newRateTime = now - player.metalMine.lastUpgradeTime
        minutes = newRateTime.total_seconds()
        player.metal += apply_resource(minutes, player.metalMine, energy_bad)

    #crystal
    if player.crystalMine.lastUpgradeTime < lastTick or player.crystalMine.lastUpgradeTime > now:
        player.crystal += apply_resource(minutes, player.crystalMine, energy_bad)
    else:
        oldRateTime = player.crystalMine.lastUpgradeTime - lastTick
        minutes = oldRateTime.total_seconds()
        player.crystal += apply_resource(minutes, player.crystalMine, energy_bad)
        player.crystalMine.upgradeFinalise(player)
        newRateTime = now - player.crystalMine.lastUpgradeTime
        minutes = newRateTime.total_seconds()
        player.crystal += apply_resource(minutes, player.crystalMine, energy_bad)

    # ships?

    print(minutes, " Time has passed")
    # player.crystal += apply_resource(minutes, player.crystalMine.rate, energy_bad)
    # player.metal += apply_resource(minutes, player.metalMine.rate, energy_bad)
    # Check upgrades?

def apply_resource(minutes, mine, energy_bad):
    resource = round(minutes * mine.rate)
    if energy_bad:
        return round(resource * 0.2)
    else: 
        return resource


def calculate_energy(player):
    player.energy = (player.SolarPlant.energyConsumption + 
        player.metalMine.energyConsumption + 
        player.crystalMine.energyConsumption
    )


def print_status(player):
    print("Metal:", player.metal, " Crystal:",
          player.crystal, " Energy:", player.energy)
    print("Metal Mine:", player.metalMine.level,
          "Crystal Mine:", player.crystalMine.level)
    print("Current upgrades....")


def status(player):
    status = {
        "name": player.name,

        "metal": player.metal,
        "crystal": player.crystal,
        "energy": player.energy,

        "Metal Mine Level": player.metalMine.level,
        "Metal Mine Rate": player.metalMine.rate,
        "Metal Mine Energy Consumption": player.metalMine.energyConsumption,

        "Crystal Mine Level": player.crystalMine.level,
        "Crystal Mine Rate": player.crystalMine.rate,
        "Crystal Mine Energy Consumption": player.crystalMine.energyConsumption,

        "Solar Plant Level": player.SolarPlant.level,
        "Solar Plant Rate": player.SolarPlant.rate,
        "Solar Plant Energy Consumption": player.SolarPlant.energyConsumption
    }
    return json.dumps(status)


class Mine:
    def __init__(self, rate, level, name, energy_mod = 1):
        self.level = level
        self.name = name
        self.rate = rate
        self.energyConsumption = -5 * self.level * energy_mod
        self.upgradeMetalCost = 100 * self.level
        self.upgradeCrystalCost = 75 * self.level
        self.upgradeTime = 10 * self.level
        self.lastUpgradeTime = dt.datetime.now()
        self.upgrading = False

    def upgradeInitiate(self, player):
        if (player.metal < self.upgradeMetalCost
            or player.crystal < self.upgradeCrystalCost
                or self.lastUpgradeTime > dt.datetime.now()):
            return False
        player.metal -= self.upgradeMetalCost
        player.crystal -= self.upgradeCrystalCost
        self.lastUpgradeTime = dt.datetime.now() + dt.timedelta(seconds=self.upgradeTime)
        self.upgradeMetalCost = 100 * self.level
        self.upgradeCrystalCost = 75 * self.level
        self.upgrading = True
        return True

    def upgradeFinalise(self, player):
        self.level += 1
        self.rate = 1.3 * self.rate
        self.energyConsumption = self.energyConsumption * 1.25
        self.upgradeTime = 10 * self.level
        self.upgrading = False
        calculate_energy(player)


class MetalMine(Mine):
    def __init__(self):
        super().__init__(50, 1, "Metal")


class CrystalMine(Mine):
    def __init__(self):
        super().__init__(35, 1, "Crystal")


class SolarPlant(Mine):
    def __init__(self, energy_mod = -2.1):
        super().__init__(0, 1, "SolarPlant", energy_mod)


class Ship:
    def __init__(self, name, hitpoints, armor, damage, type):
        self.name = name
        self.hitpoints = hitpoints
        self.armor = armor
        self.damage = damage
        self.type = type


class Player:
    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name
        self.metalMine = MetalMine()
        self.crystalMine = CrystalMine()
        self.SolarPlant = SolarPlant()
        self.metal = 1000
        self.crystal = 1000
        self.energy = 0.5
        self.lastTick = dt.datetime.now()

    def __str__(self):
        return f"name: {self.name}, id: {self.id}"


# if __name__ == "__main__":
#     main()
