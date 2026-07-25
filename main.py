def main():
    # Your core program logic goes here
    print("Hello from the main function!")

class Mine:
  def __init__(self, rate, level, name):
    self.level = level
    self.name = name
    self.rate = rate * self.level
    self.upgradeMetalCost = 100 * self.level
    self.updateCrystalCost = 75 * self.level
    self.upgradeTime = 10 * self.level


class MetalMine:
   def __init__(self, rate, level, name):
      super().__init__(self, 50, level, "Metal")


class MetalMine:
   def __init__(self, rate, level, name):
      super().__init__(self, 35, level, "Crystal")


class ship:
  def __init__(self, name, hitpoints, armor, damage, type):
   self.name = name
   self.hitpoints = hitpoints
   self.armor = armor
   self.damage = damage
   self.type = type



if __name__ == "__main__":
    main()
