class Game:
  def __init__(self, name, achievement, status, tags=["None"]):
    self.name = name
    self.tags = tags
    self.achievement = achievement
    self.status = status

  def __repr__(self):
    return f"[ {self.name}, {self.tags}, {self.achievement}, {self.status} ]"

  def __str__(self):
    return f"[ {self.name}, {self.tags}, {self.achievement}, {self.status} ]"