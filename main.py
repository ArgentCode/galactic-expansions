def main():
    # Your core program logic goes here
    print("Welcome to Galactic Expansions")
    print("Name your empire: ")
    name = input("Name your empire: ")
    newPlayer = Player(name)
    while True:
       status(newPlayer)
       choice = input("What would you like to do? m to upgrade metal mine, c to upgrade crystal mine, x to exit ")
       if choice == "x":
          print("Thanks for playing!")
          exit()
       elif choice == "m":
          print("Metal Mine upgraded!")
       elif choice == "c":
          print("Crystal Mine upgraded!")
       elif choice == "m":
          print("I didn't quite get that. Try again,")


def status(Player):
   print("Metal:", Player.metal, " Crystal:", Player.crystal, " Energy:", Player.energy)
   print("Metal Mine:", Player.metalmine.level, "Crystal Mine:", Player.crystalmine.level)


class Mine:
  def __init__(self, rate, level, name):
    self.level = level
    self.name = name
    self.rate = rate * self.level
    self.energyConsumption = 5 * self.level
    self.upgradeMetalCost = 100 * self.level
    self.updateCrystalCost = 75 * self.level
    self.upgradeTime = 10 * self.level


class MetalMine:
   def __init__(self, level=1):
      Mine.__init__(self, 50, level, "Metal")


class CrystalMine:
   def __init__(self, level=1):
      Mine.__init__(self, 35, level, "Crystal")


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
      self.metalmine = MetalMine(1)
      self.crystalmine = CrystalMine(1)
      self.metal = 1000
      self.crystal = 1000
      self.energy = 50


if __name__ == "__main__":
    main()
