"""
Write a python CLI application that takes all the files from a specified folder and organizes/moves them into subfolders
in another folder. Each subfolder name should be one character long and represents the first character in a given file
from the source folder.

"""

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

