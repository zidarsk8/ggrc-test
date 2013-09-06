'''
Created on Sep 5, 2013

@author: diana.tzinov
'''




import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers
from helperRecip.GRCObject import GRCObject


class TestProgramMapToRegulation(WebDriverTestCase):

    
    def testProgramMapToRegulation(self):
        self.testname="testProgramEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers()
        do.setUtils(util)
        do.login()

        do.expandLeftNavMenuForObject("Program")
        first_link_of_the_section_link = element.left_nav_first_object_link_in_the_section.replace("SECTION","Program" )
        do.navigateToObject("Program",first_link_of_the_section_link)
        do.expandLeftNavMenuForObject("Regulation")
        first_link_of_the_section_link = element.left_nav_first_object_link_in_the_section.replace("SECTION","Regulation" )
        util.hoverOverAndWaitFor(first_link_of_the_section_link,element.map_to_this_object_link)
        util.clickOn(element.map_to_this_object_link)
        #time.sleep(20)
        
        
if __name__ == "__main__":
    unittest.main()