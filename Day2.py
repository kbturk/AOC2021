import sys, argparse
from copy import deepcopy

from typing import Dict, List, Set, Tuple

def arg_parser():
    parser = argparse.ArgumentParser(description = 'enter input file')
    parser.add_argument('ifile', help = 'please provide text input file', type = argparse.FileType('r'))
    return parser

def parser(input) -> int:
    coords = [0,0]
    for line in input:
        a, b = line.split()
        if a == 'forward':
            coords[0] += int(b)
        elif a == 'down':
            coords[1] += int(b)
        elif a == 'up':
            coords[1] -= int(b)
    return coords[0]*coords[1]

def parser2(input) -> int:
    aim = 0
    coords = [0,0]
    for line in input:
        a, b = line.split()
        if a == 'forward':
            coords[0] += int(b)
            coords[1] += aim * int(b)
        elif a == 'down':
            aim += int(b)
        elif a == 'up':
            aim -= int(b)
    return coords[0]*coords[1]

def main(args: List[str]) -> int:
    inputs = arg_parser().parse_args(args[1:])
    input = [line.rstrip('\n') for line in inputs.ifile]
    print(f'part1 {parser(input)}')
    print(f'part2 {parser2(input)}')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))