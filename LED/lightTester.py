

class LightTester():


    def __init__(self,grid_size):
        self.lights = [[False]*grid_size for x in range(grid_size)]
        
        
    def edit_grid(self, command, start, end):

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
        #print (x_coord,y_coord)

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

        count=0
        for idx1 in range (0, len(self.lights), 1 ):
            for idx2 in range (0, len(self.lights), 1):
                if self.lights[idx1][idx2] == True:
                    count +=1

        return count
