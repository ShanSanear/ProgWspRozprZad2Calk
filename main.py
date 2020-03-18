import logging
import time

import parsing


def calculate_quadratic_formula(a, b, c, x):
    return a * x ** 2 + b * x + c


def rectangular_method(n, a, b, c, starting_point, ending_point):
    calculated_integral = 0.0
    dx = (ending_point - starting_point) / n
    partial_value = 0
    start_time = time.time()
    for i in range(1, n):
        partial_value = calculate_quadratic_formula(a=a, b=b, c=c, x=starting_point + (i * dx))
        calculated_integral += partial_value * dx
    end_time = time.time()
    logging.info("It took %f seconds", end_time - start_time)
    logging.info("Calculated integral for rectangular method: %f", calculated_integral)


def trapezoidal_rule(n, a, b, c, starting_point, ending_point):
    calculated_integral = 0.0
    dx = (ending_point - starting_point) / n
    partial_value = 0
    start_time = time.time()
    for i in range(1, n - 1):
        calculated_integral += calculate_quadratic_formula(a=a, b=b, c=c, x=starting_point + (i * dx))
    calculated_integral += (calculate_quadratic_formula(a=a, b=b, c=c, x=starting_point) +
                            calculate_quadratic_formula(a=a, b=b, c=c, x=ending_point)) / 2
    calculated_integral *= dx
    end_time = time.time()
    logging.info("It took %f seconds", end_time - start_time)
    logging.info("Calculated integral for trapezoidal rule: %f", calculated_integral)


def main():
    logging.basicConfig(format="[%(levelname)1.1s] %(asctime)s %(module)s:%(lineno)d %(message)s",
                        datefmt="%H:%M:%S", level=logging.DEBUG)
    args = parsing.argument_parsing()
    logging.debug("Arguments: %s", args)
    rectangular_method(n=args.n, a=args.a, b=args.b, c=args.c, starting_point=args.s, ending_point=args.e)
    trapezoidal_rule(n=args.n, a=args.a, b=args.b, c=args.c, starting_point=args.s, ending_point=args.e)


if __name__ == '__main__':
    main()
