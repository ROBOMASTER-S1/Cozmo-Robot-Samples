import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
    for _ in range(8):
        robot.drive_straight(distance_mm(200), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90), speed=degrees(50)).wait_for_completed()
cozmo.run_program(cozmo_program)
# robot.turn_in_place(degrees(90), speed=degrees(50)).wait_for_completed()
