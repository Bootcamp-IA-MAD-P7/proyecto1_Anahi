class Taxi:
    def __init__(self):
        self.fare = 0.00
        self.journey_active = False
        self.moving = False
        self.rate_moving = 0.05
        self.rate_stopped = 0.02
    
    def start_journey(self):
        self.fare = 0.00
        self.journey_active = True
        self.moving = True

    def end_journey(self):
        self.journey_active = False
        return self.fare

    def set_moving(self):
        self.moving = True

    def set_stopped(self):
        self.moving = False

    def taximeter(self):
        if self.moving:
            self.fare += self.rate_moving
        else:
            self.fare += self.rate_stopped
    
    def set_rates(self, rate_moving, rate_stopped):
        if rate_moving <= 0 or rate_stopped <= 0:
            raise ValueError("Las tarifas deben ser números positivos")
        self.rate_moving = rate_moving
        self.rate_stopped = rate_stopped