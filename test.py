TURRET_DATA_1 = [
  {
    #1
    "range": 90,
    "cooldown": 1500,
  },
  {
    #2
    "range": 110,
    "cooldown": 1200,
  },
  {
    #3
    "range": 125,
    "cooldown": 1000,
  },
  {
    #4
    "range": 150,
    "cooldown": 900,
  }
]

level = 1

if level != len(TURRET_DATA_1):
    level += 1
else:
    print("Udah max")