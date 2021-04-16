from figure import *
import pytest


@pytest.fixture
def my_triangle():
    return Triangle(name="SomeTr", a=5, b=5, c=6)


@pytest.fixture
def my_rectangle():
    return Rectangle(name="SomeRec", a=5, b=7)


@pytest.fixture
def my_square():
    return Square(name="SomeSq", a=7)

@pytest.fixture
def my_circle():
    return Circle(name="SomeCircle", r=3)
