import pytest
from Lab11 import numbers_multiplication, nubmers_division, distance_between_points, quadratic_equation, geometric_progression_sum
#Денисова Карина 107а1

@pytest.mark.parametrize('num1, num2, res', [(4, 1, 4),
                                            (11, 0 , 0),
                                            (3, -2, -6),
                                            (-4, -2, 8),
                                            (5, 3, 15),])
def test_numbers_multiplication(num1, num2, res):
    """Тест умножения"""
    result = numbers_multiplication(num1, num2)
    assert result == res

@pytest.mark.parametrize('num1, num2, res', [(5, 0, "Error devision by zero"),
                                            (0, 3, 0),
                                            (6, 2, 3),
                                            (-5, 4, -1.25),
                                            (-8, -4, 2),])
def test_nubmers_division(num1, num2, res):
    """Тест деления"""
    result = nubmers_division(num1, num2)
    assert result == res

@pytest.mark.parametrize('x1, y1, x2, y2, res', [(3, 9, 3, 9, 0),
                                                (3, 3, 3, -1, 4),
                                                (-4, -1, 3, -1, 7),
                                                (4, 3, 1, 7, 5),
                                                (1, 2, 2, 1, 1.4142135623730951),])
def test_distance_between_points(x1, y1, x2, y2, res):
    """Тест нахождения расстояния между точками"""
    result = distance_between_points(x1, y1, x2, y2)
    assert result == res
        

@pytest.mark.parametrize('a, b, c, res', [(1, -5, 6, [2, 3]),
                                        (3, -5, 2, [0.6666666666666666, 1]),
                                        (4, 0, 0, 0),
                                        (2, 0, -8, [2, -2]),
                                        (2, -1, 1, "No solutions"),])
def test_quadratic_equation(a, b, c, res):
    """Тест решения квадратного уравнения"""
    result = quadratic_equation(a, b, c)
    assert result == res

@pytest.mark.parametrize('n, q, b1, res', [(5, 0.5, 8, 15.5),
                                          (5, 5, 1, 781),
                                          (10, -2, 2, -682),
                                          (5, 7, 7, 19607),
                                          (6, 2, 3, 189),])
def test_geometric_progression_sum(n, q, b1, res):
    """Тест нахождения суммы геометрической прогрессии"""
    result = geometric_progression_sum(n, q, b1)
    assert result == res

        
