import unittest
from LED.parse import *
from LED.lightTester import *


class Test_LED(unittest.TestCase):

    #Setting up the grid
    def setUp(self):
        self.led = LightTester(3)
        

    #Testing the given coordinates the edit_grid function will switch the lights    
    def test_edit_grid_turnOn(self):

        self.test_variable = self.led.edit_grid("turn on", [1,0],[2,2])
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 6,"lights not successfully turned on")  
        
    
    #Testing the given coordinates the edit_grid function will turn off the lights
    def test_edit_grid_turnOff(self):

        self.test_variable = self.led.edit_grid("turn off", [0,0],[1,1])
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 0,"lights not successfully turned off")
        
    
    #Testing the given coordinates the edit_grid function will switch the lights
    def test_edit_grid_switch(self):

        self.test_variable = self.led.edit_grid("switch", [0,0],[2,2])
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 9,"lights not successfully switched")
        
         

    #Testing that the coordinates are corrected if they occur outside the range
    def test_range(self):
        self.assertEqual(self.led.coord_range([3,4],[4,5]), ([2,2],[2,2]), "Coordinates not corrected to limit")
        self.assertEqual(self.led.coord_range([-1,1],[-5,-5]), ([0,1],[0,0]),"Coordinates not corrected to limit")
        
     
     
    # testing that the apply function successfully turns on lights on the grid     
    def test_turn_on(self):

        self.test_variable = self.led.apply("turn on", 0,2)
        
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 1, "Lights not successfully turned on")


    # testing that the apply function successfully turns off lights on the grid 
    def test_turn_off(self):

        self.test_variable = self.led.apply("turn off", 0,2)
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 0, "Lights not successfully turned off")    
     
    # testing that the apply function successfully switches lights on the grid     
    def test_switch(self):

        self.test_variable = self.led.apply("switch", 0,2)
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 1,"Lights not successfully switched")    
        
        
if __name__ == '__main__':
    unittest.main()