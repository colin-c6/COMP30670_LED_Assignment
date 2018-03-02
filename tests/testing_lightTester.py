import unittest
from LED.parse import *
from LED.lightTester import *


class Test_LED(unittest.TestCase):

    ''' Class contained functions to check the functionality of the lightTesting.py script
    
    When initalized , a grid is created by creating an instance of the LightTester class'''
    
    def setUp(self):
        self.led = LightTester(3)
        

     
    def test_edit_grid_turnOn(self):
        ''' Function that tests that given coordinates, the edit_grid function will turn on the lights '''
        
        self.test_variable = self.led.edit_grid("turn on", [1,0],[2,2])
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 6,"lights not successfully turned on")  
        
    
 
    def test_edit_grid_turnOff(self):
        ''' Function that tests that given coordinates, the edit_grid function will turn off the lights '''

        self.test_variable = self.led.edit_grid("turn off", [0,0],[1,1])
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 0,"lights not successfully turned off")
        
    

    def test_edit_grid_switch(self):
        ''' Function that tests that given coordinates, the edit_grid function will switch the lights '''

        self.test_variable = self.led.edit_grid("switch", [0,0],[2,2])
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 9,"lights not successfully switched")
        
         

    
    def test_range(self):
        '''Function that tests that the coordinates are corrected if they occur outside the range '''
                
        self.assertEqual(self.led.coord_range([3,4],[4,5]), ([2,2],[2,2]), "Coordinates not corrected to limit")
        self.assertEqual(self.led.coord_range([-1,1],[-5,-5]), ([0,1],[0,0]),"Coordinates not corrected to limit")
        
     
     
         
    def test_turn_on(self):
        '''Function tests that the apply function successfully turns on lights on the grid'''

        self.test_variable = self.led.apply("turn on", 0,2)
        
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 1, "Lights not successfully turned on")



    def test_turn_off(self):
        '''Function tests that the apply function successfully turns off lights on the grid'''
        self.test_variable = self.led.apply("turn off", 0,2)
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 0, "Lights not successfully turned off")    
     
  
    def test_switch(self):
        '''Function tests that the apply function successfully switches lights on the grid'''
        self.test_variable = self.led.apply("switch", 0,2)
        self.count = 0
        for ind1 in range (0, len(self.test_variable), 1 ):
            for ind2 in range (0, len(self.test_variable), 1):
                if self.test_variable[ind1][ind2] == True:
                    self.count +=1
        self.assertEqual(self.count, 1,"Lights not successfully switched")    
        
        
if __name__ == '__main__':
    unittest.main()