class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        
    def go_to_floor(self, target_floor):
        times = target_floor - self.current_floor
        if times >= 0:
            for i in range(times):
                self.floor_up() 
        else:
            for i in range(-times):
                self.floor_down()
        
    def floor_up(self):
        self.current_floor += 1
        print(f"The elevator is now {self.current_floor} floor.")
        
    def floor_down(self):
        self.current_floor -= 1
        print(f"The elevator is now {self.current_floor} floor.")  

class Building:
    def __init__(self, bottom_floor, top_floor, elevators_number):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(elevators_number):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator, destination_floor):
        elevator = self.elevators[elevator]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        #Check if each elevator is currently on the bottom floor
        for elevator in self.elevators:
            while elevator.current_floor != elevator.bottom_floor:
                #if not in the bottom floor, call floor_down method of elevator
                elevator.floor_down()

# building = Building(1, 10, 3)
# building.run_elevator(0, 5)
# building.run_elevator(1, 8)
# # building.run_elevator(2, 3)
# building.fire_alarm()