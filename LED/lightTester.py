

class LightTester():  
    ''' class that creates the LED board grid with size L X L. Each point on the grid is initalised to false. '''

    def __init__(self,grid_size):
        self.lights = [[False]*grid_size for x in range(grid_size)]
        
        
    def edit_grid(self, command, start, end):
        ''' function that corrects coordinate ranges and forces changes on the grid
        
        this function corrects coordinate ranges by passing the coordinate arguments to coord_range which corrects ensures
        that the coordinates are in the required range. This function forces changes on the grid by passing the command, 
        x coordinate and y coordinate for each point on the rectangle to the apply function '''

        self.command = command
        self.start = start
        self.end = end

        start,end = self.coord_range (self.start,self.end)
    
        #finding the size of the rectangle with the row and column length 
        row_size = self.end[0] - self.start[0]
        column_size = self.end[1] - self.start[1]

        #Nested for loop to send each coordinate in the rectangle to the apply function.
        for x in range (self.start[0], self.start[0] + row_size +1, 1):
            for y in range(self.start[1], self.start[1] + column_size +1, 1):
                self.apply(self.command,x,y)

        return self.lights
    
    
    def coord_range(self, coord1,coord2):
        ''' function checks that the coordinates are within the range of the grid and if theyre not corrects them to the edge of the grid '''
        self.start = coord1
        self.end = coord2

        #making sure point is in range 
        if self.start[0] < 0:
            self.start[0] = 0
        elif self.start[0] > len(self.lights)-1:
            self.start[0] = len(self.lights)-1

        if self.start[1] < 0:
            self.start[1] = 0
        elif self.start[1] > len(self.lights)-1:
            self.start[1] = len(self.lights)-1

        if self.end[0] < 0:
            self.end[0] = 0
        elif self.end[0] > len(self.lights)-1:
            self.end[0] = len(self.lights)-1

        if self.end[1] < 0:
            self.end[1] = 0
        elif self.end[1] > len(self.lights)-1:
            self.end[1] = len(self.lights)-1

        self.start_point =[self.start[0], self.start[1]]
        self.end_point = [self.end[0], self.end[1]]

        return self.start_point,self.end_point
    
    
    
    
    def apply(self,command,x_coord,y_coord):
        ''' function that applys changes to the grid by examining the command and applying command to the point on the grid '''

        self.command = command
        self.x_coord = x_coord
        self.y_coord = y_coord


        if self.command == "turn on":
            self.lights[x_coord][y_coord] = True

        elif self.command == "turn off":
            self.lights[x_coord][y_coord] = False

        elif self.command == "switch":
            #need to check the current status of the lights now 
            if self.lights[x_coord][y_coord] == True:
                self.lights[x_coord][y_coord] = False
            else:
                self.lights[x_coord][y_coord] = True


        return self.lights


    def count(self):
        ''' function that counts how many lights are turned on on the grid.turned on lights have the value true'''

        count=0
        for idx1 in range (0, len(self.lights), 1 ):
            for idx2 in range (0, len(self.lights), 1):
                if self.lights[idx1][idx2] == True:
                    count +=1

        return count
