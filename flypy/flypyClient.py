from .flypyImages import PlaneImage
from .exceptions import NotFound
from .utils import instantiate as universalConnection

class flypyClient:
  def __init__(self, connection = None):
    self.connection = connection

  async def findPlaneImageByReg(self, reg):
    if self.connection is None:
      self.connection = await universalConnection()
      planeImage = PlaneImage(self.connection, reg)
      
      updateAttempt = await planeImage.update()
      if updateAttempt == None:
        raise NotFound
        del planeImage
      else:
        return planeImage
