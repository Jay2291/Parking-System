class ParkingSystem:
    def __init__(self, big, medium, small):
        self.sp = [0, big, medium, small]

    def addVehicle(self, carType):
        if(self.sp[carType]>0):
            self.sp[carType] -= 1
            print("Parking Allocated")
        else:
            print("Parking full for this type")
    
ps = ParkingSystem(2, 0, 1)

print("""The type of vechicle to park:
            (1) Big sized Vehicle
            (2) Medium sized Vehicle
            (3) Small sized Vehicle""")
alot = int(input("Enter your option here: "))
if alot == 1:
    ps.addVehicle(1)
 
elif alot == 2:
    ps.addVehicle(2)
 
elif alot == 3:
    ps.addVehicle(3)
 
else:
    print("Incorrect option")

