RATE_MOVING = 0.05
RATE_STOPPED = 0.02

class Taxi:
    def __init__(self):
        self.fare = 0.00
        self.journey_active = False
        self.moving = False
    
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
            self.fare += RATE_MOVING
        else:
            self.fare += RATE_STOPPED