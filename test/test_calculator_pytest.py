import pytest
import time
from src.demo.calculator import Calculator

@pytest.fixture()
def set_up():
    print("[pytest with fixture] start")
    yield
    print("[pytest with fixture] end")

class TestCalculator():

    @pytest.mark.parametrize(["num1", "num2", "total"], [(3, 5, 8), (1, 2, 3), (2, 2, 4)])
    def test_add(self, num1, num2, total):
        print(num1)
        print(num2)
        c = Calculator()
        result = c.add(num1, num2)
        assert result == total

    def test_sub(self):
        c = Calculator()
        result = c.sub(10, 5)
        assert result == 5

    @pytest.mark.usefixtures("set_up")
    def test_mul(self):
        c = Calculator()
        result = c.mul(5, 7)
        assert result == 35

    @pytest.mark.usefixtures("set_up")
    def test_div(self):
        c = Calculator()
        result = c.div(10, 5)
        assert result == 2


if __name__ == '__main__':
    pytest.main(['-s', 'test_calculator_pytest.py'])