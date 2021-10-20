import unittest
import user_interface

class TestValidateMainMenu(unittest.TestCase):
    """ Tests validate_main_menu method inside of the user_interface"""

    def test_validate_main_menu_selection1(self):
        """Test that main menu selection 1 is valid"""
        main_menu_selection = user_interface.validate_main_menu(1)
        self.assertEqual(main_menu_selection,(True,1))

    def test_validate_main_menu_selection2(self):
        """Test that main menu selection 2 is valid"""
        main_menu_selection = user_interface.validate_main_menu(2)
        self.assertEqual(main_menu_selection,(True,2))
    
    def test_validate_main_menu_selection3(self):
        """Test that main menu selection 3 is valid"""
        main_menu_selection = user_interface.validate_main_menu(3)
        self.assertEqual(main_menu_selection,(True,3))
    
    def test_validate_main_menu_selection4(self):
        """Test that main menu selection 4 is valid"""
        main_menu_selection = user_interface.validate_main_menu(4)
        self.assertEqual(main_menu_selection,(True,4))
    
    def test_validate_main_menu_selection_other_than_provided(self):
        """Test that main menu selection other than provided returns False,None"""
        main_menu_selection = user_interface.validate_main_menu(5)
        self.assertEqual(main_menu_selection,(False,None))

class TestTryParseInt(unittest.TestCase):
    """Tests the try_parse_int method inside of the user_interface"""

    def test_try_parse_int_is_int(self):
        """Tests to ensure the method will return correctly with int 10 passing in"""
        try_parse_value = user_interface.try_parse_int(10)
        self.assertEqual(try_parse_value,10)

    def test_try_parse_int_isnot_int(self):
        """Test to ensure method will not return value if not an int"""
        try_parse_value = user_interface.try_parse_int("hello")
        self.assertEqual(try_parse_value,0)

import cans



class TestGetUniqueCanNames(unittest.TestCase):
    """Test the get_unique_can_names_method of the user_interface"""
    
    """Inventory variable for test_creat_inventory test method"""

    inventory = []
    for index in range(2):
        inventory.append(cans.Cola())
    for index in range(2):
        inventory.append(cans.OrangeSoda())
    for index in range(2):
        inventory.append(cans.RootBeer())
    print(inventory)
    
    empty_inventory = []
    
    def test_get_unique_can_names_quantity(self):
        """test to make sure regardless of how many cans added, names is still only 3"""
        test_inventory = user_interface.get_unique_can_names(self.inventory)
        print(len(test_inventory))
    
    def test_get_unique_can_names_empty(self):
        """ test to make sure if nothing is passed in then nothing value is returned"""
        test_inventory = user_interface.get_unique_can_names(self.empty_inventory)
        print(len(test_inventory))






if __name__ == '__main__':
    unittest.main()
