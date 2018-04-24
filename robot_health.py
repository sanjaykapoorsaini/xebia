import robot


#
#  @author: Sanjay Kumar
#  This is Robot Health Model Class.
#
class RobotHealth(object):
    def can_carry(self, weight):
        """Checks wither the robot is Overweight or not.

        Args:
            weight: Carried weight in KG.
        """
        if weight > 10:
            print("Overweight")
            print("************************************************")
            return False
        return True

    def power_check(self, robot_obj, required_charging):
        """Checks wither sufficient charging is present or not.

        Sets the headlight color to red if battery is less than 15%.
        Args:
            robot_obj: Robot class object.
            required_charging: Charging required.
        """
        available_charging = robot_obj.charging_status
        if available_charging < required_charging:
            print("Insufficient Charging For Task")
            print("************************************************")
            return False
        else:
            remaining = available_charging - required_charging
            robot_obj.charging_status = remaining
            if remaining < 15:
                robot_obj.head_light_color = robot.Color.RED
                print("*********************************************")
            return True
