class Game:
  def __init__(self, name, tags, achievement, status):
    self.name = name
    self.tags = tags
    self.achievement = achievement
    self.status = status

  def __str__(self):
    return f"{self.name}"