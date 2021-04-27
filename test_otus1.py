# Треугольники

def test_tr_perimeter(my_triangle):
    assert my_triangle.perimeter() == 16


def test_tr_area(my_triangle):
    assert my_triangle.area() == 12


def test_tr_angles(my_triangle):
    assert my_triangle.my_angles() == 3


def test_tr_name(my_triangle):
    assert my_triangle.my_name() == "SomeTr"

def test_tr_add_area(my_triangle, my_rectangle):
    assert my_triangle.add_area(my_rectangle) == 47


# Прямоугольники

def test_rec_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 24


def test_rec_area(my_rectangle):
    assert my_rectangle.area() == 35


def test_rec_angles(my_rectangle):
    assert my_rectangle.my_angles() == 4


def test_rec_name(my_rectangle):
    assert my_rectangle.my_name() == "SomeRec"


def test_rec_add_area(my_rectangle, my_triangle):
    assert my_rectangle.add_area(my_triangle) == 47


# Квадраты

def test_sq_perimeter(my_square):
    assert my_square.perimeter() == 28


def test_sq_area(my_square):
    assert my_square.area() == 49


def test_sq_angles(my_square):
    assert my_square.my_angles() == 4


def test_sq_name(my_square):
    assert my_square.my_name() == "SomeSq"

def test_sq_add_area(my_square, my_circle):
    assert my_square.add_area(my_circle) == 77


# Окружности

def test_circle_perimeter(my_circle):
    assert int(my_circle.perimeter()) == 18


def test_circle_area(my_circle):
    assert int(my_circle.area()) == 28


def test_circle_angles(my_circle):
    assert my_circle.my_angles() == 0


def test_circle_name(my_circle):
    assert my_circle.my_name() == "SomeCircle"

def test_circle_add_area(my_circle, my_rectangle):
    assert my_circle.add_area(my_rectangle) == 63

