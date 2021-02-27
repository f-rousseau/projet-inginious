class Vehicle(object):
    currentId = 0

    def __init__(self, brand: str, hasMotor: bool, hasBody: bool, seats: int):
        self.id = Vehicle.currentId
        Vehicle.currentId += 1
        self.brand = brand
        self.hasMotor = hasMotor  # boolean
        self.hasBody = hasBody  # boolean
        self.seats = seats

    def __str__(self):
        return "Id : {}\nBrand : {}\nHas a motor : {}\nHas a body : {}\nSeats : {}".format(self.id, self.brand,
                                                                                           self.hasMotor, self.hasBody,
                                                                                           self.seats)


class Car(Vehicle):

    def __init__(self, brand, fuel, seats):
        super().__init__(brand, True, True, seats)
        if fuel in ["Gasoline", "Electric", "Hybrid", "Diesel"]:
            self.fuel = fuel
        else:
            raise Exception('Invalid fuel type. Must be "Gasoline", "Electric", "Hybrid", "Diesel"')

    def __str__(self):
        pre = super().__str__()
        return "{}\nFuel type : {}".format(pre, self.fuel)


class Bike(Vehicle):

    def __init__(self, brand):
        super().__init__(brand, False, False, 1)


class Lorry(Vehicle):

    def __init__(self, brand: str, weight_in_tons: float):
        super().__init__(brand, True, True, 2)
        self.weight = weight_in_tons

    def __str__(self):
        pre = super().__str__()
        return "{}\nWeight in tons : {}".format(pre, round(self.weight, 3))


class Garage(object):

    def __init__(self, size: int):
        self.vehicles = []
        self.size = size

    def __str__(self):
        s = ""
        for i, j in enumerate(self.vehicles):
            s += "Space {} = vehicle with id : {}\n".format(i, j.id)
        return s

    def addVehicle(self, vehicle: Vehicle):
        if len(self.vehicles) < self.size:
            self.vehicles.append(vehicle)
            print("Vehicle added")
            return True
        else:
            print("vehicle can't be added")
            return False

    def removeVehicle(self, vehicleId: int):
        for i, j in enumerate(self.vehicles):
            if j.id == vehicleId:
                self.vehicles.pop(i)
                print("Vehicle removed")
                return True
        print("vehicle can't be removed")
        return False


a = Vehicle("Peugeot", True, True, 3)
b = Car("VW", "Electric", 4)
c = Lorry("Man", 4.5)

garage = Garage(2)

garage.addVehicle(a)
garage.addVehicle(b)
garage.addVehicle(c)
garage.removeVehicle(1)
garage.addVehicle(c)

print(a, b, c, garage)
