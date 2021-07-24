import json
import os


class speedtest:
  __pout__ = None
  __brief__ = None
  __descr__ = None
  __perc__ = None
  __title__ = None
  __intro__ = None

  def __init__(self):
    process = os.popen( "speedtest -f json" )
    self.__pout__ = json.load( process )
    self.__setBrief__()
    self.__setTitle__()
    self.__setIntro__()

  def __setTitle__(self):
      self.__title__ = "HomeHub"

  def __setIntro__(self):
      self.__intro__ = "We have performed"

  def __setBrief__(self):
    self.__brief__ = " a speed test"


  def getDownload(self):
    down = self.__pout__['download']['bandwidth']
    down = (down/(1000*1000))*8
    return round(down,2)

  def getUpload(self):
    up = self.__pout__['upload']['bandwidth']
    up = (up/(1000*1000))*8
    return round(up, 2)

  def getServer(self):
    return [self.__pout__['server']['name'], self.__pout__['server']['location'], self.__pout__['server']['country']]

  def getBrief(self):
    return str(self.__brief__)

  def getTitle(self):
      return str(self.__title__)

  def getIntro(self):
      return str(self.__intro__)