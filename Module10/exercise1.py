class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor#By default, a new elevator starts at the lowest floor.
        
    def go_to_floor(self, target_floor):
        #How many floors does the elevator need to go up or down?
        times = target_floor - self.current_floor 
        #If the value is positive, the floor_up function is called.
        if times >= 0:
            for i in range(times):
                self.floor_up() #How methods within the same class call each other
        #If the value is negative, the floor_down function is called.
        else:
            for i in range(-times):
                self.floor_down()#no need to include the default `self` parameter when call another method
        
    def floor_up(self):
        self.current_floor += 1
        #As required, print the current floor for each floor ascended.
        print(f"The elevator is now {self.current_floor} floor.")
        
    def floor_down(self):
        self.current_floor -= 1
        print(f"The elevator is now {self.current_floor} floor.")  

# h = Elevator(1, 10)
# print("Basic elevator test:")
# h.go_to_floor(5)
# h.go_to_floor(1)