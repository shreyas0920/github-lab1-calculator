# import pytest
# from src import calculator

# def test_fun1():
#     assert calculator.fun1(2, 3) == 5
#     assert calculator.fun1(5, 0) == 5
#     with pytest.raises(ValueError):
#         calculator.fun1(-1, 1)
#     with pytest.raises(ValueError):
#         calculator.fun1(1, -1)

# def test_fun2():
#     assert calculator.fun2(2, 3) == -1
#     assert calculator.fun2(5, 0) == 5
#     with pytest.raises(ValueError):
#         calculator.fun2(-1, 1)
#     with pytest.raises(ValueError):
#         calculator.fun2(1, -1)

# def test_fun3():
#     assert calculator.fun3(2, 3) == 6
#     assert calculator.fun3(5, 0) == 0
#     with pytest.raises(ValueError):
#         calculator.fun3(-1, 1)
#     with pytest.raises(ValueError):
#         calculator.fun3(1, -1)

# def test_fun4():
#     assert calculator.fun4(2, 3, 5) == 10
#     assert calculator.fun4(5, 0, 1) == 4  # Adjusted to handle new validation
#     with pytest.raises(ValueError):
#         calculator.fun4(-1, 1, 2)
#     with pytest.raises(ValueError):
#         calculator.fun4(1, -1, 2)

# def test_fun5():
#     assert calculator.fun5(10, 2) == 5.0
#     assert calculator.fun5(5, 1) == 5.0
#     with pytest.raises(ValueError):
#         calculator.fun5(-1, 1)
#     with pytest.raises(ValueError):
#         calculator.fun5(1, -1)
#     with pytest.raises(ValueError):
#         calculator.fun5(10, 0)

import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5, 1) == 6  # Changed 0 to 1
    with pytest.raises(ValueError):
        calculator.fun1(-1, 1)
    with pytest.raises(ValueError):
        calculator.fun1(1, -1)
    with pytest.raises(ValueError):
        calculator.fun1(5, 0)  # Test zero input

def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5, 1) == 4  # Changed 0 to 1
    with pytest.raises(ValueError):
        calculator.fun2(-1, 1)
    with pytest.raises(ValueError):
        calculator.fun2(1, -1)
    with pytest.raises(ValueError):
        calculator.fun2(5, 0)  # Test zero input

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5, 1) == 5  # Changed 0 to 1
    with pytest.raises(ValueError):
        calculator.fun3(-1, 1)
    with pytest.raises(ValueError):
        calculator.fun3(1, -1)
    with pytest.raises(ValueError):
        calculator.fun3(5, 0)  # Test zero input

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5, 1, 2) == 8  # Changed 0, 1 to 1, 2
    with pytest.raises(ValueError):
        calculator.fun4(-1, 1, 2)
    with pytest.raises(ValueError):
        calculator.fun4(1, -1, 2)
    with pytest.raises(ValueError):
        calculator.fun4(5, 0, 1)  # Test zero input

def test_fun5():
    assert calculator.fun5(10, 2) == 5.0
    assert calculator.fun5(5, 1) == 5.0
    with pytest.raises(ValueError):
        calculator.fun5(-1, 1)
    with pytest.raises(ValueError):
        calculator.fun5(1, -1)
    with pytest.raises(ValueError):
        calculator.fun5(10, 0)