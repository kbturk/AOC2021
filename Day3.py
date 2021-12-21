import sys, argparse
from typing import List, Tuple
from copy import deepcopy

def arg_parser():
    parser = argparse.ArgumentParser(description="input_file")
    parser.add_argument('input_file', help = 'please provide input file name.', type = str)
    return parser

#returns (most common, least common) digit
def most_least(subList: List[str], i: int) -> Tuple[str,str]:
    tot = [0,0]
    for item in subList:
        if item[i] == '0':
            tot[0] += 1
        else:
            tot[1] += 1
    if tot[0] == tot[1]:
        return ('1','0')
    elif tot[0] > tot[1]:
        return ('0','1')
    else:
        return ('1','0')

#d should be 0 (most common) or 1 (least common)
def make_a_list(raw:List[str], d:int=0) -> List[str]:
    subList = deepcopy(raw)
    sListTemp=[]

    for i in range(len(subList[0])):
        digit = most_least(subList,i)
        for item in subList:
            if digit[d] == item[i]:
                sListTemp.append(item)
        if len(sListTemp) == 1:
            return sListTemp
        subList = deepcopy(sListTemp)
        sListTemp = []
    raise NameError(f"no single solution found: {subList}")
    return subList

def part1(raw: List[str]) -> int:
    gamma = ""
    epsilon = ""
    for i in range(len(raw[0])):
        dgamma, depsilon = most_least(raw,i)
        gamma += dgamma
        epsilon += depsilon
    print(f'gamma: {gamma}, epsilon: {epsilon}')
    return int(gamma,2)*int(epsilon,2)

def part2(raw: List[str]) -> int:
    o2rating = make_a_list(raw,0)[0]
    co2rating = make_a_list(raw,1)[0]
    print(f'o2rating: {o2rating}, co2rating: {co2rating}')
    return int(o2rating,2)*int(co2rating,2)

def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    with open(arg.input_file, 'r') as f:
        raw = [line.rstrip('\n') for line in f]
    print(f'{part1(raw)}')
    print(f'{part2(raw)}')
    return 0

if __name__ =="__main__":
    sys.exit(main(sys.argv))