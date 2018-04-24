import random
import robot
import robot_health


#
#   @author: Sanjay Kumar
#   This is Robot Prototype Class.
#
class PrototypeRobot(object):
    """Main Prototype Robot Class."""

    def __init__(self):
        """Initializes the robot and robot_health classes."""
        self.robo = robot.Robot()
        self.rh = robot_health.RobotHealth()

    def set_charging(self, percentage):
        """Sets the charging status.

        Args:
            percentage: charging value in percentage.
        """
        current_charging = self.robo.charging_status
        if current_charging + percentage > 100:
            self.robo.charging_status = 100
        else:
            self.robo.charging_status = current_charging + percentage

    def walk(self, km):
        """Prints stats for walk."""
        required_charging = int(km * 20)  # int(km * 1000 / 50)
        if self.rh.power_check(self.robo, required_charging):
            self.print_output(required_charging, dist=km)

    def carry(self, weight):
        """Prints stats for carry weight."""
        if self.rh.can_carry(weight):
            required_charging = 2 * weight
            if self.rh.power_check(self.robo, required_charging):
                self.print_output(required_charging, wgt=weight)

    def walk_and_carry(self, dist, weight):
        """Prints stats for walk while carrying weight."""
        if self.rh.can_carry(weight):
            required_charging = int(dist * 20) + 2 * weight
            if self.rh.power_check(self.robo, required_charging):
                self.print_output(required_charging, wgt=weight, dist=dist)

    def print_output(self, req_charge, dist=None, wgt=None):
        """Prints stats on the basis of different arguments.

        Args:
            req_charge: Required charging in percentage.
            dist: Distance walked by robot.
            wgt: Weight carried by robot.
        """
        out = ""
        if dist:
            out += "Walked " + str(dist) + "km | "
        if wgt:
            out += "Carried " + str(wgt) + "kg | "
        out += "Charging Used " + str(req_charge) + "% | Remaining " + str(self.robo.charging_status) + "%"
        print(out)
        print("Robot HeadLight Color " + self.robo.head_light_color)
        print("************************************************")

    def display_price(self, bar_code):
        """Prints the bar code scan price randomly.

        Args:
            bar_code: Bar code value.
        """
        if bar_code % 2 == 0:
            print("Price is " + str(random.randint(1, 1000)))
        else:
            print("Scan Failure")


if __name__ == "__main__":
    obj = PrototypeRobot()
    obj.walk(3.5)
    obj.set_charging(100)
    obj.walk_and_carry(2, 3)
    obj.carry(12)
    # obj.walk_and_carry(2, 3)
    obj.display_price(18)
