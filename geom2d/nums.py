import math

def are_close_enough(a, b, tolerance=1e-10):
    """
    Determines if two numbers are close based on a given tolerance. Returns true if the
    absolute difference between the values is less than the tolerance.

        Parameters:
            a (float): First number
            b (float): Second number
            tolerance (float): Tolerance for evaluation, default value of 1e-10

        Returns:
            (bool): True if |a - b| < tolerance
    """

    return math.fabs(a - b) < tolerance

def is_close_to_zero(a, tolerance=1e-10):
    return are_close_enough(a, 0.0, tolerance)

def is_close_to_one(a, tolerance=1e-10):
    return are_close_enough(a, 1.0, tolerance)

