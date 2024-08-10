import numpy as np
import math

def get_shift_values(x_range, y_range, random_number):
    np.random.seed(random_number)
    x_shift = np.random.uniform(x_range[0], x_range[1])
    y_shift = np.random.uniform(y_range[0], y_range[1])
    return x_shift, y_shift

def dynamic1(candidate, random_number):
    x, y = candidate[0], candidate[1]
    if -75 <= x <= -55 and -75 <= y <= -55:
        z = 0.1 * (((-65 - x) / 5) ** 2 + ((-65 - y) / 5) ** 2) + 0.6
        return z if z < 1 else 1
    else:
        x_shift, y_shift = get_shift_values([-15, 15], [-15, 15], random_number)
        x, y = candidate[0] + x_shift, candidate[1] + y_shift
        return (
            np.exp(-math.pow(x / 35, 6) - math.pow(y / 35, 6))
            + 2 * np.exp(-math.pow(x / 10, 2) - math.pow(y / 10, 2))
            * math.pow(np.cos(x / 10), 1)
            * math.pow(np.cos(y / 10), 1)
            + 1
        )
