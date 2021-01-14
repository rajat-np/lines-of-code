import os
import sys

from lines_of_code.utils import scan_lines
from lines_of_code.rules import definitions


def get_lines_of_code(input_path):
    """
    Function to return total, comment, blank and code lines in a file present in input_path.
    """

    result = {}
    
    if not os.path.exists(input_path):
        sys.exit('The specified path does not exist.')

    if os.path.isdir(input_path):
        sys.exit('The specified path is not a file.')

    _filename, file_extension = os.path.splitext(input_path)

    if definitions.get(file_extension) is None:
        sys.exit(f'{file_extension} extension is not supported yet.')

    definition = definitions[file_extension]

    with open(input_path, 'r') as file:

        lines_list = file.readlines()
        total_lines = len(lines_list)
        
        blank_lines, comment_lines = scan_lines(lines_list, definition['defs'])

        code_lines = total_lines - (blank_lines + comment_lines)

        result = dict(
            total_lines=total_lines,
            blank_lines=blank_lines,
            comment_lines=comment_lines,
            code_lines=code_lines
        )

    return result    
