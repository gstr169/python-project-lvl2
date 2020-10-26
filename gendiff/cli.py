import argparse


def cli_call():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(args)
