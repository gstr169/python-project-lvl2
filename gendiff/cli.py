import argparse
from gendiff.differentiator import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    return args


def cli_call():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file))
