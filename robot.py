import enum


# Creating Color enumeration for head light color.
class Color(enum.Enum):
    GREEN = 'GREEN'
    RED = 'RED'


#
#  @author: Sanjay Kumar
#  This is Robot Model Class.
#
class Robot(object):

    def __init__(self):
        self._charging_status = 100
        self._head_light_color = Color.GREEN

    @property
    def charging_status(self):
        return self._charging_status

    @charging_status.setter
    def charging_status(self, value):
        self._charging_status = value

    @property
    def head_light_color(self):
        return self._head_light_color

    @head_light_color.setter
    def head_light_color(self, color):
        self._head_light_color = color
