import unittest

from lines_of_code.main import get_lines_of_code

class TestLinesOfCode(unittest.TestCase):

    def test_python_code(self):
        expected_result = {
            'total_lines': 8,
            'blank_lines': 3,
            'comment_lines': 1,
            'code_lines': 4
        }
        actual_result = get_lines_of_code('./tests/source_files/test.py')
        self.assertEqual(expected_result, actual_result)
    
    def test_java_code(self):
        expected_result = {
            'blank_lines': 3, 
            'code_lines': 6, 
            'comment_lines': 3, 
            'total_lines': 12
        }

        actual_result = get_lines_of_code('./tests/source_files/test.java')
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
