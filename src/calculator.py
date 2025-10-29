def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number (positive only).
        y (int/float): Second number (positive only).
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number or non-positive.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if x <= 0 or y <= 0:
        raise ValueError("Both inputs must be positive.")
    
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number (positive only).
        y (int/float): Second number (positive only).
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number or non-positive.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if x <= 0 or y <= 0:
        raise ValueError("Both inputs must be positive.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number (positive only).
        y (int/float): Second number (positive only).
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number or a non-positive.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if x <= 0 or y <= 0:
        raise ValueError("Both inputs must be positive.")
    return x * y

def fun4(x,y,z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number (positive only).
        y (int/float): Second number (positive only).
        z (int/float): Third number (positive only).
    Returns:
        int/float: Sum of x, y and z.
    Raises:
        ValueError: If any input is not a number or non-positive.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise ValueError("All inputs must be numbers.")
    if x <= 0 or y <= 0 or z <= 0:
        raise ValueError("All inputs must be positive.")
    total_sum = x + y + z
    return total_sum

def fun5(x, y):
    """
    Divides two numbers.
    Args:
        x (int/float): Dividend (positive only).
        y (int/float): Divisor (positive only, non-zero).
    Returns:
        float: Quotient of x divided by y.
    Raises:
        ValueError: If x or y is not a number, non-positive, or y is zero.
    Example:
        >>> fun5(10, 2)
        5.0
        >>> fun5(5, 0)
        ValueError: Divisor cannot be zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if x <= 0 or y <= 0:
        raise ValueError("Both inputs must be positive.")
    if y == 0:
        raise ValueError("Divisor cannot be zero.")
    return x / y


# f1_op = fun1(2,3)
# f2_op = fun2(2,3)
# f3_op = fun3(2,3)
# f4_op = fun4(f1_op,f2_op,f3_op)

