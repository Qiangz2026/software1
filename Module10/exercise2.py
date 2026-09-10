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
        #Store the required number of elevator instances in the elevator list.
        self.elevators = []
        for i in range(elevators_number):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        #Locate the specific elevator using the index.
        elevator = self.elevators[elevator_number]
        #call go_to_floor method and go to the destination_floor
        elevator.go_to_floor(destination_floor)

# building = Building(1, 10, 3)
# building.run_elevator(0, 5)
# building.run_elevator(1, 3)
# building.run_elevator(2, 8)
# small_building = Building(0, 5, 1)
# small_building.run_elevator(0, 4)
# office = Building(1, 6, 5)
# office.run_elevator(0, 4)
# office.run_elevator(4, 2)