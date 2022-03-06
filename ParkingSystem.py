import sys

class ParkingSystem:
    def __init__(self, big, medium, small):
        self.sp = [0, big, medium, small]

    def addVehicle(self, carType):
        if(self.sp[carType]>0):
            self.sp[carType] -= 1
            print("Parking Allocated")
        else:
            print("Parking full for this type")

    def remVehicle(self, carType):
            self.sp[carType] += 1
            print("Parking Allocated has been made free")
    
ps = ParkingSystem(2, 0, 1)
while True:
    print("""The types of vehicle to Park:\n
                (1) Park Big sized Vehicle
                (2) Park Medium sized Vehicle
                (3) Park Small sized Vehicle\n
            Or to free Allocated Vehicle:\n
                (4) Remove Big sized Vehicle
                (5) Remove Medium sized Vehicle
                (6) Remove Small sized Vehicle \n
                (7) Exit""")
    alot = int(input("Enter your option here: "))
    if alot == 1:
        ps.addVehicle(1)
    
    elif alot == 2:
        ps.addVehicle(2)
    
    elif alot == 3:
        ps.addVehicle(3)
    
    elif alot == 4:
        ps.remVehicle(1) 
    
    elif alot == 5:
        ps.remVehicle(2)
    
    elif alot == 6:
        ps.remVehicle(3)

    elif alot == 7:
        print("Thank You for using our services")
        sys.exit()

    else:
        print("Incorrect option")

