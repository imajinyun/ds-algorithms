import unittest

import simulation as sim


class TestSimulation(unittest.TestCase):
    """ 测试 simulation.py """

    def testSimulation(self):
        for i in range(10):
            sim.simulation(3600, 5)

    def testIsNewTask(self):
        self.assertFalse(sim.is_new_task())


if __name__ == '__main__':
    unittest.main()
