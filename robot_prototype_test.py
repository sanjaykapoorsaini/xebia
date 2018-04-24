import unittest
import robot_prototype


class TestPrototypeRobot(unittest.TestCase):

    def setUp(self):
        self.obj = robot_prototype.PrototypeRobot()

    def test_walk(self):
        self.obj.walk(5)
        self.assertEquals(self.obj.robo.charging_status, 0)
        self.assertEquals(self.obj.robo.head_light_color, 'RED')

    def test_carry(self):
        self.obj.carry(10)
        self.assertEquals(self.obj.robo.charging_status, 80)
        self.assertEquals(self.obj.robo.head_light_color, 'GREEN')

    def test_walk_and_carry(self):
        # 100% used in 5km so 20% for 1km and extra 2 for carry weight.
        self.obj.walk_and_carry(4, 1)
        self.assertEquals(self.obj.robo.charging_status, 18)
        self.assertEquals(self.obj.robo.head_light_color, 'GREEN')


if __name__ == '__main__':
    unittest.main()
