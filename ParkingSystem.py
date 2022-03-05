class ParkingSystem:
    def __init__(self, big, medium, small):
        self.sp = [0, big, medium, small]

    def addVehicle(self, carType):
        if(self.sp[carType]>0):
            self.sp[carType] -= 1
            return("Parking Allocated")
        else:
            return("Parking full for this type")
    
ps = ParkingSystem(2, 0, 1)
print(ps.addVehicle(3))