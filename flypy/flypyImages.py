class PlaneImage:
  def __init__(self, connection, reg, data = None):
    self.data = None
    self.reg = reg
    self.connection = connection
  
  async def update(self):
    data = await self.connection.request(f"https://api.planespotters.net/pub/photos/reg/{self.reg}")

    if "error" in data.keys():
      return "Error"
    else:
      self.data = data
  
  @property
  def image(self):
    return self.data["photos"][0]["thumbnail_large"]["src"]
  
  @property
  def photographer(self):
    return self.data["photos"][0]["photographer"]
  
  @property
  def link(self):
    return self.data["photos"][0]["link"]
