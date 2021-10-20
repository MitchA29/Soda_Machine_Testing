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






if __name__ == '__main__':
    unittest.main()
