import pytest
from main import Calculator

@pytest.fixture
def my_class_instance():
    return Calculator(10)

class TestCalculator:
    
    def test_add(self, my_class_instance):
        assert my_class_instance.add(10) == 20

    def test_subtract(self, my_class_instance):
        assert my_class_instance.subtract(10) == 0

    def test_mult(self, my_class_instance):
        assert my_class_instance.multiply(10) == 100

    def test_divide(self, my_class_instance):
        assert my_class_instance.divide(5) == 2

    def test_zero_division(self, my_class_instance):
        with pytest.raises(ZeroDivisionError):
            my_class_instance.divide(0)