from turret import Turret
from turret_data import TURRET_DATA_1, TURRET_DATA_2, TURRET_DATA_3

class Turret1(Turret):
  def __init__(self, sprite_sheets, tile_x, tile_y, shot_fx):
    self.level = 1
    self.cooldown = TURRET_DATA_1[0]['cooldown']
    self.range = TURRET_DATA_1[0]['range']
    super().__init__(sprite_sheets, tile_x, tile_y, shot_fx, self.cooldown, self.range)
  
  def upgrade(self):
    if self.level < len(TURRET_DATA_1):
      new_cooldown = TURRET_DATA_1[self.level]['cooldown']
      new_range = TURRET_DATA_1[self.level]['range']
      self.level += 1
      super().upgrade(new_cooldown, new_range)
    else:
      print ("Udah Mentok")

class Turret2(Turret):
  def __init__(self, sprite_sheets, tile_x, tile_y, shot_fx):
    self.level = 1
    self.cooldown = 50
    self.range = 70
    super().__init__(sprite_sheets, tile_x, tile_y, shot_fx, self.cooldown, self.range)

  def upgrade(self):
    if self.level < len(TURRET_DATA_3):
      new_cooldown = TURRET_DATA_2[self.level]['cooldown']
      new_range = TURRET_DATA_2[self.level]['range']
      self.level += 1
      super().upgrade(new_cooldown, new_range)
    else:
      print ("Udah Mentok")

class Turret3(Turret):
  def __init__(self, sprite_sheets, tile_x, tile_y, shot_fx):
    self.level = 1
    self.cooldown = 125
    self.range = 1000
    super().__init__(sprite_sheets, tile_x, tile_y, shot_fx, self.cooldown, self.range)

  def upgrade(self):
    if self.level < len(TURRET_DATA_3):
      new_cooldown = TURRET_DATA_3[self.level]['cooldown']
      new_range = TURRET_DATA_3[self.level]['range']
      self.level += 1
      super().upgrade(new_cooldown, new_range)
    else:
      print ("Udah Mentok")
