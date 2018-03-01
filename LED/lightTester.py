

class LightTester():


    def __init__(self,grid_size):
        self.lights = [[False]*grid_size for x in range(grid_size)]
        
        
    def limits(self, command, start, end):

        self.command = command
        self.start = start
        self.end = end

        start,end = self.coord_range (self.start,self.end)
    
        return""
    
    
    def coord_range (self, coord1,coord2):

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

        self.start2=[self.start[0], self.start[1]]
        self.end2 = [self.end[0], self.end[1]]

        return self.start2,self.end2