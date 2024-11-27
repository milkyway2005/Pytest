#Денисова Карина 107а1

def numbers_multiplication(num1, num2):
    return num1*num2

def nubmers_division(num1, num2):
    if num2 == 0:
        return "Error devision by zero"
    return num1/num2

def distance_between_points(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            return "All numbers"
        return -(c/b)
    if b == 0:
        if -c/a < 0:
            return "No solutions"
        x = (-c/a)**0.5
        if x == 0:
            return 0
        return [x, -x]
    if c == 0:
        return [0, -b/a]
    D = (b**2 - 4*a*c)
    if D < 0:
        return "No solutions"
    return [(-b-D**0.5)/(2*a), (-b+D**0.5)/(2*a)]

def geometric_progression_sum(n, q, b1):
    return (b1*(q**n - 1))/(q-1)
