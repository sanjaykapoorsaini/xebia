import enum
import random

# creating enumerations using class
class Color(enum.Enum):
    GREEN = 1
    RED = 2
# /*
#  * @author: Sanjay Kumar
#  * This is Robot Model Class.
#  */
class Robot(object):

  def __init__(self):
    self._chargingStatus = 100
    self._headLightColor = Color.GREEN.name

  @property
  def chargingStatus(self):
    return self._chargingStatus

  @chargingStatus.setter
  def chargingStatus(self, value):
    self._chargingStatus = value

  @property
  def headLightColor(self):
    return self._headLightColor

  @headLightColor.setter
  def setHeadLightColor(self, color):
    self._headLightColor = color
# ______________________________________________________________________________


class RobotHealth(object):

  def canCarry(self, weight):
    if weight > 10:
      print("Overweight")
      print("************************************************")
      return False
    return True

  def powerCheck(self, r, requiredCharging):
    availbleCharging = r.chargingStatus
    if(availbleCharging < requiredCharging):
      print("Insufficient Charging For Task")
      print("************************************************")
      return False
    else:
      remaining = availbleCharging - requiredCharging
      r.chargingStatus = remaining
      if(remaining < 15):
        r.headLightColor = Color.RED.name
        print("*********************************************")
      return True

#____________________________________________________________________________

class PrototypeRobot(object):

  def __init__(self):
    self.r = Robot()
    self.rh = RobotHealth()

  def setCharging(self, percentage):
      currentCharging = self.r.chargingStatus
      if(currentCharging + percentage > 100):
        self.r.chargingStatus = 100
      else:
        self.r.chargingStatus = currentCharging+percentage


  def walk(self, km):
       requiredCharging = int(km*1000/50)
       if self.rh.powerCheck(self.r, requiredCharging):
         print("Walked "+str(km)+"km | Charging Used "+ str(requiredCharging) +"% | Remaining  "+ str(self.r.chargingStatus) +"%")
         print("Robot HeadLight Color "+ self.r.headLightColor)
         print("************************************************")
         return True
       return False

  def carry(self, weight):
      if self.rh.canCarry(weight):
        requiredCharging = 2*weight
        if self.rh.powerCheck(self.r, requiredCharging):
          print("Carried "+ str(weight)+"kg | Charging Used "+ str(requiredCharging) +"% | Remaining  "+ str(self.r.chargingStatus) +"%")
          print("Robot HeadLight Color "+ str(self.r.headLightColor))
          print("************************************************")
          return True
      return False

  def walkAndCarry(self, dist, weight):
    if self.rh.canCarry(weight):
      requiredCharging = (int(dist*1000/50)) + 2*weight
      if self.rh.powerCheck(self.r, requiredCharging):
        print("Walked "+ str(dist) + "km and Carried "+ str(weight)+"kg | Charging Used "+ str(requiredCharging) +"% | Remaining  "+ str(self.r.chargingStatus) +"%")
        print("Robot HeadLight Color "+ self.r.headLightColor)
        print("************************************************")
        return True
    return False

  def displayPrice(self, barCode):
    if(barCode % 2 == 0):
      print("Price is "+ str(random.randint(1, 1000)))
    else:
      print("Scan Failure")

if __name__ == "__main__":
    obj = PrototypeRobot()
    obj.walk(3.5)
    obj.carry(6)
    obj.walkAndCarry(1,13)
    obj.setCharging(100)
    obj.walkAndCarry(2,3)
    obj.displayPrice(18)
