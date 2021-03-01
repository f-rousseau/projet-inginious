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