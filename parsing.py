import argparse


class CustomNamespace(argparse.Namespace):
    def __init__(self):
        super().__init__()
        self.n = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.s = 0
        self.e = 0


def argument_parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="Number of divisions for specified calculus", type=int, required=True)
    parser.add_argument("-a", help="Coefficient for x^2", type=float, required=True)
    parser.add_argument("-b", help="Coefficient for X", type=float, required=True)
    parser.add_argument("-c", help="Y intercept of the parabola", type=float, required=True)
    parser.add_argument("-s", help="Start of the calculation", type=float, required=True)
    parser.add_argument("-e", help="End of the calculation", type=float, required=True)
    args = parser.parse_args(namespace=CustomNamespace())
    return args
