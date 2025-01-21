import argparse
import sys
def calc(args):
    if args.o =='add':
        return args.x +args.y

    elif args.o =='mul':
        return args.x *args.y

    elif args.o =='sub':
        return args.x -args.y

    elif args.o =='div':
        return args.x /args.y
    else:
        return "Something wrong"

if __name__ == '__main__':
    parsar = argparse.ArgumentParser()
    parsar.add_argument('--x', type=float, default=1.0, help="Enter first number.This is a utility for calculation. please contact harry bhai")

    parsar.add_argument('--y', type=float, default=1.0, help="Enter second number.This is a utility for calculation. please contact harry bhai")

    parsar.add_argument('--x', type=float, default=1.0, help="Enter thied. number.This is a utility for calculation. please contact harry bhai")

    args = parsar.parse_args()
    sys.stdout.write(str(calc(args)))