import datetime as dt
import json
# import sqlalchemy # calls to database
# import flask # api calls to front end


def main():
    # Your core program logic goes here
    print("Welcome to Galactic Expansions")
    name = input("Name your empire: ")
    newPlayer = Player(name)
    while True:
        tick(newPlayer)
        status(newPlayer)
        choice = input(
            "What would you like to do? m to upgrade metal mine, c to upgrade crystal mine, x to exit ")
        if choice.lower() == "x" or choice.lower == "exit":
            print("Thanks for playing!")
            exit()
        elif choice.lower() == "m":
          #  newPlayer.metalMine.upgrade(newPlayer)
            print("Metal Mine upgraded!")
        elif choice.lower == "c":
          #  newPlayer.crystalMine.upgrade(newPlayer)
            print("Crystal Mine upgraded!")
        else:
            print("I didn't quite get that. Try again,")


def tick(player):
    now = dt.datetime.now()
    lastTick = player.lastTick
    timeDelta = now - lastTick
    player.lastTick = now
    minutes = timeDelta.total_seconds()
    # metal
    # if mine is in normal conditions, update materials. Else, upgrade mine and calculate the
    # old and new rates
    if player.metalMine.lastUpgradeTime < lastTick or player.metalMine.lastUpgradeTime > now:
        player.metal += round(minutes * player.metalMine.rate)
    else:
        oldRateTime = player.metalMine.lastUpgradeTime - lastTick
        minutes = oldRateTime.total_seconds()
        player.metal += round(minutes * player.metalMine.rate)
        player.metalMine.upgradeFinalise(player)
        newRateTime = now - player.metalMine.lastUpgradeTime
        minutes = newRateTime.total_seconds()
        player.metal += round(minutes * player.metalMine.rate)

    #crystal
    if player.crystalMine.lastUpgradeTime < lastTick or player.crystalMine.lastUpgradeTime > now:
        player.crystal += round(minutes * player.crystalMine.rate)
    else:
        oldRateTime = player.crystalMine.lastUpgradeTime - lastTick
        minutes = oldRateTime.total_seconds()
        player.crystal += round(minutes * player.crystalMine.rate)
        player.crystalMine.upgradeFinalise(player)
        newRateTime = now - player.crystalMine.lastUpgradeTime
        minutes = newRateTime.total_seconds()
        player.crystal += round(minutes * player.crystalMine.rate)

    # ships?

    print(minutes, " Time has passed")
    player.crystal += round(minutes * player.crystalMine.rate)
    player.metal += round(minutes * player.metalMine.rate)
    # Check upgrades?


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
        "Crystal Mine Level": player.crystalMine.level,
    }
    return json.dumps(status)


class Mine:
    def __init__(self, rate, level, name):
        self.level = level
        self.name = name
        self.rate = rate
        self.energyConsumption = 5 * self.level
        self.upgradeMetalCost = 100 * self.level
        self.upgradeCrystalCost = 75 * self.level
        self.upgradeTime = 10 * self.level
        # 1 is available, 0 is out of comission (destroyed), 2 is upgrading (cannot be upgraded again)
        self.status = 0
        self.lastUpgradeTime = dt.datetime.now()

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
        self.energyConsumption = 5 * self.level
        self.upgradeTime = 10 * self.level
        return True

    def upgradeFinalise(self, player):
        self.level += 1
        self.rate = 1.3 * self.rate


class MetalMine(Mine):
    def __init__(self):
        super().__init__(50, 1, "Metal")


class CrystalMine(Mine):
    def __init__(self, level=1):
        super().__init__(35, 1, "Crystal")


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
        self.metal = 1000
        self.crystal = 1000
        self.energy = 50
        self.lastTick = dt.datetime.now()

    def __str__(self):
        return f"name: {self.name}, id: {self.id}"


# if __name__ == "__main__":
#     main()
