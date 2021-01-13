import argparse

from lines_of_code.main import get_lines_of_code


if __name__ == '__main__':        
    arg_parser = argparse.ArgumentParser(prog='lines_of_code', description='Count lines of code in a source file')

    arg_parser.add_argument('path',
                            metavar='path',
                            type=str,
                            help='path to the source file')

    args = arg_parser.parse_args()

    input_path = args.path

    result = get_lines_of_code(input_path)

    print(result)