import datetime as dt

def main():
    # Your core program logic goes here
    print("Welcome to Galactic Expansions")
    name = input("Name your empire: ")
    newPlayer = Player(name)
    while True:
       tick(newPlayer)
       status(newPlayer)
       choice = input("What would you like to do? m to upgrade metal mine, c to upgrade crystal mine, x to exit ")
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
   timeDelta = dt.datetime.now() - player.lastTick
   minutes = timeDelta.total_minutes()
   print(minutes, " Time has passed")
   player.crystal += minutes * player.crystalMine.rate
   player.metal += minutes * player.metalMine.rate
   # Check upgrades?


def status(Player):
   print("Metal:", Player.metal, " Crystal:", Player.crystal, " Energy:", Player.energy)
   print("Metal Mine:", Player.metalMine.level, "Crystal Mine:", Player.crystalMine.level)
   print("Current upgrades....")


class Mine:
  def __init__(self, rate, level, name):
      self.level = level
      self.name = name
      self.rate = rate
      self.energyConsumption = 5 * self.level
      self.upgradeMetalCost = 100 * self.level
      self.updateCrystalCost = 75 * self.level
      self.upgradeTime = 10 * self.level
      self.status = 0 # 1 is available, 0 is out of comission (destroyed), 2 is upgrading (cannot be upgraded again)

  def upgrade(self, Player):
      Player.metal -= self.upgradeMetalCost
      Player.crystal -= self.updateCrystalCost
      self.level += 1
      self.rate = self.rate
      self.upgradeFinishTime = dt.datetime.today() + self.upgradeTime
      self.upgradeMetalCost = 100 * self.level
      self.upgradeMetalCost = 75 * self.level
      self.energyConsumption = 5 * self.level
      self.upgradeTime = 10 * self.level


class MetalMine:
   def __init__(self):
      Mine.__init__(self, 50, 1, "Metal")


class CrystalMine:
   def __init__(self, level=1):
      Mine.__init__(self, 35, 1, "Crystal")


class Ship:
  def __init__(self, name, hitpoints, armor, damage, type):
   self.name = name
   self.hitpoints = hitpoints
   self.armor = armor
   self.damage = damage
   self.type = type


class Player:
   def __init__(self, name):
      self.name = name
      self.metalMine = MetalMine()
      self.crystalMine = CrystalMine()
      self.metal = 1000
      self.crystal = 1000
      self.energy = 50
      self.lastTick = dt.datetime.now()


if __name__ == "__main__":
    main()
