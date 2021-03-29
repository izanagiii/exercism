from random import sample
from string import ascii_uppercase as upper, digits

class Robot:
    name_db = []

    def __init__(self):
        self.name = self.rand_name()

    # generate a random name for robot
    def rand_name(self):
        while True:
            name_initial = []
            name_initial.extend(sample(upper, 2))
            name_initial.extend(sample(digits, 3))
            name_final = "".join([str(i) for i in name_initial])

            if name_final not in Robot.name_db:
                Robot.name_db.append(name_final)
                break
        return name_final

    def reset(self):
        Robot.name_db.remove(self.name)
        # del self.name
        self.name = self.rand_name()

    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self):
    #     self._name = sefl.rand_name()
    
    # @name.deleter
    # def name(self):
    #     Robot.name_db.remove(self._name)
    #     # del self._name
    #     # creates a new name as soon as you delete the name of robot
    #     self._name = self.rand_name()

    # def __del__(self):
    #     Robot.name_db.remove(self._name)
    #     del self

# robot1 = Robot()
# print(f"robot1 name: {robot1.name}")
# robot2 = Robot()
# robot3 = Robot()
# robot4 = Robot()

# # del robot1.name
# # robot1 = Robot()

# # del robot1
# # robot1 = Robot()

# robot1.reset()

# print(f"robot1 name: {robot1.name}")
# print(f"robot2 name: {robot2.name}")
# print(f"robot3 name: {robot3.name}")
# print(f"robot4 name: {robot4.name}")

# print(Robot.name_db)


robot = Robot()
name = robot.name

robot.reset()
name2 = robot.name

print(f"is {name} == {name2} ? {name == name2}")

print(Robot.name_db)
