import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )

    def test_empty_list(self):
        self.assertListEqual([],unique([]))
    
    def test_many_items_list(self):
        self.assertListEqual(['hello','cat','dog'],unique(['hello','hello','cat','cat','cat','dog','dog']) )

    def test_extreamcase_list(self):
        self.assertListEqual([2,99],unique([2,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99]))

    
    
 
if __name__ == '__main__':
    unittest.main()