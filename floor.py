import rectangle
import config
import elevator

class Floor:
    def __init__(self, Elevator, FloorNumber, FLOORHEIGHT):
        self.Rect                   = rectangle.Rectangle(100 + 100 * Elevator.getID(), FloorNumber * FLOORHEIGHT, 90, FLOORHEIGHT, True)
        self.FloorNumber            = config.FLOORNUMBER - FloorNumber - 1
        self.Elevator               = elevator.Elevator(self.FloorNumber)
    def getRect(self):              return self.Rect
    def getFloorNumber(self):       return self.FloorNumber
    def getElevatorNumber(self):    return self.ElevatorNumber