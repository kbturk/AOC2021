import sys, argparse
from copy import deepcopy
from pprint import pprint
from typing import Dict, List, Set, Tuple

def arg_parser():
    parser = argparse.ArgumentParser(description = 'provide input file')
    parser.add_argument('replacement_file', help = 'please provide text input file', type = argparse.FileType('r'))
    return parser

def main(args: List[str]) -> int:
    inputs = arg_parser().parse_args(args[1:])
    instructions = [int(line.rstrip('\n')) for line in inputs.replacement_file]
    last = instructions[0]
    count = 0
    for l in instructions:
        if last - l < 0:
            count += 1
        last = l
    count2 = 0
    for i in range(4,len(instructions)+1):
        #print(instructions[i-4:i-1], instructions[i-3:i])
        if sum(instructions[i-4:i-1]) - sum(instructions[i-3:i]) < 0:
            count2 += 1
    print(f'no of incrs: {count}, rolling window: {count2}')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))