class MarsRover():
    #Initialise the MarsRover class attributes. (X,Y) and Z is direction facing
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    #Rotate right dict(clock-wise rotation)        
    def rotate_right(self):
        ROTATE_RIGHT = {
            'N':'E',
            'E':'S',
            'S':'W',
            'W':'N'
        }       
        self.Z = ROTATE_RIGHT[self.Z]
            
    #Rotate left dict(anti clock-wise rotation)        
    def rotate_left(self):        
        ROTATE_LEFT = {
            'N':'W',
            'W':'S',
            'S':'E',
            'E':'N'
        }
        self.Z = ROTATE_LEFT[self.Z]

    #Assumption that the starting box on the plateu grid is (1,1)
    #First check if the next move will take the rover out of the plane/plateu, if it does return False
    #If not, then move( +/- in X/Z ) it according to it's Z and return True                 
    def check_and_move(self,plateau_width,plateau_height):              
        if self.Z == 'N':
            if self.Y+1 >=1 and self.Y+1 <=plateau_height:
                self.Y += 1
                return True
            else:
                return False
        elif self.Z == 'E':
            if self.X+1 >=1 and self.X+1 <=plateau_width:
                self.X += 1
                return True
            else:
                return False    
        elif self.Z == 'S':
            if self.Y-1 >=1 and self.Y-1 <=plateau_height:
                self.Y -= 1
                return True
            return False        
        elif self.Z == 'W':
            if self.X-1 >=1 and self.X-1 <=plateau_width:
                self.X -= 1
                return True
            else:
                return False
                              
    def __str__(self):
        return str(self.X) + " " + str(self.Y) + " " + self.Z

    #A get_rover_position class method to read and set the rover's current position
    @classmethod
    def get_rover_position(self):
        position = input("Enter Rover position:-- ").strip().split(" ")
        X = int(position[0])
        Y = int(position[1])
        Z = position[2]
        return self(X, Y, Z)

def main():
    #User input for plateu dimensons(e.g. 5 5), Assumption that the starting box on the plateu grid is (1,1)
    plateau_dimensions = input("Enter Plateau dimensions:-- ").strip().split(" ")
    plateau_width = int(plateau_dimensions[0])
    plateau_height = int(plateau_dimensions[1])  
    while True:
        rover = MarsRover.get_rover_position()         
        command = input("Enter commands for rover movement:-- ").strip()
        #iterate through each of the commands
        for command_word in command:
            if command_word == 'L':
                rover.rotate_left()
            elif command_word == 'R':
                rover.rotate_right()
            #calling the check_and_move method, break it if at any time it results False
            elif command_word == 'M':
                if not rover.check_and_move(plateau_width,plateau_height):
                    result = str(rover)
                    print("Invalid rover command passed, will go off plateu. Please check and rescue the rover :) The rover has stopped at:-- ")
                    break   
        result = str(rover)
        print(result)

if __name__ == '__main__':
    main()